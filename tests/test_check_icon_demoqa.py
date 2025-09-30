from pages.demoqa import DemoQA

def test_check_icon(browser):
    demoqa_page = DemoQA(browser)
    demoqa_page.visit()
    assert demoqa_page.exist_icon()