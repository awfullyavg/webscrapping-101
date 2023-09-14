from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import smtpd

options = webdriver.ChromeOptions() 
options.binary_location = "/usr/bin/google-chrome" #Need to point to location of chromedriver in WSL
driver = webdriver.Chrome(options=options)
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(8)

lang_menu = driver.find_element(By.ID, "promptContentChangeLanguage")
lang_eng = lang_menu.find_element(By.ID, "langSelect-EN")
lang_eng.click()

driver.implicitly_wait(8)

for i in range(100):
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1) ]

    #Actions chains are like a queue of actions to perform
    actions = ActionChains(driver)
    actions.click(cookie)

    actions.perform() #Need perform to execute 
    
    # Print the number of cookies and other relevant information
    print(f"Cookies: {cookie_count.text}, Items: {[item.text for item in items]}")

time.sleep(5)
driver.quit()