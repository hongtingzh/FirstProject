import os.path

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = path + '/forms.html'
        print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys('hongting')
        pwd = self.driver.find_element(By.ID, 'pwd')
        pwd.send_keys('hongting123')
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        self.driver.find_element(By.ID, 'submit').click()
        ttt = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        sleep(2)
        username.clear()
        pwd.clear()
        print(ttt)
        sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    case.test_login()