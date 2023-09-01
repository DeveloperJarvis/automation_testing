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

    __items = []
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def hover_over_elements(self):
        try:
            menu_list = []
            title = ""
            actions = ActionChains(self.driver)
            driver = self.driver

            test = driver.find_element(By.ID, "site-navigation")

            html_list = test.find_element(By.CLASS_NAME,"main-navigation-items-list")            
            self.__items = html_list.find_elements(By.TAG_NAME,"li")
            items = html_list.find_elements(By.TAG_NAME,"li")

            for i in range(len(self.__items)):
                # print("self.__items: ", self.__items[i].get_attribute("innerHTML"))
                # print(i)
                menu_list.append(self.__items[i].get_attribute("innerHTML"))
            length = len(self.__items)
            for i in range(length):
                # print(i)
                # print("yes")
                # print("self.__items: ", menu_list[i])
                # print("no")
                title = driver.title
                if "javascript:void" in menu_list[i]:
                    continue
                for item in items:
                    actions.move_to_element(item).perform()
                    # print("item: ", item.get_attribute("innerHTML"))
                    # print("Condition: ", item.get_attribute("innerHTML") == menu_list[i])
                    if item.get_attribute("innerHTML") == menu_list[i]:
                        actions.move_to_element(item).click().perform()
                        print(driver.title)
                        driver.implicitly_wait(4)
                        if not title == driver.title:
                            actions = ActionChains(self.driver)
                            driver = self.driver
                            test = driver.find_element(By.ID, "site-navigation")
                            html_list = test.find_element(By.CLASS_NAME,"main-navigation-items-list")
                            items = html_list.find_elements(By.TAG_NAME,"li")
                        print("================================  break ran")
                        break
                                
            return "Hover completed"
        except MoveTargetOutOfBoundsException as e:
            traceback.print_exc()
            error = "internal server error"
            return error
        except Exception as e:
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