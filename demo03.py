from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
        self.driver.get('https://www.baidu.com')

    def test_prop(self):

        self.driver.find_element(By.PARTIAL_LINK_TEXT, '新闻').click()
        windows = self.driver.window_handles
        # self.driver.switch_to.window(windows[0])
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test_prop()

# print(self.driver.mobile)
# print(self.driver.name) #浏览器名称
# print(self.driver.title)
# print(self.driver.current_url) #域名
# print(self.driver.page_source) #页面源码
# print(self.driver.current_window_handle)
# print(self.driver.window_handles)
# print(self.driver.window_handles)