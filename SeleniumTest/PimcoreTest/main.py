import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from DemoPimcoreAdmin.loginDemoPimcoreAdmin import DemoPimcoreAdmin
from DemoPimcore.visit import DemoPimcoreVisit

# Call test function

class PimcoreTesting(unittest.TestCase):
    
    def choose_website(self):
        choice = "demo pimcore admin"
        print(choice)

        if choice == "demo pimcore admin":
            demo_pimcore_admin = DemoPimcoreAdmin()
            print("2")
            print(choice + " is being tested")
            response = demo_pimcore_admin.test_search_in_demo_pimcore_admin()
            print(response)

    def __init__(self):
        PimcoreTesting.choose_website(self=self)


pimcore_testing = PimcoreTesting()

if __name__ == "__main__":
    unittest.main()

