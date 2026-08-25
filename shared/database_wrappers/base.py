"""
Shared utilities for OpenRepurpose database wrappers.
"""

from typing import Any, Dict


def success_result(
    source: str,
    data: Any,
) -> Dict[str, Any]:
    """
    Return a standardized successful API result.
    """

    return {
        "status": "success",
        "source": source,
        "data": data,
        "error": None,
    }


def error_result(
    source: str,
    error: str,
    data: Any = None,
) -> Dict[str, Any]:
    """
    Return a standardized failed API result.
    """

    return {
        "status": "error",
        "source": source,
        "data": data,
        "error": str(error),
    }


# --------------------------------------------------
# Backward-compatible aliases
# --------------------------------------------------

def success(
    source: str,
    data: Any,
) -> Dict[str, Any]:
    """
    Backward-compatible alias for success_result().
    """

    return success_result(
        source=source,
        data=data,
    )


def error(
    source: str,
    message: str,
    data: Any = None,
) -> Dict[str, Any]:
    """
    Backward-compatible alias for error_result().
    """

    return error_result(
        source=source,
        error=message,
        data=data,
    )


def not_implemented(
    source: str,
) -> Dict[str, Any]:
    """
    Return a standardized result for an unavailable wrapper.
    """

    return error_result(
        source=source,
        error="Wrapper not implemented.",
    )