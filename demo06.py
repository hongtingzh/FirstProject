import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        path = os.path.dirname(os.path.abspath(__file__))
        file_name = 'file:////' + path + '/forms2.html'
        self.driver.get(file_name)

    def test_checkbox(self):
        swimming = self.driver.find_element(By.NAME, 'swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        self.driver.quit()

    def test_radio(self):
        list = self.driver.find_elements(By.NAME, 'gender')
        for g in list:
            if g.get_attribute('value') == 'female':
                g.click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_radio()