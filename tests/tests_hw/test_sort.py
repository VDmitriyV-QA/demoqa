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


def test_table_sorting(driver):
    driver.get("https://demoqa.com/webtables")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rt-th"))
    )

    header_selectors = [
        "div.rt-th:nth-child(1)",
        "div.rt-th:nth-child(2)",
        "div.rt-th:nth-child(3)",
        "div.rt-th:nth-child(4)",
        "div.rt-th:nth-child(5)",
        "div.rt-th:nth-child(6)"
    ]

    for selector in header_selectors:
        header = driver.find_element(By.CSS_SELECTOR, selector)
        header.click()

        WebDriverWait(driver, 5).until(
            lambda d: "sort-asc" in header.get_attribute("class") or
                      "sort-desc" in header.get_attribute("class")
        )

        assert "sort-asc" in header.get_attribute("class") or \
               "sort-desc" in header.get_attribute("class")