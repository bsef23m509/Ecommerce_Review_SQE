# This file can be extended to configure fixtures and start/stop server if needed.
# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome-stable"
    options.add_argument("--headless=new")
    service = Service("/usr/bin/chromedriver")
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()
