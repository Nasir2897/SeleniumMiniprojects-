from selenium import webdriver
import time
import pytest
# Selenium 4
@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    driver.back()
    driver.get("https://bing.com/chat")
    print(driver.title)
    driver.forward()
    print(driver.title)
    driver.back()
    driver.get("https://bing.com/chat")
    driver.refresh()
    time.sleep(5)
    driver.quit()