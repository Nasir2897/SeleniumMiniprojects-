from selenium import webdriver
import time
import pytest
# Selenium 4
@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome() # POST request / Create the Session
    time.sleep((20))