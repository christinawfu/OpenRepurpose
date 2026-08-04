"""
Shared helper functions used by all database wrappers.
"""

def success(source: str, data: dict):
    return {
        "status": "success",
        "source": source,
        "data": data,
    }


def error(source: str, message: str):
    return {
        "status": "error",
        "source": source,
        "data": {},
        "message": message,
    }

def not_implemented(source: str) -> dict:
    """
    Return a standardized placeholder response for wrappers
    that have not been implemented yet.
    """

    return {
        "status": "not_implemented",
        "source": source,
        "data": {},
        "message": f"{source} wrapper has not been implemented yet."
    }