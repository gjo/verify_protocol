import pytest

@pytest.fixture(scope="session")
def verify_object():
    from verify_protocol import verify_object

    return verify_object
