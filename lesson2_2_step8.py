from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")
    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Petrov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("qasw@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла