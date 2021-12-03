__author__ = 'Huangthunder'

# coding=utf-8
#  本文件简易的封装定位单个元素和定位一组元素及selenium常规API操作的方法

import time
from selenium import webdriver
from public.common.log import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

success = "SUCCESS   "
fail = "FAIL      "
logger = Log()

# 初始化driver
def __init__(self, driver):
    self.driver = driver

# logger.info方法打印日志信息
def my_print(msg):
    logger.info(msg)

# 定义浏览器类型
def browser(browser):
    try:
        t1 = time.time()
        if browser == "chrome":
            driver = webdriver.Chrome()
            # my_print("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
            return driver
        elif browser == "firefox":
            driver = webdriver.Firefox()
            # my_print("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            # my_print("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            # my_print("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
            return driver
        else:
            print("Not found this browser, You can enter 'chrome','firefox','ie' or 'phantomjs'")
    except Exception as msg:
        print("%s" % msg)

# get方法浏览器中请求测试地址
def open(self,url):
    """
    open url.

    Usage:
    location.open(self,"https://www.baidu.com")
    """
    t1 = time.time()
    try:
        self.driver.get(url)
        # self.driver.maximize_window()
        my_print("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
    except Exception:
        my_print("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
        raise

# maximize_window方法浏览器最大化
def max_window(self):
    """
    Set browser window maximized.
    Usage:
    
    location.max_window(self)
    """
    t1 = time.time()
    try:
        self.driver.maximize_window()
        # my_print("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))
    except Exception:
        # my_print("{0} Unable set browser window maximized, Spend {1} seconds".format(fail, time.time() - t1))
        raise

# minimize_window方法浏览器最大化
def min_window(self):
    """
    Set browser window minimized.

    Usage:
    location.min_window(self)
    """
    t1 = time.time()
    self.driver.maximize_window()
    my_print("{0} Set browser window minimized, Spend {1} seconds".format(success, time.time() - t1))

# set_window_size方法指定浏览器大小
def set_window(self, wide, high):
    """
    Set browser window wide and high.

    Usage:
    location.set_window(self,wide,high)
    """
    t1 = time.time()
    self.driver.set_window_size(wide, high)
    my_print("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,wide,high,time.time() - t1))

# close方法浏览器关闭(关闭当前窗口)
def close(self):
    """
    Simulates the user clicking the "close" button in the titlebar of a popup
    window or tab.

    Usage:
    location.close(self)
    """
    t1 = time.time()
    self.driver.close()
    my_print("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

# close_all方法浏览器关闭所有窗口
def close_all(self):
    """
    Simulates the user clicking the "close" button in the titlebar of a popup
    window or tab.

    Usage:
    location.close_all(self)
    """
    t1 = time.time()
    self.driver.close_all()
    my_print("{0} Closed all window, Spend {1} seconds".format(success, time.time() - t1))

# quit方法浏览器退出(退出整个浏览器)
def quit(self):
    """
    Quit the driver and close all the windows.

    Usage:
    location.quit(self)
    """
    t1 = time.time()
    self.driver.quit()
    # my_print("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))


# 调用webdriver的API方法获取元素id属性
def findId(driver,id):
    """
    Usage:
    location.findId(self,'id->kw')
    """
    t1 = time.time()
    try:
        if "->" not in id:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = id.split("->")[0].strip()
        value = id.split("->")[1].strip()
        if by == "id":
            element = driver.find_element_by_id(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, id, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, id, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素name属性
def findName(driver,name):
    """
    Usage:
    location.findName(self,'name->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "name":
            element = driver.find_element_by_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素class属性
def findClassName(driver,name):
    """
    Usage:
    location.findClassName(self,'classname->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "classname":
            element = driver.find_element_by_class_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素name属性
def findTagName(driver,name):
    """
    Usage:
    location.findTagName(self,'tagname->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "tagname":
            element = driver.find_element_by_tag_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素link_text属性
def findLinkText(driver,text):
    """
    Usage:
    location.findLinkText(self,'linktext->kw')
    """
    t1 = time.time()
    try:
        if "->" not in text:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = text.split("->")[0].strip()
        value = text.split("->")[1].strip()
        if by == "linktext":
            element = driver.find_element_by_link_text(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素partial_link_text属性
def findPLinkText(driver,text):
    """
    Usage:
    location.findPLinkText(self,'plinktext->kw')
    """
    t1 = time.time()
    try:
        if "->" not in text:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = text.split("->")[0].strip()
        value = text.split("->")[1].strip()
        if by == "plinktext":
            element = driver.find_element_by_partial_link_text(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素xpath属性
def findXpath(driver,name):
    """
    Usage:
    location.findXpath(self,'xpath->kw')
    """
    t1 = time.time()
    try:
        t1 = time.time()
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "xpath":
            element = driver.find_element_by_xpath(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素css属性
def findCss(driver,name):
    """
    Usage:
    location.findCss(self,'css->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        t1 = time.time()
        if by == "css":
            element = driver.find_element_by_css_selector(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return element
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组id属性
def findsId(driver,id):
    """
    Usage:
    location.findsId(self,'id->kw')
    """
    t1 = time.time()
    try:
        if "->" not in id:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = id.split("->")[0].strip()
        value = id.split("->")[1].strip()
        if by == "id":
            elements = driver.find_elements_by_id(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, id, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, id, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组name属性
def findsName(driver,name):
    """
    Usage:
    location.findsName(self,'name->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "name":
            elements = driver.find_elements_by_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组class属性
def findsClassName(driver,name):
    """
    Usage:
    location.findsClassName(self,'classname->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "classname":
            elements = driver.find_elements_by_class_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组name属性
def findsTagName(driver,name):
    """
    Usage:
    location.findsTagName(self,'tagname->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "tagname":
            elements = driver.find_elements_by_tag_name(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组link_text属性
def findsLinkText(driver,text):
    """
    Usage:
    location.findsLinkText(self,'linktext->kw')
    """
    t1 = time.time()
    try:
        if "->" not in text:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = text.split("->")[0].strip()
        value = text.split("->")[1].strip()
        if by == "linktext":
            elements = driver.find_elements_by_link_text(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组partial_link_text属性
def findsPLinkText(driver,text):
    """
    Usage:
    location.findsPLinkText(self,'plinktext->kw')
    """
    t1 = time.time()
    try:
        if "->" not in text:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = text.split("->")[0].strip()
        value = text.split("->")[1].strip()
        if by == "plinktext":
            elements = driver.find_elements_by_partial_link_text(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组xpath属性
def findsXpath(driver,name):
    """
    Usage:
    location.findsXpath(self,'xpath->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "xpath":
            elements = driver.find_elements_by_xpath(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素一组css属性
def findsCss(driver,name):
    """
    Usage:
    location.findsCss(self,'css->kw')
    """
    t1 = time.time()
    try:
        if "->" not in name:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = name.split("->")[0].strip()
        value = name.split("->")[1].strip()
        if by == "css":
            elements = driver.find_elements_by_css_selector(value)
            my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
        return elements
    except Exception:
        my_print("{0} Unable find element: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
        raise

# 调用webdriver的API方法获取元素属性
def get_element(driver, css):
    """
    Judge element positioning way, and returns the element.

    Usage:
    location.get_element(self,'id->kw')
    """
    if "->" not in css:
        raise NameError("Positioning syntax errors, lack of '->'.")

    by = css.split("->")[0].strip()
    value = css.split("->")[1].strip()
    t1 = time.time()
    # 调用webdriver的API方法获取元素id属性
    if by == "id":
        element = driver.find_element_by_id(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素name属性
    elif by == "name":
        element = driver.find_element_by_name(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素class属性
    elif by == "class":
        element = driver.find_element_by_class_name(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素link全部(完全匹配)超链接属性
    elif by == "link_text":
        element = driver.find_element_by_link_text(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素link部分(模糊匹配)超链接属性
    elif by == "partial_link_text":
        element = driver.find_element_by_partial_link_text(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素xpath属性
    elif by == "xpath":
        element = driver.find_element_by_xpath(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素css属性
    elif by == "css":
        element = driver.find_element_by_css_selector(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    # 调用webdriver的API方法获取元素tag标签属性
    elif by == "tag_name":
        element = driver.find_element_by_tag_name(value)
        my_print("{0} Typed element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    else:
        raise NameError(
            "Please enter the correct targeting elements,'id','name','class','link_text','partial_link_text','xpaht','css','tag_name'.")
    return element

# implicitly_wait方法隐性等待
def wait(driver, secs):
    """
    Implicitly wait.All elements on the page.

    Usage:
    location.wait(self,10)
    """
    t1 = time.time()
    driver.implicitly_wait(secs)
    my_print("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,secs,time.time() - t1))

# webDriverWait方法显性等待公式
def element_wait(driver, css, secs=5):
    """
    Waiting for an element to display.

    Usage:
    location.element_wait(self,"id->kw",10)
    """
    if "->" not in css:
        raise NameError("Positioning syntax errors, lack of '->'.")

    by = css.split("->")[0].strip()
    value = css.split("->")[1].strip()
    messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

    if by == "id":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
    elif by == "name":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
    elif by == "class":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
    elif by == "link_text":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
    elif by == "xpath":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
    elif by == "css":
        WebDriverWait(driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),messages)
    else:
        raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

# send_keys方法输入文本内容
def send(self,css,text):
    """
        Quit the driver and close all the windows.

        Usage:
        location.send(self,'xpath->is',text)
        """
    t1 = time.time()
    try:
        el = get_element(self,css)
        el.send_keys(text)
        my_print("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,css, text, time.time() - t1))
    except Exception:
        my_print("{0} Unable to send element: <{1}> content: {2}, Spend {3} seconds".format(fail,css, text,time.time() - t1))
        raise

# clear方法清除文本内容和send_keys方法输入文本内容
def clear_send(self, css, text):
    """
    Clear and input element.

    Usage:
    location.clear_send(self,"id->kw","selenium")
    """
    t1 = time.time()
    try:
        el = get_element(self,css)
        # el.clear()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACK_SPACE)
        el.send_keys(text)
        my_print("{0} Clear and send element: <{1}> content: {2}, Spend {3} seconds".format(success,css, text,time.time() - t1))
    except Exception:
        my_print("{0} Unable to clear and send element: <{1}> content: {2}, Spend {3} seconds".format(fail,css, text,time.time() - t1))
        raise

# clear方法清除文本内容和send_keys方法输入文本内容
def clear(self, css):
    """
    Clear element.

    Usage:
    location.clear(self,"id->kw")
    """
    t1 = time.time()
    try:
        el = get_element(self, css)
        # el.clear()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACK_SPACE)
        my_print("{0} Clear element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
    except Exception:
        my_print("{0} Unable to clear element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
        raise

# click方法点击某个元素
def click(self, css):
    """
    It can click any text / image can be clicked
    Connection, check box, radio buttons, and even drop-down box etc..

    Usage:
    location.click(self,"id->kw")
    """
    t1 = time.time()
    try:
        el = get_element(self,css)
        el.click()
        my_print("{0} Clicked element: <{1}>, Spend {2} seconds".format(success,css,time.time() - t1))
    except Exception:
        my_print("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
        raise