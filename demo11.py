from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome('.\drivers\chromedriver.exe')
        self.driver.maximize_window()

    def test_Action_chains(self):
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        sleep(2)
        action = ActionChains(self.driver)
        doubleclick = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        contextclick = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        action.double_click(doubleclick).perform()
        sleep(2)
        self.driver.find_element(By.NAME, 't1').click()
        sleep(2)
        action.context_click(contextclick).perform()
        sleep(2)
        self.driver.quit()

    def test_keys(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)
        kw = self.driver.find_element(By.ID, 'kw')
        kw.send_keys('selenium')
        kw.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        kw.send_keys(Keys.CONTROL, 'x')
        sleep(1)
        kw.send_keys(Keys.CONTROL, 'v')
        sleep(2)
        self.driver.quit()

    def test_move_to_element(self):
        self.driver.get('https://www.baidu.com')
        sleep(2)
        action = ActionChains(self.driver)
        news = self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]')
        sleep(1)
        action.move_to_element(news).perform()
        sleep(2)
        self.driver.quit()




if __name__ == '__main__':
    case = TestCase()
    # case.test_Action_chains()
    # case.test_keys()
    case.test_move_to_element()