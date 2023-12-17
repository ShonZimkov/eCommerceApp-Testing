import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        print('Lunching Chrome browser.....')
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Lunching Firefox browser.....')
        return driver
    else:
        driver = webdriver.Edge()
        print('Lunching MS Edge browser.....')
        return driver

def pytest_addoption(parser): #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser Value to the setup method
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'eCommerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Shons'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)