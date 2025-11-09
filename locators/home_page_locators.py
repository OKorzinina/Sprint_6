from selenium.webdriver.common.by import By


class HomePageHeaderLocators:
    """Верхняя часть главной страницы"""
    logo_yandex = (By.XPATH, ".//a[contains(@class, 'LogoYandex')]")  # Изменено: contains для гибкости
    logo_scooter = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")  # Изменено: contains для гибкости
    order_button = (By.XPATH, "//div[@class='Header_Buttons__1FXDj']/button[text()='Заказать']")  # Уточнено: поиск кнопки "Заказать" внутри div
    order_status_button = (By.XPATH, ".//button[contains(text(), 'Статус заказа')]")  # Изменено: contains для большей устойчивости
    track_field = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")  # Более семантичный локатор
    view_button = (By.XPATH, ".//button[text()='Посмотреть']")  # Более семантичный локатор
    header_page_title = (By.XPATH, ".//div[contains(text(), 'Учебный тренажер')]")  # Изменено: contains для устойчивости


class HomePageLocators:
    """Элементы главной страницы"""
    home_page_title = (By.XPATH, ".//div[contains(@class, 'Header__iJKdX')]")  # Изменено: contains для гибкости
    order_button = (By.XPATH, "//div[@class='Home_Buttons__1JtPq']/button[text()='Заказать']")  # Уточнено: поиск кнопки "Заказать" внутри div
    accept_cookies_button = (By.ID, "rcc-confirm-button")
    questions_title = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")  # Изменено: contains для устойчивости

    # Локаторы кнопок вопросов
    questions = [
        (By.XPATH, "//div[@id='accordion__heading-{}']".format(i)) for i in range(8)
    ]

    # Локаторы текста ответов
    questions_text = [
        (By.XPATH, "//div[@id='accordion__panel-{}']".format(i)) for i in range(8)
    ]

