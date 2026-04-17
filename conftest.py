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
    return url


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    logger = logging.getLogger("TEST")
    logger.info(f"\n===== RUNNING: {item.name} =====")
    if "browser" in item.fixturenames:
        browser_name = item.config.getoption("--browser")
        allure.dynamic.title(f"{item.name} [{browser_name}]")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        api_client = item.funcargs.get("api_client")
        if api_client and hasattr(api_client, "request_history") and api_client.request_history:
            allure.attach(
                "\n\n".join(api_client.request_history),
                name="API cURL History (FAILED)",
                attachment_type=allure.attachment_type.TEXT
            )

        driver = item.funcargs.get("browser")
        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="UI Screenshot (FAILED)",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")