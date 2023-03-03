from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver = webdriver.Chrome("Browsers\chromedriver.exe")
# maximize the window size
driver.maximize_window()

driver.implicitly_wait(30)
# navigate to the url
driver.set_page_load_timeout(50)
driver.get("https://www.google.com/")
time.sleep(3)
# close the browser
driver.quit()
