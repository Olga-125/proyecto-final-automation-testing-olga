import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")

    service = Service("C:/WebDriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver
