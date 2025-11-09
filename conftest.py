#import allure
#import pytest
#from selenium import webdriver

#from helps.data import Urls


#@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
#@pytest.fixture
#def driver():
    #driver = webdriver.Firefox()
    #driver.get(Urls.QA_SCOOTER_URL)
    #yield driver
    #driver.quit()


# Корректное отображение аргументов в параметризированном тесте
#def pytest_make_parametrize_id(val):
    #return repr(val)



import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions # Добавляем импорт Options
from webdriver_manager.firefox import GeckoDriverManager

from helps.data import Urls


@pytest.fixture(scope='function')
def driver():
    # 1. Загружаем geckodriver
    geckodriver_path = GeckoDriverManager().install()
    service = FirefoxService(executable_path=geckodriver_path)

    # 2. Создаем объект FirefoxOptions
    firefox_options = FirefoxOptions()

    # 3. Явно указываем путь к исполняемому файлу Firefox
    # ЗАМЕНИТЕ ЭТОТ ПУТЬ НА РЕАЛЬНЫЙ ПУТЬ НА ВАШЕЙ СИСТЕМЕ!
    firefox_binary_location = r"C:\Users\Olga\AppData\Local\Mozilla Firefox\firefox.exe" # Пример для Windows
   
    firefox_options.binary_location = firefox_binary_location

    # 4. Инициализируем драйвер, передавая service и options
    driver = webdriver.Firefox(service=service, options=firefox_options)

    driver.set_window_size(1920, 1080)

    with allure.step('Переход на страницу сервиса'):
        driver.get(Urls.QA_SCOOTER_URL)

    yield driver

    with allure.step('Закрытие браузера'):
        driver.quit()


def pytest_make_parametrize_id(val):
    if isinstance(val, tuple) and len(val) == 3:
        if 'accordion__heading' in val[0][1]:
            return f"Question {val[0][1].split('-')[-1]}"
        return repr(val)
    return repr(val)
