#!/usr/bin/python
# written by owen kealey
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from threading import Thread

driver1 = webdriver.Chrome()

driver2 = webdriver.Chrome()

driver3 = webdriver.Chrome()

driver4 = webdriver.Chrome()

driver5 = webdriver.Chrome()

driver6 = webdriver.Chrome()

driver7 = webdriver.Chrome()

driver8 = webdriver.Chrome()

driver9 = webdriver.Chrome()

driver10 = webdriver.Chrome()
url = "http://www.adidas.com/yeezy"
def dodriver1():
    driver1.set_window_size(1, 1)
    driver1.implicitly_wait(5)
    driver1.get(url)
    try:
        driver1.implicitly_wait(2)
        driver1.find_element_by_class_name("addtocartbutton").click()
        driver1.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver1.delete_all_cookies()
        dodriver1()
def dodriver2():
    driver2.set_window_size(1, 1)
    driver2.implicitly_wait(5)
    driver2.get(url)
    try:
        driver2.implicitly_wait(2)
        driver2.find_element_by_class_name("addtocartbutton").click()
        driver2.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver2.delete_all_cookies()
        dodriver2()
def dodriver3():
    driver3.set_window_size(1, 1)
    driver3.implicitly_wait(5)
    driver3.get(url)
    try:
        driver3.implicitly_wait(2)
        driver3.find_element_by_class_name("addtocartbutton").click()
        driver3.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver3.delete_all_cookies()
        dodriver3()
def dodriver4():
    driver4.set_window_size(1, 1)
    driver4.implicitly_wait(5)
    driver4.get(url)
    try:
        driver4.implicitly_wait(2)
        driver4.find_element_by_class_name("addtocartbutton").click()
        driver4.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver4.delete_all_cookies()
        dodriver4()
def dodriver5():
    driver5.set_window_size(1, 1)
    driver5.implicitly_wait(5)
    driver5.get(url)
    try:
        driver5.implicitly_wait(2)
        driver5.find_element_by_class_name("addtocartbutton").click()
        driver5.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver5.delete_all_cookies()
        dodriver5()
def dodriver6():
    driver6.set_window_size(1, 1)
    driver6.implicitly_wait(5)
    driver6.get(url)
    try:
        driver6.implicitly_wait(2)
        driver6.find_element_by_class_name("addtocartbutton").click()
        driver6.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver6.delete_all_cookies()
        dodriver6()
def dodriver7():
    driver7.set_window_size(1, 1)
    driver7.implicitly_wait(5)
    driver7.get(url)
    try:
        driver7.implicitly_wait(2)
        driver7.find_element_by_class_name("addtocartbutton").click()
        driver7.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver7.delete_all_cookies()
        dodriver7()

def dodriver8():
    driver8.set_window_size(1, 1)
    driver8.implicitly_wait(5)
    driver8.get(url)
    try:
        driver8.implicitly_wait(2)
        driver8.find_element_by_class_name("addtocartbutton").click()
        driver8.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver8.delete_all_cookies()
        dodriver8()
def dodriver9():
    driver9.set_window_size(1, 1)
    driver9.implicitly_wait(5)
    driver9.get(url)
    try:
        driver9.implicitly_wait(2)
        driver9.find_element_by_class_name("addtocartbutton").click()
        driver9.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver9.delete_all_cookies()
        dodriver9()
def dodriver10():
    driver10.set_window_size(1, 1)
    driver10.implicitly_wait(5)
    driver10.get(url)
    try:
        driver10.implicitly_wait(2)
        driver10.find_element_by_class_name("addtocartbutton").click()
        driver10.set_window_size(1000,1000)
        return
    except NoSuchElementException:
        driver10.delete_all_cookies()


if __name__ == '__main__':
    Thread(target = dodriver1).start()
    Thread(target = dodriver2).start()
    Thread(target=dodriver3).start()
    Thread(target=dodriver4).start()
    Thread(target=dodriver5).start()
    Thread(target=dodriver6).start()
    Thread(target=dodriver7).start()
    Thread(target=dodriver8).start()
    Thread(target=dodriver9).start()
    Thread(target=dodriver10).start()
