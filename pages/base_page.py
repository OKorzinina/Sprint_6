import allure 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получить текущий URL") # Добавлена аннотация allure.step
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание отображения элемента по локатору {locator}") # Добавлена аннотация allure.step
    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
            )

    @allure.step("Кликнуть по кнопке/элементу по локатору {locator}") # Добавлена аннотация allure.step
    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()

    @allure.step("Заполнить поле по локатору {locator} текстом: '{text}'") # Добавлена аннотация allure.step
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    @allure.step("Получить текст элемента по локатору {locator}") # Добавлена аннотация allure.step
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    @allure.step("Прокрутить страницу до элемента по локатору {locator}") # Добавлена аннотация allure.step
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключиться на новую вкладку браузера") # Добавлена аннотация allure.step
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверить отображение элемента по локатору {locator}") # Добавлена аннотация allure.step
    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()
