import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in awesomeqa website")
@allure.description("TC#1 - Simple Login check on awesomeqa Website.")
def test_awesomeqa():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")