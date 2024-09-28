from selenium.webdriver.common.by import By
from quiz_page import QuizPage

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def tap(self, by, value):
        element = self.driver.find_element(by, value)
        assert element, f"존재하지 않는 element: {value}"
        element.click()

    # 로고 버튼
    logo_image = "/html/body/main/a/img"
    # C 버튼
    c_button = "/html/body/main/div[2]/div[1]/a/div"
    c_bookmark_close = "/html/body/main/div[2]/div[1]/div"
    c_bookmark_open = "/html/body/main/div[2]/div[1]/a[2]/div"
    # Java 버튼
    java_button = "/html/body/main/div[2]/div[2]/a/div"
    java_bookmark_close = "/html/body/main/div[2]/div[2]/div"
    java_bookmark_open = "/html/body/main/div[2]/div[2]/a[2]/div"
    # Python 버튼
    py_button = "/html/body/main/div[2]/div[3]/a/div"
    py_bookmark_close = "/html/body/main/div[2]/div[3]/div"
    py_bookmark_open = "/html/body/main/div[2]/div[3]/a[2]/div"

    def tap_logo_button(self):
        self.tap(By.XPATH, self.logo_image)

    def tap_c_button(self):
        self.tap(By.XPATH, self.c_button)
        return QuizPage(self.driver)

    def tap_java_button(self):
        self.tap(By.XPATH, self.java_button)
        return QuizPage(self.driver)

    def tap_py_button(self):
        self.tap(By.XPATH, self.py_button)
        return QuizPage(self.driver)
