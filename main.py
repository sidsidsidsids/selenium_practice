from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from main_page import MainPage
import time

# Initialize Chrome WebDriver correctly using the Service object
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Open site
    driver.get("https://jungcheogico-omega.vercel.app")

    # Wait for the page to load
    time.sleep(1)

    # Test in main page
    main_page = MainPage(driver)

    # Tap button and check it moves to quiz page
    quiz_page = main_page.tap_c_button()

    # Delay for quiz loading
    time.sleep(6)

    # Tap header to switch quiz c to java + delay for quiz loading
    quiz_page.tap_header_java()
    time.sleep(2)

    # Tap header to switch quiz java to python + delay for quiz loading
    quiz_page.tap_header_py()
    time.sleep(2)

    # Tap header to switch quiz python to c + delay for quiz loading
    quiz_page.tap_header_c()
    time.sleep(2)

    # Set Comment
    quiz_page.input_comment("댓글이 정상적으로 작성되는 지 테스트")
    quiz_page.input_name("테스트중인 셀레니움")
    quiz_page.input_password("test1234")

    # Write Comment
    quiz_page.tap_comment_button()

    # Delay for check comment
    time.sleep(6)

    # Close the browser
    driver.quit()
except Exception as e:
    print(' Failed to compile, exception is %s' % repr(e))
