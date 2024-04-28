import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_02_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID,"clickable")
    actions = ActionChains(driver)
    time.sleep(5)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys('vani').key_up(Keys.SHIFT).perform()
    time.sleep(3)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("K").perform()
    time.sleep(10)

