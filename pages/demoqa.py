from selenium.common.exceptions import NoSuchElementException
from pages.Base_Page import BasePage
from components.components import WebElement

class DemoQA(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, 'header > a')
        self.footer = WebElement(driver, 'footer span')
        self.btn_elements = WebElement(driver, 'div.home-body > div > div:nth-child(1)')
        self.center_text = WebElement(driver, 'div.col-12.mt-4.col-md-6')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

    def exist_btn_elements(self):
        try:
            self.btn_elements.find_element()
        except NoSuchElementException:
            return False
        return True

    def click_btn_elements(self):
        self.btn_elements.click()