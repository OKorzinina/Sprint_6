import time
import allure
import pytest

from helps.data import Questions, Urls
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage, HomePageHeader
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Проверка перехода по логотипу "Самокат"')  
    @allure.description('Клик на логотип "Самокат" возвращает на главную страницу')  
    def test_scooter_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        header_page.order_button_click()
        header_page.scooter_logo_click()
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()
        assert current_url == Urls.QA_SCOOTER_URL, "URL не соответствует ожидаемому"  
        assert title_is_displayed, "Заголовок не отображается"  

    @allure.title('Проверка перехода на Яндекс.Дзен')  
    @allure.description('Клик на логотип "Яндекс" открывает Яндекс.Дзен в новой вкладке')  
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        header_page.yandex_logo_click()
        header_page.go_to_new_tab()
        time.sleep(3)  
        current_url = header_page.get_current_url()
        assert current_url == Urls.DZEN_URL, "URL Дзена не соответствует ожидаемому"  
        assert dzen_page.check_element_main_button(), "Элемент на странице Дзен не найден"  

    @allure.title('Проверка ответов на вопросы')  
    @allure.description('Проверка соответствия текста ответов при нажатии на вопросы')  
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text',
                             zip(HomePageLocators.questions, HomePageLocators.questions_text,
                                 Questions.expected_question_text))
    def test_accordion(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePage(driver)
        text = home_page.get_text_question(question_locator, question_text_locator)

        assert text == expected_question_text, "Текст ответа не соответствует ожидаемому"  
