from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.get('https:www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        self.driver.find_element(By.ID, 'kw').send_keys('find_Element_by_id')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)
        # self.driver.quit()

    def test_name(self):
        self.driver.find_element(By.NAME, 'wd').send_keys('find_Element_By_Name')
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

    def test_linktext(self):
        self.test_id()
        self.driver.find_element(By.LINK_TEXT, '百度首页').click()
        sleep(3)
        self.driver.quit()

    # 一部分链接
    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '首页').click()
        sleep(3)
        self.driver.quit()

    # ctrl+F 唤出xpath校验文本框
    def test_xpath(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('find_Element_By_Xpath')
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        sleep(3)
        self.driver.quit()

    def test_Tag_Name(self):
        inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        print(inputs[0])
        sleep(3)
        self.driver.quit()

    # def test_Css_Selector(self):


    # def test_Class_Name(self):


if __name__ == '__main__':
    case = TestCase()
    # case.test_linktext()
    # case.test_partial_link_text()
    # case.test_xpath()
    case.test_Tag_Name()