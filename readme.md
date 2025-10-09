##  Задание №7

### Цели задания:
1. Реализовать метод `get_text()` в классе компонентов
2. Создать тесты для проверки текстовых элементов на страницах DemoQA

### Реализованные тест-кейсы:

#### 1. Проверка текста в подвале главной страницы
- **URL:** https://demoqa.com/
- **Проверка:** Текст в подвале должен соответствовать `© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.`

#### 2. Проверка текста на странице Elements
- **URL:** https://demoqa.com/
- **Действие:** Клик по кнопке "Elements"
- **Проверка:** Текст по центру должен соответствовать `Please select an item from left to start practice.`

##  Технологии


## Задание №8

### Цели задания:
1. Реализовать метод `visible()` в классе компонентов для проверки видимости элементов
2. Создать тесты для проверки работы аккордеона на странице DemoQA
3. Проверить отображение/скрытие контента при взаимодействии с элементами

### Реализованные тест-кейсы:

#### 1. test_visible_accordion - Проверка работы аккордеона
- **URL:** https://demoqa.com/accordian
- **Действия:**
  - Проверить, что элемент `#section1Content > p` виден
  - Кликнуть на `#section1Heading`
  - Добавить `time.sleep(2)`
  - Проверить, что элемент `#section1Content > p` НЕ виден

#### 2. test_visible_accordion_default - Проверка состояния по умолчанию
- **URL:** https://demoqa.com/accordian
- **Проверка:** Следующие элементы по умолчанию скрыты:
  - `#section2Content > p:nth-child(1)`
  - `#section2Content > p:nth-child(2)`
  - `#section3Content > p`

## Технологии

- **Python 3.x**
- **Selenium WebDriver**
- **PyTest** с параметризацией тестов
- **Page Object Pattern**
- **Time** модуль для пауз

##  Установка и запуск

1. **Установите зависимости:**
```bash
pip install -r requirements.txt

# Домашнее задание №10 - Автоматизация тестирования с Selenium

Этот проект содержит автоматизированные тесты для веб-сайта DemoQA, написанные на Python с использованием Selenium WebDriver.


## Описание тестов

### 1. test_text_box.py
- Переход на страницу Text Box
- Заполнение полей Full Name и Current Address
- Проверка отображения введенных данных после отправки формы

### 2. test_login_form_validate.py  
- Проверка плейсхолдеров полей First Name, Last Name, Email
- Проверка атрибута pattern у поля Email
- Проверка валидации пустой формы

### 3. test_login_form.py
- Заполнение полей State и City в форме Practice Form

## Требования

- Python 3.7+
- Chrome браузер
- ChromeDriver (должен быть в PATH)

## Установка зависимостей

```bash
pip install selenium pytest

# Домашнее задание №10-11 - Автоматизация тестирования с Selenium

Этот проект содержит автоматизированные тесты для веб-сайта DemoQA, написанные на Python с использованием Selenium WebDriver.