mport pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with


@pytest.mark.smoke
@allure.title("Verify that codepen registered page is opened ")
@allure.description("TC#1 - simple enter all email,password,confirm password and click submit button.")
def test_open_CodePen():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    element_email = driver.find_element(locate_with(By.XPATH,"//input[@id='email']").below('username')
    element_email.send_keys("vani.v3509@gmail.com")
    time.sleep(3)
    element_password = driver.find_element(By.XPATH,"//input[@id='password']")
    element_password.send_keys(123456)
    time.sleep(3)
    element_againpass=driver.find_element(By.XPATH,"//input[@id='password2']")
    element_againpass.send_keys(123456)
    time.sleep(3)
    submit_btn = driver.find_element(By.XPATH, value="//button[text()='Submit']")
    submit_btn.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    assert (driver.find_element(By.XPATH,"//input[@id='username']/following::small").text
            == "Username must be at least 3 characters")
    driver.quit()
