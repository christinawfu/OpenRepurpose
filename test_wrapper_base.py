from shared.database_wrappers.base import (
    success_result,
    error_result,
)


def test_success_result():

    result = success_result(
        source="Test",
        data={"value": 123},
    )

    assert result["status"] == "success"
    assert result["source"] == "Test"
    assert result["data"]["value"] == 123
    assert result["error"] is None


def test_error_result():

    result = error_result(
        source="Test",
        error="Something failed.",
    )

    assert result["status"] == "error"
    assert result["source"] == "Test"
    assert result["error"] == "Something failed."
    assert result["data"] is None


print("Wrapper base tests passed.")