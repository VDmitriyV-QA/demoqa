from pages.browser_tab import BrowserTab
import time


def test_browser_tab(browser):
    page_browser = BrowserTab(browser)
    page_browser.visit()

    assert len(browser.windows_handles) == 1
    page_browser.new_tab.click()
    time.sleep(2)
    assert len(browser.windows_handles) == 2

    browser.switch_to.window(browser.windows_handles[1])
    time.sleep(2)
