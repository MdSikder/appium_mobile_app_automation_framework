from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "com.example.yourapp:id/username")
    PASSWORD_INPUT = (By.ID, "com.example.yourapp:id/password")
    LOGIN_BUTTON = (By.ID, "com.example.yourapp:id/login")
