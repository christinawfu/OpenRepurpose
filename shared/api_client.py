"""
Shared HTTP utilities for OpenRepurpose.
"""

from typing import Any, Dict, Optional

import requests


DEFAULT_TIMEOUT = 20


def get_json(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Any:
    """
    Perform a GET request and return parsed JSON.

    Raises an exception when the request fails so that
    individual database wrappers can convert the failure
    into a standardized error result.
    """

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=timeout,
    )

    response.raise_for_status()

    return response.json()


def post_json(
    url: str,
    json: Optional[Dict[str, Any]] = None,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Any:
    """
    Perform a POST request and return parsed JSON.

    This is used by APIs such as Open Targets
    that accept structured request bodies.
    """

    response = requests.post(
        url,
        json=json,
        params=params,
        headers=headers,
        timeout=timeout,
    )

    response.raise_for_status()

    return response.json()