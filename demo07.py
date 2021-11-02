import os.path
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.maximize_window()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:////' + path + '/forms3.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element(By.ID, 'select')
        se = Select(se)
        se.select_by_value('guangzhou')
        sleep(2)
        se.select_by_visible_text('北京')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_select()