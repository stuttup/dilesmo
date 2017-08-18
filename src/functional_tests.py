
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
        self.browser.get('http://localhost:8000/query')
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
        time.sleep(1)

        # when he hits enter the page updates and he is shown images about football
        images_block = self.browser.find_element_by_id('images')
        images = images_block.find_elements_by_tag_name('img')

        self.assertTrue(
            any(image.get_attribute('title') == 'football' for image in images),
            f"New image with title 'football' did not appear. \
            The titles were:\n{image.get_attribute('title') for image in images}"
        )

        # There is still a text box inviting him to make another research


        self.fail('Test à finir!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')


