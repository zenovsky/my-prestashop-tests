import logging

import allure
import pytest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("test.log")],
)


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://localhost:8081")
    parser.addoption("--executor", default="local")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--video", action="store_true", default=False)
    parser.addoption("--browser_version", default=None)


@pytest.fixture(scope="session")
def base_url(request):
    url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    return url


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    logger = logging.getLogger("TEST")
    logger.info(f"\n===== RUNNING: {item.name} =====")
    if "browser" in item.fixturenames:
        browser_name = item.config.getoption("--browser")
        allure.dynamic.title(f"{item.name} [{browser_name}]")
