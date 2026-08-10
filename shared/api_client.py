import requests


DEFAULT_TIMEOUT = 15


def get_json(url):
    """
    Sends an HTTP GET request and returns parsed JSON.

    Returns a standardized dictionary with:
    - status
    - data
    - error
    """

    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()

        return {
            "status": "success",
            "data": response.json(),
            "error": None
        }

    except requests.exceptions.RequestException as e:

        return {
            "status": "error",
            "data": None,
            "error": str(e)
        }
    

def post_json(url: str, payload: dict):
    """
    Send a POST request containing JSON and return a standardized response.
    """

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return {
            "status": "success",
            "data": response.json(),
            "error": None,
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "data": None,
            "error": str(e),
        }