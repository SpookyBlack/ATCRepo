#!/usr/bin/python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Hello! Welcome to GSPR's ATC and Auto Checkout service for Supreme items. This program("bot") takes all of your
information, takes orders on what items you want, what size you want the items to be and what colors you want the items
to be and uses it to checkout. This program can be started any time before 11 am on Thursday and the program will
adjust for the time difference, wait for that period of time, and then, at 11 am,  proceed to ATC/Checkout. Once the
program is started, however, the user's computer must remain open, on and fully awake(cannot go into sleep mode) for the
entire time.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cvvone = "REPLACE ME WITH FIRST 4 DIGITS OF CC NUMBER"
cvvtwo = "REPLACE ME WITH NEXT 4 DIGITS OF CC NUMBER"
cvvthree = "REPLACE ME WITH NEXT 4 DIGITS OF CC NUMBER"
cvvfour = "REPLACE ME WITH LAST 4 DIGITS OF CC NUMBER"
sec_code = "REPLACE ME WITH SECURITY CODE OF CC"
month = 'REPLACE ME WITH EXPIRATION MONTH OF CC'
year = 'REPLACE ME WITH EXPIRATION YEAR OF CC'
name = "REPLACE ME WITH YOUR NAME"
email = "REPLACE ME WITH YOUR EMAIL"
bo = "REPLACE ME WITH STREET ADDRESS"
zcode = "REPLACE ME WITH ZIP CODE"
tel1 = "REPLACE ME WITH FIRST THREE DIGITS OF TEL NUMBER"
tel2 = "REPLACE ME WITH MIDDLE THREE DIGITS OF TEL NUMBER"
lasttel = "REPLACE ME WITH LAST FOUR DIGITS OF TEL NUMBER"

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException, WebDriverException, NoSuchElementException
import datetime, pause, time, pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


now = datetime.datetime.now()
print now
time_list = []
time_list.append(now.year)
time_list.append("-")
time_list.append(now.month)
time_list.append("-")
time_list.append(now.day)
time_list.append("")
time_list.append("T")
time_list.append("10")
time_list.append(":")
time_list.append("59")
time_list.append(":")
time_list.append("42")
time_list.append(".")
time_list.append("0")
time_string = str(time_list)
timestring1 = time_string.replace("[", "")
timestring2 = timestring1.replace("]", "")
timestring3 = timestring2.replace(",", "")
timestring4 = timestring3.replace("'", "")
timestring5 = timestring4.replace(" ", "")
dt = datetime.datetime.strptime(timestring5, "%Y-%m-%dT%H:%M:%S.%f")
print dt
testmode = raw_input("testmode(yes/no)?:")
items = raw_input("How many items(1/2)?:")
kword1 = raw_input("kword1:")
kword2 = raw_input("kword2:")
kword3 = raw_input("kword3:")
kword4 = raw_input("kword4:")
kword5 = raw_input("kword5:")
kword6 = raw_input("kword6:")
cat1 = raw_input("Category of item one?:")
cat2 = raw_input("Category of item two?:")
color1 = raw_input("Color of item one?:")
color2 = raw_input("Color of item two?:")
checksizeone = raw_input("Sized product for item one?:")
if str(checksizeone) == "yes":
    size1 = raw_input("What size?:")
else:
    pass
checksizetwo = raw_input("Sized product for item two?:")
if str(checksizetwo) == "yes":
    size2 = raw_input("What size?:")
else:
    pass

raw_input("Start?")

driver = webdriver.Chrome()

pause.until(dt)


def waitfunction():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'container')))
def waitfunctioncart():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'add-remove-buttons')))

def waitfunctioncheckout():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button')))
def refreshfunc():
    driver.refresh()


