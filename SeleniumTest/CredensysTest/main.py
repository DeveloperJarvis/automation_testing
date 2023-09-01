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

class CredencysTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def hover_over_elements(self):
        try:
            actions = ActionChains(self.driver)
            driver = self.driver

            test = driver.find_element(By.ID, "site-navigation")

            html_list = test.find_element(By.CLASS_NAME,"main-navigation-items-list")
            # print(html_list.get_attribute("innerHTML"))
            
            items = html_list.find_elements(By.TAG_NAME,"li")
            
            for item in items:
                print(item.get_attribute("innerHTML"))
                driver.implicitly_wait(1)
                actions.move_to_element(item).perform()
                driver.implicitly_wait(4)
            driver.implicitly_wait(1.5)
            print(len(items))
            return "Hover completed"
        except MoveTargetOutOfBoundsException as e:
            traceback.print_exc()
            error = "internal server error"
            return error

    def test_search_in_demo_pimcore_admin(self):
        response = ""
        driver = self.driver
        print(driver)
        driver.get("https://www.credencys.com/")
        print(driver.title)
        if driver.title == "Enterprise PIM & MDM Implementation Company - Credencys":
            response = CredencysTest.hover_over_elements(self=self)
            
        if response == "Hover completed":
            print("Completed")
        
        time.sleep(3)
        title = driver.title
        CredencysTest.tearDown(self=self)
        return title
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()