import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def launchBrowser(request):
    try:
        global driver
        browser = request.config.getoption("browser_name")
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--allow-running-insecure-content")
            #chrome_options.add_argument("--incognito")
            chrome_options.add_argument("ignore-certificate-errors")
            driver = webdriver.Chrome(executable_path="C:\pythonsel\Softwares\chromedriver.exe", options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--start-maximized")
            firefox_options.add_argument("--disable-popup-blocking")
            firefox_options.add_argument("ignore-certificate-errors")
            driver = webdriver.Firefox(executable_path="C:\pythonsel\Softwares\geckodriver.exe", options=firefox_options)
        driver.implicitly_wait(10)
        driver.get("https://www.flipkart.com/")
        request.cls.driver = driver
        yield
        driver.quit()
    except Exception as e:
        print(e)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    try:
        pytest_html = item.config.pluginmanager.getplugin('html')

        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "launchBrowser":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra
    except Exception as e:
        print(e)


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