def itemone():
    itemonenow =datetime.datetime.now()
    driver.get("http://www.supremenewyork.com/shop/all/" + str(cat1))
    waitfunction()
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    print "trying to find item one"
    try:
        driver.implicitly_wait(20)
        global t1
        t1 = time.time()
        driver.find_element_by_partial_link_text(kword1).click()
        print "found item one, trying to add it to your cart"
        itemonecolor()
    except NoSuchElementException:
        if str(itemonenow) != str(dt) and testmode == "no":
            refreshfunc()
            itemone()
        try:
            driver.implicitly_wait(.25)
            driver.find_element_by_partial_link_text(kword2).click()
            print "found item one, trying to add it to your cart"
            itemonecolor()
        except NoSuchElementException:
            print "I will keep trying!"
            driver.get("http://www.supremenewyork.com/shop/all/shirts")
            waitfunction()
            try:
                driver.implicitly_wait(.25)
                driver.find_element_by_partial_link_text(kword3).click()
                print "found item one, trying to add it to your cart"
                itemonecolor()
            except NoSuchElementException:
                print "could not find item one, trying to find item two"
                itemtwo()
def itemonecolor():
    waitfunctioncart()
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_xpath(str("//a[@data-style-name=" + str("'") + str(color1) + str("'") + str("]"))).click()
    except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException):
        print "color selection failed for item one, getting default color"
    if checksizeone == "yes":
        try:
            driver.implicitly_wait(.5)
            thing = Select(driver.find_element_by_id("size"))
            thing.select_by_visible_text(size1)
        except (NoSuchElementException, StaleElementReferenceException):
            try:
                driver.implicitly_wait(1)
                thing = Select(driver.find_element_by_id("size"))
                thing.select_by_visible_text(size1)
            except (StaleElementReferenceException, NoSuchElementException):
                print "getting default size(small)"
    else:
        pass


    addtocart()
    try:
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    except WebDriverException:
        print "cookie loading failed"
    if items == 1:
        checkout()
    else:
        itemtwo()


################################################################################################
def itemtwo():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    try:
        for cookie in cookies:
            driver.add_cookie(cookie)
    except WebDriverException:
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except WebDriverException:
            print "cookie loading failed"
    driver.get("http://www.supremenewyork.com/shop/all/" + str(cat2))
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemtwo()
        return
    waitfunction()
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_partial_link_text(kword4).click()
        print "found item two, trying to add it to your cart"
        itemtwocolor()
    except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException):
        try:
            driver.implicitly_wait(.25)
            driver.find_element_by_partial_link_text(kword5).click()
            print "found item two, trying to add it to your cart"
            itemtwocolor()
        except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException):
            print "I will keep trying!"
            try:
                driver.get("http://www.supremenewyork.com/shop/all/hats")
                waitfunction()
                driver.implicitly_wait(.25)
                driver.find_element_by_partial_link_text(kword6)
                itemtwocolor()
            except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException):
                print "could not find item two, now attempting to checkout with whatever is in your cart"
                checkout()


def itemtwocolor():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemtwo()
        return
    waitfunctioncart()
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_xpath(
            str("//a[@data-style-name=" + str("'") + str(color2) + str("'") + str("]"))).click()
    except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException):
        print "color selection failed for item two, getting default color"
    if checksizetwo == "yes":

        try:
            print "trying to get requested size"
            driver.implicitly_wait(.5)
            thing = Select(driver.find_element_by_id("size"))
            thing.select_by_visible_text("Medium")
        except (NoSuchElementException,StaleElementReferenceException):
            try:
                driver.implicitly_wait(1)
                thing = Select(driver.find_element_by_id("size"))
                thing.select_by_visible_text("Medium")
            except(NoSuchElementException,StaleElementReferenceException):
                print "Could not find requested size-getting default size"
    addtocart()
    checkout()


################################################################################################
def addtocart():
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return
    waitfunctioncart()
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_css_selector('input.button').click()
        print "Successfully added this item to your cart"
    except (StaleElementReferenceException, ElementNotVisibleException, NoSuchElementException):
        try:
            time.sleep(.25)
            driver.find_element_by_css_selector('input.button').click()
        except (NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, WebDriverException):
            print "cannot add this item to cart"


#####################################################################################################

