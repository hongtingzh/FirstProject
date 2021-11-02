import os.path

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:////' + path + '/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        print(self.driver.switch_to.alert.text)
        sleep(1)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.quit()

    def test_conform(self):
        self.driver.find_element(By.ID, 'confirm').click()
        print(self.driver.switch_to.alert.text)
        sleep(1)
        # self.driver.switch_to.alert.accept()
        self.driver.switch_to.alert.dismiss()
        sleep(2)
        self.driver.quit()

    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        prompt = self.driver.switch_to.alert
        prompt.send_keys('221')
        sleep(3)
        prompt.accept()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_conform()
    case.test_prompt()