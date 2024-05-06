import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton


# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in drag and drop website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_javascript():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.maximize_window()
    # button = driver.find_element(By.XPATH ,"//button[@onclick='addElement']")
    # button.click()
    # suppose the above code is not working we can use javascript code to click on this button also
    #JavaScript Execoutor

    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    js_ex = driver.execute_script
    js_ex("arguments[0].click()",button)
    js_ex("arguments[0].click()",button)
    time.sleep(10)
    driver.quit()