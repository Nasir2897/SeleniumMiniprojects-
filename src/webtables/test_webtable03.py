# example of click mouse action->Normal and action will performed
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_03_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID,"click")
    ActionChains(driver)\
        .click(clickable)\
        .perform()
    assert "resultPage.html" in driver.current_url
    time.sleep(10)