from selenium.webdriver.common.by import By


class HomePageHeaderLocators:
    """Верхняя часть главной страницы"""
    logo_yandex = (By.XPATH, ".//a[contains(@class, 'LogoYandex')]")  
    logo_scooter = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")  
    order_button = (By.XPATH, "//div[@class='Header_Buttons__1FXDj']/button[text()='Заказать']")  
    order_status_button = (By.XPATH, ".//button[contains(text(), 'Статус заказа')]")  
    track_field = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")  
    view_button = (By.XPATH, ".//button[text()='Посмотреть']")  
    header_page_title = (By.XPATH, ".//div[contains(text(), 'Учебный тренажер')]") 


class HomePageLocators:
    """Элементы главной страницы"""
    home_page_title = (By.XPATH, ".//div[contains(@class, 'Header__iJKdX')]")  
    order_button = (By.XPATH, "//div[@class='Home_Buttons__1JtPq']/button[text()='Заказать']") 
    accept_cookies_button = (By.ID, "rcc-confirm-button")
    questions_title = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")  

    # Локаторы кнопок вопросов
    questions = [
        (By.XPATH, "//div[@id='accordion__heading-{}']".format(i)) for i in range(8)
    ]

    # Локаторы текста ответов
    questions_text = [
        (By.XPATH, "//div[@id='accordion__panel-{}']".format(i)) for i in range(8)
    ]

