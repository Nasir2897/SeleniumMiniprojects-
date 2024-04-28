import random

import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@allure.title("Login page of OrangeHRM website ")
@allure.description("Search for the user in file records.")
@allure.label("owner", "vani valaboju")
@allure.link("", name="Website")
@allure.testcase("TC-1")
def test_open_OrangeHRM():
    # <<<<<<<<<<< Load website and login phase >>>>>>>>
    # Open the orange hrm website
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="open webpage-screenshot", attachment_type=AttachmentType.PNG)

    # Enter credentials and click login
    element_username = driver.find_element(By.XPATH, "//input[@name='username']")
    element_username.send_keys("Admin")
    element_password = driver.find_element(By.XPATH, "//input[@name='password']")
    element_password.send_keys("admin123")
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="After login Dashboard-screenshot", attachment_type=AttachmentType.PNG)

    # <<<<<<<<<<< Load Admin page and add user profile phase >>>>>>>>
    # Click Admin link on dashboard page
    element_adminpage = driver.find_element(By.XPATH, "//a[contains(@href,'/web/index.php/admin/viewAdminModule')]")
    element_adminpage.click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Admin page-screenshot", attachment_type=AttachmentType.PNG)

    # click add button to open add new profile page
    adduser_btn = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    adduser_btn.click()
    driver.maximize_window()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Add user webpage-screenshot", attachment_type=AttachmentType.PNG)

    # Enter user role, employee name, status, username and passwords. click on save.
    element_icons = driver.find_elements(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])")
    element_userrole_icon = element_icons[0]
    element_userrole_icon.click()
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()

    element_status_icon = element_icons[1]
    element_status_icon.click()
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()
    time.sleep(5)

    element_empname = driver.find_element(By.XPATH,
                                          "//input[@placeholder='Type for hints...']")

    element_empname.send_keys("Brown")
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[1]").click()

    element_addusername = driver.find_element(By.XPATH,
                                              "//input[@class='oxd-input oxd-input--active'][@autocomplete='off']")
    username = "valabojuvani" + str(random.randint(100, 999))
    element_addusername.send_keys(username)

    time.sleep(3)
    element_passwords = driver.find_elements(By.XPATH,
                                             "//input[@class='oxd-input oxd-input--active'][@type='password'][@autocomplete='off']")

    element_password = element_passwords[0]
    element_password.send_keys("Vani@123*")
    element_confirmpassword = element_passwords[1]
    element_confirmpassword.send_keys("Vani@123*")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Add user details filled-screenshot", attachment_type=AttachmentType.PNG)

    save_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_btn.click()
    time.sleep(15)
    allure.attach(driver.get_screenshot_as_png(), name="Search webpage -screenshot", attachment_type=AttachmentType.PNG)

    # <<<<<<<<<<< Search for newly added user profile phase >>>>>>>>
    # Enter user role, employee name, status, username to search the user
    element_search_username = driver.find_elements(By.XPATH,
                                                  "//input[@class='oxd-input oxd-input--active']")[1]
    element_search_username.send_keys(username)
    time.sleep(3)
    element_search_icons = driver.find_elements(By.XPATH,
                                                "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])")

    element_search_userrole_icon = element_search_icons[0]
    element_search_userrole_icon.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()

    element_search_empname = driver.find_element(By.XPATH,
                                                 "//input[@placeholder='Type for hints...']")

    element_search_empname.send_keys("Brown")
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[1]").click()

    element_search_status_icon = element_search_icons[1]
    element_search_status_icon.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()
    allure.attach(driver.get_screenshot_as_png(), name="search webpage details filled-screenshot", attachment_type=AttachmentType.PNG)

    # click search button
    search_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_btn.click()
    time.sleep(5)

    # assert search results
    element_search_table_cells = driver.find_elements(By.XPATH, "//div[@class = 'oxd-table-cell oxd-padding-cell']")[1]
    assert element_search_table_cells.text == username
    allure.attach(driver.get_screenshot_as_png(), name="Search results-screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(10)
