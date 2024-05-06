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
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_positive():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(3)
    button_jsalert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    button_jsalert.click()
    time.sleep(5)
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    button_jsconfirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    button_jsconfirm.click()
    time.sleep(5)
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    button_jsprompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button_jsprompt.click()
    time.sleep(5)
    wait = WebDriverWait(driver,timeout= 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("vani")
    time.sleep(5)
    alert.accept()
    #alert.dismiss()
    time.sleep(5)
    result = driver.find_element(By.ID,'result')
    print(result.text)
    assert "vani" in result.text