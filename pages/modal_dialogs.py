import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.components import WebElement


class BasePage:
    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        from selenium.webdriver.common.by import By
        return self.driver.find_element(By.CSS_SELECTOR, locator)


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # Более специфичный локатор для кнопок модальных окон
        self.buttons = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 button')
        self.icon = WebElement(driver, 'header > a')