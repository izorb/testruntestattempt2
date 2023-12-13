# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #для "безголового" режима
import pytest


# Фикстура (fixture) для инициализации браузера перед каждым тестом
@pytest.fixture()
def browser():
    # Создание объекта опций для настройки браузера
    options = Options()
    # Добавление аргумента для запуска браузера в "безголовом" (headless) режиме
    options.add_argument('--headless')
    # Инициализация объекта браузера (в данном случае, Chrome) с применением опций
    chrome_browser = webdriver.Chrome(options=options)
    # Возвращение объекта браузера для использования в тестах
    return chrome_browser

# Тест проверки наличия кнопки на странице
def test_button_exist(browser):
    # Открытие URL в браузере
    browser.get('https://www.qa-practice.com/elements/button/simple')
    # Проверка наличия элемента кнопки с использованием селектора By.ID
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

# Второй тест проверки наличия кнопки на другой странице
def test_button_exist_2(browser):
    # Открытие другого URL в браузере
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    # Проверка наличия элемента кнопки с использованием селектора By.PARTIAL_LINK_TEXT
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()


def test_me():

    assert 1 == 1

