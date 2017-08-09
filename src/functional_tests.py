
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_run_app(self):
        # A user hears about Dilesmo and goes to
        # checkout their home page
        self.browser.get('http://localhost:8000')
        self.assertIn('Dilesmo', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Dilesmo', header_text)
        # He is invited to enter a query in the search box
        inputbox = self.browser.find_element_by_id('query')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Que recherchez vous ? Dites-moi tout'
        )

        # He types football in the text box
        inputbox.send_keys('football')

        # when he hits enter the page updates and he is shown images about football
        main_image = self.browser.find_element_by_id('main_image')
        images = self.mai,main_image.find_element_by_tag_name('<img>')
        self.assertTrue(
            any(image.title == 'footbal' for image in images)
        )

        # There is still a text box inviting him to make another research


        self.fail('Test à finir!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')


