from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_profile_path = "user-data-dir=C:\\Users\\M.A COM\\AppData\\Local\\Google\\Chrome\\User Data\\WatsappAutomation"
options = webdriver.ChromeOptions()
options.add_argument(chrome_profile_path)
browser=webdriver.Chrome(options=options)
currTime = time.strftime("    %d-%b-%Y   %H:%M:%S")

with open('contacts.txt', 'r', encoding='utf-8') as file:
    contacts = [contact.strip() for contact in file.readlines()]
with open('message.txt', 'r', encoding='utf-8') as file:
        message = file.read()
        # + str(currTime)

def send_message(contact, message):
    try:
        search_box_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        search_box = wait.until(EC.presence_of_element_located((By.XPATH,search_box_path)))
        search_box.send_keys(contact,Keys.ENTER)
        time.sleep(1)
        message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
        message_box.send_keys(message , Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error sending message to {contact}: {e}")
        browser.quit()
        return
        
def check_for_messages():
    try:
        unread_button_path = '//*[@id="side"]/div[2]/button[2]'
        unread_button = wait.until(EC.presence_of_element_located((By.XPATH, unread_button_path)))
        unread_button.click()
        time.sleep(1)
        unread_messages_path = '//*[@id="pane-side"]/div[1]/div/div/div[1]'
        unread_messages = wait.until(EC.presence_of_all_elements_located((By.XPATH, unread_messages_path)))
        for message in unread_messages:
            message.click()
            message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
            message_box.send_keys(message , Keys.ENTER)
            message_text = message.text
            print(f"Unread message: {message_text}")
        time.sleep(1)
    except:
        print("No new messages")
    
while(True):
    print("Starting Automation...")
    browser.get("https://web.whatsapp.com/")
    wait = WebDriverWait(browser,300)
    # # contact = contacts[0]
    # check_for_messages()
    for contact in contacts:
            send_message(contact, message)
    time.sleep(600)
    # # browser.quit
    # # print(f"Message sent successfully to {contact}")
