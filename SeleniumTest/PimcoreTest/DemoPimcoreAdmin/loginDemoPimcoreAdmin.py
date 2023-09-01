import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

# handling MoveTargetOutOfBoundsException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import traceback

class DemoPimcoreAdmin():

    __username = "superuser"
    __password = "enterprisedemo"
    
    def __init__(self):
        self.driver = webdriver.Firefox()

    def site_login(self):
        
        driver = self.driver
        print("in works")
        driver.find_element(By.NAME, "username").send_keys(self.__username)
        driver.find_element(By.NAME, "password").send_keys(self.__password)
        driver.find_element(By.CSS_SELECTOR, "button").click()
        
        return driver.title            

    def hover_over_elements(self):
        try:
            actions = ActionChains(self.driver)
            driver = self.driver
            html_list = driver.find_element(By.ID,"pimcore_navigation_ul")
            items = html_list.find_elements(By.TAG_NAME,"li")
            for item in items:
                print(item.get_attribute("innerHTML"))
                driver.implicitly_wait(3)
                actions.move_to_element(item).click().perform()
            return "Hover completed"
        except MoveTargetOutOfBoundsException as e:
            traceback.print_exc()
            error = "internal server error"
            return error

    def site_logout(self):
        try:
            actions = ActionChains(self.driver)
            driver = self.driver
            logout_element = driver.find_element(By.ID,"pimcore_logout")
            actions.move_to_element(logout_element).click()
            driver.implicitly_wait(1)
            return "Logged Out"
        except MoveTargetOutOfBoundsException as e:
            traceback.print_exc()
            error = "internal server error"
            return error

    def test_search_in_demo_pimcore_admin(self):
        response = ""
        driver = self.driver
        
        driver.get("https://demo.pimcore.com/admin")
        print(driver.title)

        if driver.title == "Welcome to Pimcore!":
            response = DemoPimcoreAdmin.site_login(self=self)
            
        if response == "demo.pimcore.com :: Pimcore":
            response = DemoPimcoreAdmin.hover_over_elements(self=self)

        if response:
            response = DemoPimcoreAdmin.site_logout(self=self)
        
        if response == "Logged Out":
            time.sleep(3)
            title = driver.title
            r = DemoPimcoreAdmin.tearDown(self=self)
            print("Completed")
        return title
    
    def tearDown(self):
        self.driver.quit()
        return "done"
