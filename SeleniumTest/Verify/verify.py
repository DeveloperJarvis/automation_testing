from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
elem = driver.find_element(By.NAME, "q")
elem.send_keys('credencys' + Keys.RETURN)
# optionsList = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li span")
# # optionsList = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e")
# print(optionsList)
# print(len(optionsList))
#
# content = driver.find_elements_by_css_selector('p.content')
# print(content)
#
# for ele in optionsList:
#     print(ele.text)

time.sleep(5)
driver.quit()

