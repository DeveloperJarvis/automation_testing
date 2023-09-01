#automation testing using selenium for web application
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

time.sleep(5)
driver.close()

