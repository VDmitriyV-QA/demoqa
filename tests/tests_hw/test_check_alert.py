import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_timer_alert(driver):
    driver.get("https://demoqa.com/alerts")

    timer_alert_btn = (By.ID, "timerAlertButton")
    driver.find_element(*timer_alert_btn).click()

    WebDriverWait(driver, 6).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()