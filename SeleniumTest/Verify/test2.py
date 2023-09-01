import unittest
from selenium import webdriver
import time

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        time.sleep(3)
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)