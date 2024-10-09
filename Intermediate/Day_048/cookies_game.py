from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

driver = webdriver.Chrome()

url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

driver.find_element(By.ID, "langSelect-PT-BR").click()

skills:dict = {}
for i, skill in enumerate(driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")):
    cost = int(skill.text.split("\n")[1].replace(",", ""))
    element = skill
    skills[i] = {"cost": cost, "element": element}


old_time = datetime.now()
while True:
    cookie_count = int(driver.find_element(By.ID, "cookies").text.replace(",", "").split(" ")[0])
    if old_time + timedelta(seconds=5) < datetime.now():
        old_time = datetime.now()
        for i, skill in enumerate(driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")):
            cost = int(skill.text.split("\n")[1].replace(",", ""))
            element = skill
            skills[i] = {"cost": cost, "element": element}
            i=0
        abilities_list = list(skills.values())
        abilities_list.sort(key=lambda x: x["cost"], reverse=True)
        for single_skill in abilities_list:
            if single_skill["cost"] <= cookie_count:
                single_skill["element"].click()
                break
    driver.find_element(By.ID, "bigCookie").click()
