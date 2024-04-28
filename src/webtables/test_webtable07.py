# example of hoverable mouse action
# Action builder basically used for mouse ponting and clicking events
# Action chains we can use keys,mouse,wheel also
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_07_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    hoverable = driver.find_element(By.ID,"hover")
    ActionChains(driver) \
        .move_to_element(hoverable) \
        .perform()
    time.sleep(100)