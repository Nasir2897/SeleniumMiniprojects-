from selenium import webdriver
import time
import pytest
# Selenium 4
from selenium.webdriver.common.by import By
@pytest.mark.smoke
def test_wologin_negative_tc():
    driver = webdriver.Chrome() # POST request / Create the Session
    driver.get("https://app.vwo.com")
    # #1 - id-> className-> name-> tagName-> linktext and PartialLinkText
    # #2 - css Selector-> xpath(sure shot way to find the element in HTML)
    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >
    email_element = driver.find_element(By.NAME,value="username")
    email_element.send_keys("admin")
    # < input
    #type = "password"
    # class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # >

    password_element = driver.find_element(By.ID, value="login-password")
    password_element.send_keys("admin")

    button_submit_element = driver.find_element(By.ID,value= "js-login-btn")
    button_submit_element.click()
    time.sleep(5)

    error_msg_element = driver.find_element(By.ID,value="js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    time.sleep(10)
    driver.quit()
