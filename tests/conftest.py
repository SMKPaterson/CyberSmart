import logging
import pytest
from selenium import webdriver


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.get("https://dat-shopping.herokuapp.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()