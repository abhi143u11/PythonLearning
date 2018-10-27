from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# load Url of whatsapp web
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# check and wait for the file to load
try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'input-search')))
except:
    print('Login Failed')

# Creating input to ask for name,message and no of time to be sent

name = input('Name or user group:')
msg = input('your message')
count = int(input('Enter the Count:'))

actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(name)
actions.send_keys(Keys.ENTER)
actions.perform()

msg_box = driver.find_element_by_class_name('_2S1VP')
# msg += '\n this is message testing'


for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()