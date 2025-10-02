from pages.demoqa import DemoQA


def test_go_to_page_elements(browser):
    demoqa_page = DemoQA(browser)
    demoqa_page.visit()
    demoqa_page.click_btn_elements()

    assert 'elements' in demoqa_page.get_url()
    assert demoqa_page.center_text.get_text() == 'Please select an item from left to start practice.'