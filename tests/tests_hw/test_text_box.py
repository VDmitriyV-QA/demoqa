from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_text_box():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")

    name_text = "Ivan Ivanov"
    address_text = "Moscow Street 123"

    driver.find_element(By.ID, "userName").send_keys(name_text)
    driver.find_element(By.ID, "currentAddress").send_keys(address_text)

    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    time.sleep(1)
    submit.click()
    time.sleep(2)

    output = driver.find_element(By.ID, "output")
    name_result = output.find_element(By.ID, "name").text
    address_result = output.find_element(By.ID, "currentAddress").text

    assert name_text in name_result
    assert address_text in address_result

    driver.quit()