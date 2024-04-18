from selenium import webdriver
import time
import pytest
# Selenium 4
@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome() # POST request / Create the Session
    driver.get("https://app.vwo.com") # GET Request to URL param
    print(driver.title)
    assert  driver.title == "Login - VWO"
    time.sleep(5)
