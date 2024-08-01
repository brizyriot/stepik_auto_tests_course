from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


try:
    link = "http://suninjuly.github.io/registration2.html"
    driver.get(link)


    input_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
    input_name.send_keys("Irina")
    input_l_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
    input_l_name.send_keys("Bannikova")
    input_email = driver.find_element(By.CSS_SELECTOR, '.third_class .third')
    input_email.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # Здесь извлекается текст, содержащийся в элементе welcome_text_elt,
    # с помощью атрибута text. Полученный текст сохраняется в переменной welcome_text.
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('тест ок')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()