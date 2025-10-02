from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demoqa_page = DemoQA(browser)
    demoqa_page.visit()

    expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    actual_text = demoqa_page.footer.get_text()

    assert actual_text == expected_text


def test_check_center_text(browser):
    demoqa_page = DemoQA(browser)
    demoqa_page.visit()

    demoqa_page.click_btn_elements()

    expected_text = 'Please select an item from left to start practice.'
    actual_text = demoqa_page.center_text.get_text()

    assert actual_text == expected_text

def test_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.elements.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()