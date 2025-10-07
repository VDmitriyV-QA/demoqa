from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_form_validate():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")

    first_name = driver.find_element(By.ID, "firstName")
    assert first_name.get_attribute("placeholder") == "First Name"

    last_name = driver.find_element(By.ID, "lastName")
    assert last_name.get_attribute("placeholder") == "Last Name"

    email = driver.find_element(By.ID, "userEmail")
    assert email.get_attribute("placeholder") == "name@example.com"
    assert email.get_attribute("pattern") is not None

    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    time.sleep(1)
    submit.click()
    time.sleep(2)

    form = driver.find_element(By.ID, "userForm")
    assert "was-validated" in form.get_attribute("class")

    driver.quit()