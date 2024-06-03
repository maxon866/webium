import pytest
from webium.driver import close_driver


@pytest.fixture(autouse=True, scope="session")
def close_browser_after_run():
    yield
    close_driver()
