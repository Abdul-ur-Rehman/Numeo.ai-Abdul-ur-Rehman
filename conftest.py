import pytest
from utilities.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("driver", None)

            if driver and hasattr(driver, "get_screenshot_as_file"):

                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(driver, file_name)

                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)

