from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get(url='https://www.jianshu.com/p/3aa45532e179')
browser.close()