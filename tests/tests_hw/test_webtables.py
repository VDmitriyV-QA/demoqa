from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def test_webtables_add_edit_delete():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    time.sleep(2)

    driver.find_element(By.ID, "addNewRecordButton").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "firstName").is_displayed()

    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "firstName").is_displayed()

    driver.find_element(By.ID, "firstName").send_keys("Ivan")
    driver.find_element(By.ID, "lastName").send_keys("Ivanov")
    driver.find_element(By.ID, "userEmail").send_keys("ivan@mail.com")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "department").send_keys("IT")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Ivan" in driver.page_source
    assert "Ivanov" in driver.page_source

    driver.find_element(By.ID, "edit-record-4").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "firstName").is_displayed()

    first_name = driver.find_element(By.ID, "firstName")
    first_name.clear()
    first_name.send_keys("Petr")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert "Petr" in driver.page_source

    driver.find_element(By.ID, "delete-record-4").click()
    time.sleep(2)
    assert "Petr" not in driver.page_source

    driver.quit()


def test_webtables_pagination():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    time.sleep(2)

    select = Select(driver.find_element(By.XPATH, "//select"))
    select.select_by_value("5")
    time.sleep(2)

    next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
    previous_button = driver.find_element(By.XPATH, "//button[text()='Previous']")

    assert next_button.get_attribute("disabled") is not None
    assert previous_button.get_attribute("disabled") is not None

    for i in range(3):
        driver.find_element(By.ID, "addNewRecordButton").click()
        time.sleep(1)

        driver.find_element(By.ID, "firstName").send_keys(f"User{i}")
        driver.find_element(By.ID, "lastName").send_keys(f"Last{i}")
        driver.find_element(By.ID, "userEmail").send_keys(f"user{i}@mail.com")
        driver.find_element(By.ID, "age").send_keys("25")
        driver.find_element(By.ID, "salary").send_keys("30000")
        driver.find_element(By.ID, "department").send_keys("QA")

        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

    page_info = driver.find_element(By.XPATH, "//span[@class='-pageInfo']").text
    assert "2" in page_info

    assert next_button.get_attribute("disabled") is None

    next_button.click()
    time.sleep(2)

    previous_button.click()
    time.sleep(2)

    driver.quit()