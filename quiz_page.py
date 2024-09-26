from selenium.webdriver.common.by import By

class QuizPage:
    def __init__(self, driver):
        self.driver = driver

    def write(self, by, value, text: str):
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def tap(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()

    # 로고 버튼
    logo_image = "/html/body/section/div/div/a/img"
    # 헤더 버튼
    header_c = "/html/body/section/div/nav/div/div/ul/li[1]"
    header_java = "/html/body/section/div/nav/div/div/ul/li[2]"
    header_py = "/html/body/section/div/nav/div/div/ul/li[3]"
    # 북마크 버튼
    bookmark_button = "/html/body/section/main/div/div[1]/div/div[1]/div[1]"
    # 답 보기 버튼 / 솔루션 함수 저장 요소
    answer_button = "/html/body/section/main/div/div[2]/div[2]"
    # 메모 input
    memo_input = "/html/body/section/main/div/div[2]/textarea"
    # 댓글 input
    comment_input = "/html/body/section/main/div/div[2]/div[5]/textarea"
    name_input = "/html/body/section/main/div/div[2]/div[5]/div/input[1]"
    password_input = "/html/body/section/main/div/div[2]/div[5]/div/input[2]"
    write_button = "/html/body/section/main/div/div[2]/div[5]/div/button"

    def input_name(self, name: str):
        self.write(By.XPATH, self.name_input, name)

    def input_password(self, password: str):
        self.write(By.XPATH, self.password_input, password)

    def input_comment(self, comment: str):
        self.write(By.XPATH, self.comment_input, comment)

    def tap_comment_button(self):
        self.tap(By.XPATH, self.write_button)

    def tap_header_c(self):
        self.tap(By.XPATH, self.header_c)

    def tap_header_java(self):
        self.tap(By.XPATH, self.header_java)

    def tap_header_py(self):
        self.tap(By.XPATH, self.header_py)