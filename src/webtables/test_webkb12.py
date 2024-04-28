import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def test_kb_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    time.sleep(3)
    actions = ActionChains(driver)
    input_element=driver.find_element(By.ID,value="textInput")
    input_element.send_keys("Selenium")
    # actions.send_keys("Selenium")
    time.sleep(5)
    driver.quit()