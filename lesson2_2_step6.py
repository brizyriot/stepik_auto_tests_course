from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(z):
        return str(math.log(abs(12 * math.sin(int(z)))))

    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла






