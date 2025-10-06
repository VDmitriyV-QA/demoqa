from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        return str(self.find_element().text)

    def click(self):
        self.find_element().click()

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        try:
            return self.find_element().is_displayed()
        except NoSuchElementException:
            return False

    def check_count_elements(self, count):
        return len(self.find_elements()) == count

    def send_keys(self, text: str):
        self.find_element().send_keys(text)