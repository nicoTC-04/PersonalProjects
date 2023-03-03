import time
import random

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

n = 20  # aqui pongan las veces que quieren
for y in range(n):
    # Initialize the service
    s = Service(ChromeDriverManager().install())

    # Initialize the driver
    driver = webdriver.Chrome(service=s)

    # Navigate to the Google Form
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSece1tytKXq5pmHu_MTa5TsKrIx2TaJPHSXIXPYTnr_6GXeJQ/viewform?usp=sf_link")

    # Wait for the page to load
    driver.implicitly_wait(10)
    # Find and click the option
    opciones2 = [
        '//*[@id="i19"]',
        '//*[@id="i22"]',
        '//*[@id="i25"]',
        '//*[@id="i28"]',
        '//*[@id="i31"]',
        '//*[@id="i34"]',
        '//*[@id="i37"]',
    ]
    opciones = ['//*[@id="i5"]',
                '//*[@id="i8"]',
                '//*[@id="i11"]',

                '//*[@id="i44"]',
                '//*[@id="i47"]',
                '//*[@id="i50"]',
                '//*[@id="i53"]',

                '//*[@id="i60"]',
                '//*[@id="i63"]',
                '//*[@id="i66"]',
                '//*[@id="i69"]',
                '//*[@id="i72"]',

                '//*[@id="i79"]',
                '//*[@id="i82"]',

                '//*[@id="i89"]',
                '//*[@id="i92"]',
                ]

    random.shuffle(opciones)
    for x in opciones:
        option = driver.find_element(By.XPATH, x)
        option.click()
    time.sleep(1)
    random.shuffle(opciones2)

    limit = 0
    for x in opciones2:
        option = driver.find_element(By.XPATH, x)
        option.click()
        limit += 1
        if limit == 3:
            break
    time.sleep(2)

    option = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div')
    option.click()
