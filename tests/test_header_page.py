import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helps.data import Questions, Urls
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage, HomePageHeader
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Проверка перехода по логотипу "Самокат"')
    @allure.description('Клик на логотип "Самокат" возвращает на главную страницу')
    def test_scooter_logo_click(self, driver):
        header_page = HomePageHeader(driver)

        with allure.step("Перейти на страницу заказа, чтобы проверить возврат на главную"):
            header_page.order_button_click()

        with allure.step("Кликнуть по логотипу 'Самокат'"):
            header_page.scooter_logo_click()

        with allure.step(f"Ожидание, что текущий URL станет {Urls.QA_SCOOTER_URL}"):
            WebDriverWait(driver, 10).until(EC.url_to_be(Urls.QA_SCOOTER_URL))

        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()

        with allure.step(f"Проверить, что текущий URL соответствует ожидаемому: {Urls.QA_SCOOTER_URL}"):
            assert current_url == Urls.QA_SCOOTER_URL, "URL не соответствует ожидаемому"

        with allure.step("Проверить, что заголовок главной страницы отображается"):
            assert title_is_displayed, "Заголовок не отображается"

    @allure.title('Проверка перехода на Яндекс.Дзен')
    @allure.description('Клик на логотип "Яндекс" открывает Яндекс.Дзен в новой вкладке')
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)

        with allure.step("Кликнуть по логотипу 'Яндекс'"):
            header_page.yandex_logo_click()

        with allure.step("Переключиться на новую вкладку"):
            header_page.go_to_new_tab()

       
        with allure.step(f"Ожидание, что текущий URL станет {Urls.DZEN_URL}"):
            WebDriverWait(driver, 10).until(EC.url_to_be(Urls.DZEN_URL))

        current_url = header_page.get_current_url()

        with allure.step(f"Проверить, что текущий URL соответствует ожидаемому URL Яндекс.Дзена: {Urls.DZEN_URL}"):
            assert current_url == Urls.DZEN_URL, "URL Дзена не соответствует ожидаемому"

        with allure.step("Проверить наличие основного элемента на странице Яндекс.Дзен"):
            assert dzen_page.check_element_main_button(), "Элемент на странице Дзен не найден"

    @allure.title('Проверка ответов на вопросы')
    @allure.description('Проверка соответствия текста ответов при нажатии на вопросы')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text',
                             zip(HomePageLocators.questions, HomePageLocators.questions_text,
                                 Questions.expected_question_text))
    def test_accordion(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePage(driver)

        with allure.step(f"Получить текст ответа для вопроса по локатору: {question_locator}"):
            text = home_page.get_text_question(question_locator, question_text_locator)

        with allure.step(f"Сравнить полученный текст ('{text}') с ожидаемым ('{expected_question_text}')"):
            assert text == expected_question_text, "Текст ответа не соответствует ожидаемому"

