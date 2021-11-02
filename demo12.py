from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        sleep(2)

    def test1(self):
        self.driver.execute_script('alert("This is alert")')
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.quit()

    def test2(self):
        js = 'return document.title'
        print(self.driver.execute_script(js))

        self.driver.quit()

    def test3(self):
        js = 'var q = document.getElementById("kw");q.style.border="20px solid black";'
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element(By.ID, 'kw').send_keys('python')
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)

if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    # case.test3()
    case.test4()