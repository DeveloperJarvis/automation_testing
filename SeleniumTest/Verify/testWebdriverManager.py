import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("please pass correct browser name")

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Test@12345")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(3)
driver.quit()



