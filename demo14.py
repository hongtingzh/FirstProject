from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://sahitest.com/demo/framesTest.htm')
        sleep(1)

    def test1(self):
        top = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(2)

        self.driver.switch_to.default_content()
        second = self.driver.find_element(By.XPATH, '/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(2)

        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test1()