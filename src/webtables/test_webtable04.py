# example of click and Hold->click but we will not release.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_04_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID,"click")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .perform()

    time.sleep(10)