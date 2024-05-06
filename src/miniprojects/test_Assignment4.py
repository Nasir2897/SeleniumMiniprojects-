import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
@pytest.mark.smoke
@allure.title("Login page of ebay website ")
@allure.description("Give me the cheapest one from the list.")
@allure.label("owner", "vani valaboju")
@allure.link("https://www.ebay.com/", name="Website")
@allure.testcase("TC-1")

def test_open_ebay():
        driver = webdriver.Chrome()
        driver.get("https://www.ebay.com/")
        driver.maximize_window()
        time.sleep(5)
        assert driver.current_url == "https://www.ebay.com/"
        allure.attach(driver.get_screenshot_as_png(), name='Home_Page_Screenshot', attachment_type=AttachmentType.PNG)

        search_element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
        search_element.send_keys("16gb")

        search_btn_element = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
        search_btn_element.click()
        allure.attach(driver.get_screenshot_as_png(), name='Product_Page_Screenshot',
                      attachment_type=AttachmentType.PNG)

        time.sleep(5)
        list_of_elements = driver.find_elements(By.XPATH, "//span[@role='heading']")

        for product in list_of_elements:
                product_name = product.text
                print(product_name)

        product_price_element_list = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
        prices = []
        for prices in product_price_element_list:
                product_price = prices.text
                print(product_price)
                x = product_price.replace("$", " ").strip()
                prices.append(x)

        prices.sort()

        # min_price = prize[1]
        print(f"cheapest price is {prices[1]}")
        allure.attach(driver.get_screenshot_as_png(), name='cheapest_price_Page_Screenshot',
                      attachment_type=AttachmentType.PNG)

        time.sleep(5)
        driver.quit()