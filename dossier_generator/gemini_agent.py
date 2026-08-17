"""
Gemini-powered OpenRepurpose evidence agent.

Uses the current Google GenAI Python SDK.
"""

from google import genai

from shared.config import GEMINI_API_KEY

from shared.database_wrappers import (
    get_ensembl_id,
    get_target_disease_associations,
    get_gtex_expression,
    get_hpa_protein,
    get_clinvar_variants,
    get_chembl_drug_info,
    get_faers_events,
    normalize_disease_name,
)


if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def tool_get_ensembl_id(
    gene_symbol: str,
) -> dict:
    """Find the Ensembl identifier for a gene symbol."""

    return get_ensembl_id(
        gene_symbol
    )


def tool_get_opentargets(
    gene_symbol: str,
) -> dict:
    """Find diseases associated with a target gene using Open Targets."""

    return get_target_disease_associations(
        gene_symbol
    )


def tool_get_gtex(
    gene_symbol: str,
) -> dict:
    """Retrieve GTEx tissue RNA expression for a gene."""

    return get_gtex_expression(
        gene_symbol
    )


def tool_get_hpa(
    gene_symbol: str,
) -> dict:
    """Retrieve Human Protein Atlas protein evidence for a gene."""

    return get_hpa_protein(
        gene_symbol
    )


def tool_get_clinvar(
    gene_symbol: str,
) -> dict:
    """Retrieve ClinVar variant records for a gene."""

    return get_clinvar_variants(
        gene_symbol
    )


def tool_get_chembl(
    drug_name: str,
) -> dict:
    """Retrieve ChEMBL information for a drug or molecule."""

    return get_chembl_drug_info(
        drug_name
    )


def tool_get_faers(
    drug_name: str,
) -> dict:
    """Retrieve post-market FAERS safety information for a drug."""

    return get_faers_events(
        drug_name
    )


def tool_normalize_disease(
    disease_name: str,
) -> dict:
    """Normalize a disease name to a canonical MONDO ontology identifier."""

    return normalize_disease_name(
        disease_name
    )


TOOLS = [
    tool_get_ensembl_id,
    tool_get_opentargets,
    tool_get_gtex,
    tool_get_hpa,
    tool_get_clinvar,
    tool_get_chembl,
    tool_get_faers,
    tool_normalize_disease,
]


with open(
    "dossier_generator/system_prompt.md",
    "r",
    encoding="utf-8",
) as file:

    SYSTEM_PROMPT = file.read()


def run_agent(
    target: str,
    drug: str,
    disease: str,
):
    """
    Run the Gemini evidence agent.

    Returns a dictionary so that the caller can distinguish
    successful Gemini synthesis from API failures.
    """

    request = f"""
Investigate this biomedical drug-repurposing question.

Target gene: {target}
Drug: {drug}
Disease: {disease}

Use the available biomedical database tools to collect evidence.

Then provide a structured scientific synthesis.

Clearly distinguish:

- direct evidence
- indirect evidence
- database associations
- genetic evidence
- tissue evidence
- safety signals
- evidence gaps

Do not invent evidence.

If a database is unavailable, explicitly state that
the source was unavailable.
"""

    try:

        chat = client.chats.create(
            model="gemini-3.6-flash",
            config={
                "system_instruction": SYSTEM_PROMPT,
                "tools": TOOLS,
            },
        )

        response = chat.send_message(
            message=request
        )

        return {
            "status": "success",
            "model": "gemini-3.6-flash",
            "summary": response.text,
        }

    except Exception as error:

        error_text = str(error)

        if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:

            return {
                "status": "quota_exceeded",
                "model": "gemini-3.6-flash",
                "summary": "",
                "error": (
                    "Gemini API quota was exceeded. "
                    "Evidence collection completed, but "
                    "AI synthesis was unavailable."
                ),
            }

        return {
            "status": "error",
            "model": "gemini-3.6-flash",
            "summary": "",
            "error": error_text,
        }