def checkout():
    print "starting checkout process"
    cookies = pickle.load(open("cookies.pkl", "rb"))
    try:
        for cookie in cookies:
            driver.add_cookie(cookie)
    except WebDriverException:
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except WebDriverException:
            print "cookie loading failed"
    driver.get("http://supremenewyork.com/checkout")
    #waitfunctioncheckout()
    if str(driver.current_url) == "http://www.supremenewyork.com/shop":
        itemone()
        return


    try:
        driver.implicitly_wait(3)
        driver.implicitly_wait(.5)
        driver.find_element_by_id('order_billing_name').send_keys(name)
    except NoSuchElementException:
        try:
            driver.implicitly_wait(.5)
            driver.find_element_by_id('order_name').send_keys(name)
        except NoSuchElementException:
            print "name selection failed"

    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_id('order_email').send_keys(email)
    except NoSuchElementException:
        try:
            driver.implicitly_wait(.5)
            driver.find_element_by_name("order[email]").send_keys(email)
        except NoSuchElementException:
            try:
                driver.implicitly_wait(.5)
                driver.find_element_by_class_name("email").send_keys(email)
            except NoSuchElementException:
                print "email selection failed"
    driver.implicitly_wait(.5)

    try:
        nametwo = driver.find_element_by_id('order_tel')
        nametwo.send_keys(lasttel)
        time.sleep(.1)

        nametwo.send_keys(tel1)
        time.sleep(.1)

        nametwo.send_keys(tel2)
    except NoSuchElementException:
        print "tel selection failed"
    driver.find_element_by_id("bo").send_keys(bo)
    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_id("order_billing_zip").send_keys(zcode)
    except NoSuchElementException:
        try:
            driver.implicitly_wait(.5)
            driver.find_element_by_name("order[billing_zip]").send_keys(zcode)
        except NoSuchElementException:
            print "zip code selection failed"

    try:
        namesix = driver.find_element_by_id('cnb')

        driver.implicitly_wait(2)

        namesix.send_keys(cvvfour)
        time.sleep(.15)
        namesix.send_keys(cvvone)
        time.sleep(.15)
        namesix.send_keys(cvvtwo)
        time.sleep(.15)
        namesix.send_keys(cvvthree)
    except NoSuchElementException:
        print "cc number failed"

    try:
        driver.implicitly_wait(.5)
        driver.find_element_by_id('vval').send_keys(sec_code)
    except NoSuchElementException:
        driver.find_element_by_id('cvw').send_keys(sec_code)

    try:
        driver.implicitly_wait(5)
        expmonth = Select(driver.find_element_by_id("credit_card_month"))
        expmonth.select_by_visible_text(month)
    except NoSuchElementException:
        print "cc month selection failed"
    try:
        driver.implicitly_wait(.5)
        expyear = Select(driver.find_element_by_id('credit_card_year'))
        expyear.select_by_visible_text(year)
    except NoSuchElementException:
        print "cc year selection failed"
    t2 = time.time()
    new_time = t2-t1
    print "This took %s seconds to run" % new_time
    print "Entire form filled out"

    try:
        driver.implicitly_wait(2)
        elemen = driver.find_elements_by_class_name('iCheck-helper')
        for i in elemen:
            i.click()

    except NoSuchElementException:
        print "PLEASE AGREE TO TERMS AND CONDITIONS BY CLICKING THE CHECKBOX"

def backupcheckout():
    try:
        driver.implicitly_wait(2)
        cnb = driver.find_element_by_id('cnb')

        cnb.clear()

        cnb.send_keys(cvvfour)
        time.sleep(.35)
        cnb.send_keys(cvvone)
        time.sleep(.35)
        cnb.send_keys(cvvtwo)
        time.sleep(.35)
        cnb.send_keys(cvvthree)
    except (NoSuchElementException, StaleElementReferenceException):
        print "cc number failed"
        backupcheckout()
    try:
        driver.implicitly_wait(1)
        num = driver.find_element_by_id('vval')
        num.clear()
        num.send_keys(sec_code)
    except NoSuchElementException:
        print "idk what to do"


def finalize():
    driver.implicitly_wait(.5)
    driver.find_element_by_css_selector('input.button.checkout').click()
    try:
        driver.implicitly_wait(2)
        driver.find_element_by_class_name("errors")
        backupcheckout()
        finalize()
    except NoSuchElementException:
        print "checkout complete, enjoy!"


itemone()
if testmode != "yes":
    finalize()
else:
    print "Just running a test!"












                  



           
           





