import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQA


def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    # Проверяем, что кнопок модальных окон на странице - 2 шт
    actual_count = len(modal_page.buttons.find_elements())
    print(f"Найдено кнопок модальных окон: {actual_count}")

    # Проверим все кнопки на странице
    buttons = modal_page.buttons.find_elements()
    for i, button in enumerate(buttons):
        print(f"Кнопка {i}: {button.text}")

    # На странице должно быть 2 кнопки модальных окон
    assert actual_count == 2, f"Ожидалось 2 кнопки модальных окон, но найдено {actual_count}"


def test_navigation_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    # b. обновить страницу
    browser.refresh()

    # c. перейти на главную страницу через иконку
    modal_page.icon.click()

    # d. сделать шаг назад стрелкой браузера
    browser.back()

    # e. установить размеры экрана 900x400
    browser.set_window_size(900, 400)
    time.sleep(1)

    # f. сделать шаг вперед стрелкой браузера
    browser.forward()

    # g. вызвать проверку иконки на главной странице
    demoqa_page = DemoQA(browser)
    assert demoqa_page.exist_icon()

    # h. проверить title на главной
    assert "DEMOQA" in browser.title.upper()

    # i. вернуть размеры экрана по умолчанию 1000x1000
    browser.set_window_size(1000, 1000)