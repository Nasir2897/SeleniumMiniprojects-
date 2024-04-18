from selenium import webdriver
import time
import pytest
# Selenium 4
from selenium.webdriver.common.by import By
@pytest.mark.smoke
def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    #  class ="btn btn-dark btn-lg"
    #  >
    #  Make Appointment
    #  < / a >


    # We should interact with the HTML elements.
    # Find the element the anchor tag - button
    # Click on it

    # #1 - id, className, name, tagName, linktext and PartialLinkText
    # #2 - css Selector,xpath(sure shot way to find the element in HTML)
    element = driver.find_element(By.ID,value="btn-make-appointment")
    element.click()
    driver.back()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert  driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    driver.quit()