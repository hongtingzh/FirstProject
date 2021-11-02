from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

def test01():
    driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
    driver.get('https://www.baidu.com')
    print("123")


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')

    def test01(self):
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test01()
