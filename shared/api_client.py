import requests


DEFAULT_TIMEOUT = 15


def get_json(url: str, headers=None):
    """
    Send an HTTP GET request and return parsed JSON.
    """

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return {
            "status": "success",
            "data": response.json(),
            "error": None,
        }

    except requests.exceptions.RequestException as error:

        return {
            "status": "error",
            "data": None,
            "error": str(error),
        }


def post_json(url: str, payload: dict, headers=None):
    """
    Send an HTTP POST request containing JSON.
    """

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return {
            "status": "success",
            "data": response.json(),
            "error": None,
        }

    except requests.exceptions.RequestException as error:

        return {
            "status": "error",
            "data": None,
            "error": str(error),
        }