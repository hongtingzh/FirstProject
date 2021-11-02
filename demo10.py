from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:////' + path + '/test_wait.html'
        self.driver.get(file_path)

    def test_wait(self):
        # wait = WebDriverWait(self.driver, 3)
        # wait.until(EC.title_is('wait'))
        locator = self.driver.find_element(By.NAME, 't1').location
        self.driver.find_element(By.ID, 'btn').click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'id2'), 'id 2'))
        print(self.driver.find_element(By.ID, 'id2').text)
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_wait()