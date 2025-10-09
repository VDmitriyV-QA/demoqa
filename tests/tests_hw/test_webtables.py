# import time
# import allure
# from page_tables import Tables
#
#
# def test_tables(browser):
#     page_tables = Tables(browser)
#
#     page_tables.visit()
#     assert not page_tables.no_data.exist()
#
#
#     while page_tables.btn_delete_row.exist():
#         page_tables.btn_delete_row.click()
#
#         time.sleep(2)
#         assert page_tables.no_data.exist()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_webtables_add_edit_delete():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")

    driver.find_element(By.ID, "addNewRecordButton").click()
    time.sleep(1)

    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    driver.find_element(By.ID, "firstName").send_keys("Ivan")
    driver.find_element(By.ID, "lastName").send_keys("Ivanov")
    driver.find_element(By.ID, "userEmail").send_keys("ivan@mail.com")
    driver.find_element(By.ID, "age").send_keys("30")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "department").send_keys("IT")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    driver.find_element(By.ID, "edit-record-4").click()
    time.sleep(1)

    first_name = driver.find_element(By.ID, "firstName")
    first_name.clear()
    first_name.send_keys("Petr")

    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    driver.find_element(By.ID, "delete-record-4").click()
    time.sleep(2)

    driver.quit()


def test_webtables_pagination():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")

    rows_select = driver.find_element(By.XPATH, "//select")
    driver.execute_script("arguments[0].scrollIntoView();", rows_select)
    time.sleep(1)
    rows_select.click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//option[@value='5']").click()
    time.sleep(2)

    next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
    previous_button = driver.find_element(By.XPATH, "//button[text()='Previous']")

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

    next_button.click()
    time.sleep(2)

    previous_button.click()
    time.sleep(2)

    driver.quit()