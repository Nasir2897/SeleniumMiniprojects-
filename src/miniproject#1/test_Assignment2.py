import time
import pytest
import  allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("Verify that login is working in cura website")
@allure.description("TC#1 - simple login check on cura katalon website.")
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
    make_appointment_btn = driver.find_element(By.LINK_TEXT,value="Make Appointment")
    make_appointment_btn.click()
    allure.attach(driver.get_screenshot_as_png(),name="login-screenshot",attachment_type=AttachmentType.PNG)
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" # "Message#1:Assertion Failed message"
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
    username = driver.find_element(By.NAME, value="username")
    username.send_keys("John Doe")
    time.sleep(5)
    password = driver.find_element(By.NAME, value="password")
    password.send_keys("ThisIsNotAPassword")
    submit_btn = driver.find_element(By.ID, value="btn-login")
    submit_btn.click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/#appointment"  # "Message#2:Error wrong URL"
    driver.quit()
