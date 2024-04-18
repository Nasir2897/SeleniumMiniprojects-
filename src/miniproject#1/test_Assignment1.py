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
    # class ="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # < / a >
    time.sleep(5)
    element = driver.find_element(By.ID, value="btn-make-appointment")
    element.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    # < input
    # type = "text"
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value=""
    # autocomplete="off"
    # >
    email_element = driver.find_element(By.NAME, value="username")
    email_element.send_keys("John Doe")
    time.sleep(5)
    password_element = driver.find_element(By.NAME, value="password")
    password_element.send_keys("ThisIsNotAPassword")
    button_submit_element = driver.find_element(By.ID, value="btn-login")
    button_submit_element.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
