from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)

f_name = driver.find_element(By.CSS_SELECTOR, "input.top")
l_name = driver.find_element(By.CSS_SELECTOR, "input.middle")
email = driver.find_element(By.CSS_SELECTOR, "input.bottom")
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

f_name.send_keys("João")
l_name.send_keys("Pedro")
email.send_keys("jpjoaopedro1011@gmail.com")
submit.click()


