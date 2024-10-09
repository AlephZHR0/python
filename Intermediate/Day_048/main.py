from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.python.org/"
driver.get(url)

final_dict = {}
upcoming_events = driver.find_element(By.CSS_SELECTOR, "div.medium-widget.event-widget.last")
for i, upcoming_event in enumerate(upcoming_events.find_elements(By.TAG_NAME, "li")):
    date_MM_DD = upcoming_event.find_element(By.CSS_SELECTOR, "time").text
    event_name = (upcoming_event.find_element(By.CSS_SELECTOR, "a").text)
    final_dict[i] = {"time": date_MM_DD, "name": event_name}

print(final_dict)
