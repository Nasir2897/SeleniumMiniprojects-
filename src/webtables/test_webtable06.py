# example of doubleclick mouse action
# \-backslash is used for continuation
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_06_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID,"clickable")
    ActionChains(driver) \
        .double_click(clickable) \
        .perform()
    time.sleep(100)
