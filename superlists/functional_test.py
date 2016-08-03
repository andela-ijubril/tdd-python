from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new to-do app she goes to check
        # out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-DO', self.browser.title)
        self.fail('Finish the test!')

    # She is invited to enter  to-do item straight away

    # she types 'Buy peacock feathers' into a text box (Edith's hobby
    # is tying fly-fishing lures)

     # When she hits enter, the page updates and the page lists
     # "1: Buy peacokc feathers" as an item in a to-do list

     # There is still a text box inviting her to add another item, She
     # enters "Use peacock to make a fly" (Edith is very methodical)

     # The page updates again, and now shows both items on her list

     # Edith wonders whethe the site will remember her list. The n she sees
     # that the site has generated a uniwue URL for her -- there is some
     # explanatory text to that effect.

     # She visits that URL her to-do list is still there

     # Satisified she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
