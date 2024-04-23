import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("Verify that codepen registered page is opened ")
@allure.description("TC#1 - simple enter all email,password,confirm password and click submit button.")
def test_open_ebay():
        driver = webdriver.Chrome()
        driver.get("https://www.ebay.com/")
        time.sleep(5)
