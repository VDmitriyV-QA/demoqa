import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def is_page_available(driver, url, timeout=10):
    try:
        driver.get(url)
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return True
    except TimeoutException:
        return False


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_modal_dialogs(driver):
    url = "https://demoqa.com/modal-dialogs"

    if not is_page_available(driver, url):
        pytest.skip("Страница недоступна")

    small_modal_btn = (By.ID, "showSmallModal")
    large_modal_btn = (By.ID, "showLargeModal")
    close_small_modal = (By.ID, "closeSmallModal")
    close_large_modal = (By.ID, "closeLargeModal")
    modal_content = (By.CLASS_NAME, "modal-content")

    driver.find_element(*small_modal_btn).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(modal_content))
    driver.find_element(*close_small_modal).click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(modal_content))

    driver.find_element(*large_modal_btn).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(modal_content))
    driver.find_element(*close_large_modal).click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(modal_content))