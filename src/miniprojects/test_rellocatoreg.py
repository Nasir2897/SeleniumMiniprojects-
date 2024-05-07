import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
def test_MiniAssignment7():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Register.html")
    first_name = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name.send_keys("vani")
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("valaboju")
    email_address = driver.find_element(By.XPATH,"//input[@type='email']")
    Address_txt = driver.find_element(locate_with(By.TAG_NAME,"textarea").above(email_address))
    Address_txt.send_keys("AlkapoorTownship")
    Ad_txt = driver.find_element(By.XPATH,"//textarea[@rows='3']")
    em_Ad = driver.find_element(locate_with(By.TAG_NAME,"input").below(Ad_txt))
    em_Ad.send_keys("kathirojuvani@gmail.com")
    e_Ad = driver.find_element(By.XPATH,"//input[@type='email']")
    phone_textbox = driver.find_element(locate_with(By.TAG_NAME, "input").below(e_Ad))
    phone_textbox.send_keys("1234567890")
    time.sleep(3)
    gen_btn = driver.find_element(By.XPATH,"//input[@value='FeMale']")
    gen_btn.click()
    time.sleep(5)
    password_input= driver.find_element(By.XPATH, "//input[@id='firstpassword']")
    confirm_textbox = driver.find_element(locate_with(By.TAG_NAME,"input").below(password_input))
    confirm_textbox.send_keys("vani09")
    time.sleep(2)
    confirm_password = driver.find_element(By.XPATH, "//input[@id='secondpassword']")
    password_box = driver.find_element(locate_with(By.TAG_NAME, "input").above(confirm_password))
    password_box.send_keys("vani09")
    time.sleep(5)
    ref = driver.find_element(By.XPATH,"//button[@id='Button1']")
    sub = driver.find_element(locate_with(By.TAG_NAME,"button").to_left_of(ref))
    sub.click()
    time.sleep(5)
    submit_btn= driver.find_element(By.XPATH, "//button[@id='submitbtn']")
    refre_btn= driver.find_element(locate_with(By.TAG_NAME, "button").to_right_of(submit_btn))
    refre_btn.click()
    time.sleep(5)
