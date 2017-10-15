#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

display = Display(visible=0,size=(800,600))
display.start()
# driver = webdriver.PhantomJS(executable_path=r'D:\geckodriver\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.PhantomJS(executable_path='phantomjs',service_log_path='/tmp/ghostdriver.log')
driver.set_window_size(0,0)
driver.set_page_load_timeout(30)
# driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)


def isPrased(xpath):
    return EC.presence_of_element_located((By.XPATH, xpath))


def get_xpath_text(xpath):
    wait.until(isPrased(xpath))
    return driver.find_element_by_xpath(xpath).text

def A_click(xpath):
    search_button_element = driver.find_element_by_xpath(xpath)
    ActionChains(driver).click(search_button_element).perform()