"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()
    
    def test_case_1(self):
        """Find fuel"""
        try:
            self.driver.get('https://am4.pagespeedster.com/am4/?gameType=app&uid=mkhairulhabibm@gmail.com&uid_token=2286f7d3391388506a46f31110fccfbe&mail=mkhairulhabibm@gmail.com&mail_token=2286f7d3391388506a46f31110fccfbe&FCM=ffYKMxxJ1Ts:APA91bGM60Vm20sJIZ9ix0qM_IY-cBkwb6753lBSXbrGiDeMpu6w8JJCHne5um82gBUgfoIXthy1JJqMblGYHp2Jw3jl2GkaA6AY9jd1tdfCJ1IZua6ukZzsJF9CkEnhfhYpVr2N2GE0#')
            el = self.driver.find_element_by_xpath("//*[@title='Fuel & co2']")
            el.click()
            el2 = self.driver.find_element_by_xpath("//span[@id='sumCost']")
            print("current fuel: " + el2.text)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
