
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_run_app(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Dilesmo', self.browser.title)

        self.fail('Test à finir!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')


