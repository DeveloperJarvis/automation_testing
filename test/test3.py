#automation testing selenium python code conditions for web application
#Author: Firstname Lastname
#date: 20/08/2022
#version: 1.0
#python version: 3.10
#language: python3.10

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

time.sleep(2)
driver.find_element(By.NAME, "q").send_keys("selenium")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

time.sleep(2)
driver.close()


