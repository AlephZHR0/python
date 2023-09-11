from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from auth import *

WHAT_TO_SEARCH = input("What to search in payment method: ").lower().strip()


def input_the_code(method: str, code: str):
    driver.find_element(By.ID, f"PHONE_{method}_OTP-0").send_keys(code[0])
    driver.find_element(By.ID, f"PHONE_{method}_OTP-1").send_keys(code[1])
    driver.find_element(By.ID, f"PHONE_{method}_OTP-2").send_keys(code[2])
    driver.find_element(By.ID, f"PHONE_{method}_OTP-3").send_keys(code[3])


options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get("https://auth.uber.com/v2/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PHONE_NUMBER_or_EMAIL_ADDRESS"))).send_keys(MAIL_ADRESS, Keys.ENTER)

code = input("""If your account doesn't have OAuth, type "." Code: """)
if code != ".":
    sms = driver.find_elements(By.ID, "PHONE_SMS_OTP-0")
    voice = driver.find_elements(By.ID, "PHONE_VOICE_OTP-0")
    while sms == [] and voice == []:
        sleep(0.5)
        sms = driver.find_elements(By.ID, "PHONE_SMS_OTP-0")
        voice = driver.find_elements(By.ID, "PHONE_VOICE_OTP-0")
    if sms != []:
        input_the_code("SMS", code)
    elif voice != []:
        input_the_code("VOICE", code)
    else:
        input("Try again.")
        driver.quit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PASSWORD"))).send_keys(PASSWORD, Keys.ENTER)
WebDriverWait(driver, 10).until(EC.url_contains("https://m.uber.com/go/pickup?effect="))

driver.get("https://riders.uber.com/trips")


all_trips_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_css-fISjCi")))
current_month_button = driver.find_element(By.CLASS_NAME, "_css-kmFJRi")
previous_month_button = driver.find_element(By.CLASS_NAME, "_css-hBHgGw")
print(f"1. {all_trips_button.text}")
print(f"2. {current_month_button.text}")
print(f"3. {previous_month_button.text}")
month_of_choice = input("Your choice: ")

match month_of_choice:
    case "1":
        all_trips_button.click()
    case "2":
        current_month_button.click()
    case "3":
        previous_month_button.click()
    case _:
        input("""Invalid option, to do for all trips press enter, to close, type ".".""")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_css-bucRsj")))
number_of_pages = int(driver.find_element(By.CLASS_NAME, "_css-bucRsj").text[3:])

trips_links = []


def get_page_trips(direction: int) -> list:
    global trips_links
    page_trips = driver.find_elements(By.CLASS_NAME, "_css-hBHgGw")
    j = 0
    while page_trips == []:
        sleep(0.5)
        page_trips = driver.find_elements(By.CLASS_NAME, "_css-hBHgGw")
        j+=0.5
        if j % 5 == 0:
            driver.refresh()
        if j == 20:
            print("TimeoutException")
            driver.quit()

    for trip in page_trips:
        if trip.get_attribute("href") not in trips_links and trip.text.lower() == "mais informações":
            trips_links.append(trip.get_attribute("href"))
            
    if i != number_of_pages - 1:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "_css-fzayjn")))
        driver.find_elements(By.CLASS_NAME, "_css-fzayjn")[direction].click()
    

def check_and_handle_too_many_requests(driver):
    page_content = driver.find_elements(By.XPATH, "/html/body/pre")
    if len(page_content) != 0:
        while len(page_content) != 0:
            driver.refresh()
            sleep(1)
            page_content = driver.find_elements(By.XPATH, "/html/body/pre")


for i in range(number_of_pages):
    print(f"Page {i + 1} of {number_of_pages}")
    get_page_trips(-1)
    check_and_handle_too_many_requests(driver)
print("Verifying trips...")
for i in range(number_of_pages):
    print(f"Page {i + 1} of {number_of_pages}")
    get_page_trips(0)
    check_and_handle_too_many_requests(driver)

print(f"There are {len(trips_links)} trips")

i = 0
j = 0
for link in trips_links:
    i += 1
    print(f"Trip number {i} of {len(trips_links)}, saved {j} trips")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)

    check_and_handle_too_many_requests(driver)
    
    canceled = driver.find_elements(By.CLASS_NAME, "_css-krCBTw")
    not_canceled = driver.find_elements(By.CLASS_NAME, "_css-dTqljZ")
    k = 0
    while canceled == [] and not_canceled == []:
        sleep(0.5)
        canceled = driver.find_elements(By.CLASS_NAME, "_css-krCBTw")
        not_canceled = driver.find_elements(By.CLASS_NAME, "_css-dTqljZ")
        k+=0.5
        if k % 5 == 0:
            driver.refresh()
        if k == 20:
            print("try again later")
            driver.quit()

    if not_canceled:
        drive_elements = driver.find_elements(By.CLASS_NAME, "_css-dTqljZ")
        while drive_elements == []:
            drive_elements = driver.find_elements(By.CLASS_NAME, "_css-dTqljZ")
        card_used = drive_elements[-1].text
        if WHAT_TO_SEARCH in card_used.lower():
            see_receipt = driver.find_elements(By.CLASS_NAME, "_css-hBHgGw")
            while see_receipt == []:
                see_receipt = driver.find_elements(By.CLASS_NAME, "_css-hBHgGw")
            see_receipt[0].click()
            download_pdf = driver.find_elements(By.CLASS_NAME, "_css-iuijBg")
            while download_pdf == []:
                download_pdf = driver.find_elements(By.CLASS_NAME, "_css-iuijBg")
            download_pdf[1].click()
            j += 1
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
        driver.execute_script("window.close('');")
        driver.switch_to.window(driver.window_handles[0])
    elif canceled:
        driver.execute_script("window.close('');")
        driver.switch_to.window(driver.window_handles[0])
    else:
        print("Something went wrong")
        driver.quit()

driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.close('');")
print(f"Saved {j} trips of {len(trips_links)}")
input("Pressione enter para sair.")
driver.quit()
