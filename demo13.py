import os.path

from selenium import webdriver
from time import sleep, strftime, localtime, time

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        sleep(1)

    def filePath(self):
        path = os.path.abspath('screenShot')
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_path = path + '/' + st + '.png'
        print(file_path)

        return file_path

    def test_getscreenshot(self):
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = st + '.png'

        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        file_path = self.filePath()
        self.driver.get_screenshot_as_file(file_path)
        self.driver.fullscreen_window()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_getscreenshot()
    case.test_getscreenshot()