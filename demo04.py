from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.get('https://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element(By.ID, 't1')
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        sleep(1.5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_webelement_prop()