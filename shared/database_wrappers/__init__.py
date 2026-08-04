"""
Public interface for all database wrappers.
"""

from .openfda import get_faers_events

from .gtex import get_gtex_expression

from .hpa import get_hpa_protein

from .disgenet import get_disgenet_associations

from .omim import get_omim_disease_genes

from .ontology import normalize_disease_name

from .opentargets import get_target_disease_associations

from .clinvar import get_clinvar_variants

from .chembl import get_chembl_drug_info