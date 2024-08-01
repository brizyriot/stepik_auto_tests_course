from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/registration1.html"

try:
    # Настройки браузера
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(link)

    # Заполнение формы
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("email@example.com")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    input4.send_keys("89953477272")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
    input5.send_keys("Smolensk")

    # Поиск кнопки с текстом 'Submit' и клик по ней
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # Ожидание перед закрытием браузера
    time.sleep(10)
    browser.quit()