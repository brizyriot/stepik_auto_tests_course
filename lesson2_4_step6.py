from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
button.click()
