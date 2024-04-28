# example of drag and drop
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_08_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    draggable = driver.find_element(By.ID,"draggable")
    droppable = driver.find_element(By.ID,"droppable")
    time.sleep(5)
    ActionChains(driver).drag_and_drop(draggable,droppable).perform()
    time.sleep(5)