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


class DemoPimcoreVisit():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def hover_over_elements(self):
        try:
            actions = ActionChains(self.driver)
            driver = self.driver
            # header_class = driver.find_element(By.CLASS_NAME, "mobile-nav")
            # actions.move_to_element(header_class).click().perform()
            test = driver.find_element(By.ID, "navbar navbar-expand-md navbar-dark sticky-top py-1 site-header ")
            # print(test.get_attribute("innerHTML"))
            html_list = test.find_element(By.CLASS_NAME,"navbar-nav menu-links ml-4 m-auto")
            # print(html_list.get_attribute("innerHTML"))
            # if len(html_list.find_elements(By.CLASS_NAME,"main-navigation-items drop-down").get_attribute("innerHTML")) > 0:
            # items = html_list.find_elements(By.CLASS_NAME,"main-navigation-items drop-down")
            items = html_list.find_elements(By.TAG_NAME,"li")
            # print("items: ", items)
            for item in items:
                print(item.get_attribute("innerHTML"))
                driver.implicitly_wait(1)
                actions.move_to_element(item).perform()
            driver.implicitly_wait(1.5)
            # move_away = driver.find_element(By.CLASS_NAME, "main-nav blue-menu clearfix")
            # print(move_away)
            # actions.move_to_element(move_away).perform()
            # alert = driver.switch_to.alert
            return "Hover completed"
        except MoveTargetOutOfBoundsException as e:
            traceback.print_exc()
            error = "internal server error"
            return error
    
    def test_search_in_demo_pimcore(self):
        response = ""
        driver = self.driver
        print(driver)
        driver.get("https://demo.pimcore.com")
        print(driver.title)
        if driver.title == "Pimcore Demo":
            # response = CredencysTest.site_login(self=self)
            response = DemoPimcoreVisit.hover_over_elements(self=self)
            print("true")
        # # if response == "demo.pimcore.com :: Pimcore":
        # #     response = DemoPimcoreAdmin.hover_over_elements(self=self)
            
        # if response == "Hover completed":
        # #     response = DemoPimcoreAdmin.site_logout(self=self)
        #     print("Completed")
        
        # if response == "Logged Out":
        #     print("Completed")
        time.sleep(3)
        # driver.quit()
        return driver.title
        
"""

# if choice == "demo pimcore":
        #     demo_pimcore = DemoPimcoreVisit()
        #     print("1")
        #     print(choice + " is being tested")
        #     response = demo_pimcore.test_search_in_demo_pimcore()
        #     print(response)


"""