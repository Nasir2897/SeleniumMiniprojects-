from selenium import webdriver
import time
import pytest
# Selenium 4
@pytest.mark.smoke
def test_open_browsers():
    driver = webdriver.Chrome() # POST request / Create the Session
    driver.get("https://bing.com/chat") # GET Request to URL param
    time.sleep(10)
    driver.get("https://google.com")
    print(driver.title)
