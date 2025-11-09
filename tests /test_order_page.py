import allure

from helps.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Оформление заказа из хедера')  
    @allure.description('Успешное оформление заказа при нажатии кнопки "Заказать" в хедере')  
    def test_order_scooter_by_order_button_from_header(self, driver):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        header_page.order_button_click()
        order_page.order_scooter_full_path(Users.user)
        assert order_page.check_order_title(), "Окно подтверждения заказа не появилось"  
      
    @allure.title('Оформление заказа с главной страницы')  
    @allure.description('Успешное оформление заказа при нажатии кнопки "Заказать" на главной странице')  
    def test_order_scooter_by_order_button_from_home_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page.order_scooter_full_path(Users.user_2)
        assert order_page.check_order_title(), "Окно подтверждения заказа не появилось"  

