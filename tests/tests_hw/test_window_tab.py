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


def test_home_link(driver):
    driver.get("https://demoqa.com/links")

    home_link = (By.ID, "simpleLink")
    link_element = driver.find_element(*home_link)

    assert link_element.text == "Home"

    assert link_element.get_attribute("href") == "https://demoqa.com/"

    original_window = driver.current_window_handle

    link_element.click()

    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))

    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    WebDriverWait(driver, 5).until(EC.url_to_be("https://demoqa.com/"))
    assert driver.current_url == "https://demoqa.com/"

    driver.close()
    driver.switch_to.window(original_window)