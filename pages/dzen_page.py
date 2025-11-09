from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DzenPage(BasePage):

    @allure.step('Проверка отображения кнопки "Главная" на странице DZEN')
    def check_element_main_button(self):
        return self.check_element(DzenPageLocators.main_button_dzen)

