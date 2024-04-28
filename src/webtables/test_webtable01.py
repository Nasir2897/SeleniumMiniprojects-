import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME,"firstname")
    last_name = driver.find_element(By.NAME, "lastname")

    # Create Object of Action Chains Class
    actions = ActionChains(driver)
    time.sleep(5)
    # Send Keys but with the Shift
    actions\
        .key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name,"the testing academy")\
        .key_up(Keys.SHIFT).perform()
    time.sleep(5)
    actions \
        .key_down(Keys.SHIFT) \
        .send_keys_to_element(last_name, "py automation batch") \
        .key_up(Keys.SHIFT).perform()
    time.sleep(20)



    # row_element = driver.find_elements[By.XPATH,"//table[contains(@id,'cust')]/tbody/tr"
    # row = len(row_element)
    # print(row)
    #
    # column_element = driver.find_elements[By.XPATH, "//table(contains[@id,'cust')]/tbody/tr[2]/td"
    # col = len(column_element)
    # print(col)
    #
    # first_part="//table[contains(@id,'cust')]/tbody/tr["
    # second_part = "]/td["
    # third_part = "]"
    #
    # for i in range(2,row+1):
    #     for j in range(1,col+1):
    #         dynmamic_path = (f"{first_part}{i}{second_part}{j}{third_part})"
    #         data=driver.find_element(By.XPATH,'dynamic_path')
    #         print(data.text,end=" ")
    #
    #
    #
