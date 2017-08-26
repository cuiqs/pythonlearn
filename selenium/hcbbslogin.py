#-*-coding:utf-8-*-
#Login in hcbbs with selenium

import time
from selenium import webdriver

def login(username,password):
    driver=webdriver.Chrome()
    url='http://bbs.hcbbs.com'
    driver.get(url)
    #open url and wait to load
    time.sleep(3)

    user=driver.find_element_by_id('ls_username')
    user.clear()
    user.send_keys(username)

    pw=driver.find_element_by_id('ls_password')
    pw.clear()
    pw.send_keys(password)

    pw.send_keys(u'\ue006') #press RETURN

    time.sleep(5)

if __name__=='__main__':
    user=raw_input('username:')
    pw=raw_input('password:')
    login(user,pw)


