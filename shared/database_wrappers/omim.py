"""
OMIM Mendelian disease-gene wrapper.
"""

from shared.config import OMIM_API_KEY
from .base import success, error


def get_omim_disease_genes(
    disease_or_gene: str,
):
    """
    Retrieve Mendelian disease-gene relationships from OMIM.

    Parameters
    ----------
    disease_or_gene : str
        Disease or gene query.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    if not OMIM_API_KEY:
        return error(
            "OMIM",
            (
                "OMIM_API_KEY is not configured. "
                "Add an authorized OMIM API key to .env."
            ),
        )

    return error(
        "OMIM",
        (
            "OMIM API integration is pending "
            "authorized endpoint configuration."
        ),
    )