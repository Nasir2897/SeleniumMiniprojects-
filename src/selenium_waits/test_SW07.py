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
def test_dragdrop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    driver.maximize_window()
    time.sleep(3)
    actions = ActionChains(driver)
    from_element = driver.find_element(By.ID,'column-a')
    to_element = driver.find_element(By.ID,'column-b')
    actions.click_and_hold(from_element).move_to_element(to_element).release(to_element).perform()
    time.sleep(5)
    driver.close()