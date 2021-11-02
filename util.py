from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path='.\drivers\chromedriver.exe')
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    sleep(1)

    loc1 = (By.ID, 'kw')

    get_element(driver, *loc1).send_keys('dddd')
    get_element(driver, By.ID, 'su').click()
    sleep(3)
    driver.quit()