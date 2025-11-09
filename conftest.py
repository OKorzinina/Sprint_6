import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
from webdriver_manager.firefox import GeckoDriverManager

from helps.data import Urls


@pytest.fixture(scope='function')
def driver():
    geckodriver_path = GeckoDriverManager().install()
    service = FirefoxService(executable_path=geckodriver_path)

    firefox_options = FirefoxOptions()
    firefox_binary_location = r"C:\Users\Olga\AppData\Local\Mozilla Firefox\firefox.exe" 
    firefox_options.binary_location = firefox_binary_location
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
