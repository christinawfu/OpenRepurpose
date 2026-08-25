"""
OMIM wrapper.

Provides a controlled interface for OMIM disease-gene queries.

OMIM API access requires an OMIM API key.
"""

from shared.config import OMIM_API_KEY
from .base import success_result, error_result


def get_omim_disease_genes(
    disease_or_gene: str,
) -> dict:
    """
    Retrieve OMIM Mendelian disease-gene relationships.

    OMIM access requires an API key.

    Parameters
    ----------
    disease_or_gene:
        Disease name, gene symbol, or OMIM identifier.

    Returns
    -------
    dict
        Standardized OpenRepurpose response.
    """

    if not OMIM_API_KEY:

        return error_result(
            source="OMIM",
            error=(
                "OMIM_API_KEY is not configured. "
                "OMIM API access requires an OMIM API key."
            ),
        )

    # ------------------------------------------------------
    # OMIM API implementation will be enabled once the
    # project has a valid OMIM API key.
    # ------------------------------------------------------

    return error_result(
        source="OMIM",
        error=(
            "OMIM API key detected, but the OMIM endpoint "
            "has not yet been enabled in this MVP."
        ),
    )