import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class InternetSpeed():
    def get_internet_speed(self):
        driver = webdriver.Chrome()
        driver.get("https://www.speedtest.net/pt")
        driver.find_element(By.CSS_SELECTOR, ".start-text").click()
        driver.wait = WebDriverWait(driver, 60)
        driver.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.result-item.result-item-inline.result-item-align-center.result-item-id a"), "1"))
        self.run_id = driver.find_element(By.CSS_SELECTOR, "div.result-item.result-item-inline.result-item-align-center.result-item-id a").text
        self.download = float(driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed").text)
        self.upload = float(driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed").text)
        driver.quit()

    def __str__(self):
        return f"Download: {self.download} Mbps\nUpload: {self.upload} Mbps\nRun ID: {self.run_id}"

    def __repr__(self):
        return f"Download: {self.download} Mbps\nUpload: {self.upload} Mbps\nRun ID: {self.run_id}"

internet_speed = InternetSpeed()
internet_speed.get_internet_speed()

print(internet_speed)
