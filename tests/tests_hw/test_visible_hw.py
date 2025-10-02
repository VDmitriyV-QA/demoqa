import time
import pytest
from pages.accordion import Accordion


class TestVisibleAccordion:
    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_visible_accordion(self, browser):
        accordion_page = Accordion(browser)
        accordion_page.visit()

        assert accordion_page.section1_content.visible()

        accordion_page.section1_heading.click()

        time.sleep(2)

        assert not accordion_page.section1_content.visible()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_visible_accordion_default(self, browser):
        accordion_page = Accordion(browser)
        accordion_page.visit()

        assert not accordion_page.section2_content_p1.visible()
        assert not accordion_page.section2_content_p2.visible()
        assert not accordion_page.section3_content.visible()