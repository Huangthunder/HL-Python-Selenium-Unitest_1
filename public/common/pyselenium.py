__author__ = 'Huangthunder'

# coding=utf-8
# 本文件简易的封装定位单个元素和定位一组元素及selenium常规API操作的方法

import time
# import case
# import win32gui
# import win32con
from selenium import webdriver
from config import globalparam
from public.common.log import Log
from public.common.location import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

success = "SUCCESS   "
fail = "FAIL      "
logger = Log()

class PySelenium(object):
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 定义浏览器类型
    def browser(self):
        try:
            t1 = time.time()
            if browser == "chrome":
                driver = webdriver.Chrome()
                logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
                return driver
            elif browser == "firefox":
                driver = webdriver.Firefox()
                # logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
                return driver
            elif browser == "ie":
                driver = webdriver.Ie()
                # logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
                return driver
            elif browser == "phantomjs":
                driver = webdriver.PhantomJS()
                # logger.info("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
                return driver
            else:
                print("Not found this browser, You can enter 'chrome','firefox','ie' or 'phantomjs'")
        except Exception as msg:
            print("%s" % msg)

    # logger.info方法打印日志信息
    def log(self,msg):
        t1 = time.time()
        try:
            logger.info("{0} Print current value: {1}, Spend {2} seconds".format(success, msg, time.time() - t1))
        except Exception:
            logger.info("{0} Current value not obtained: {1}, Spend {2} seconds".format(fail, msg, time.time() - t1))
            raise

    # get方法浏览器中请求测试地址
    def open_browser(self,url):
        """
        open url.

        Usage:
        PySelenium.open_browser(self,"https://www.baidu.com")
        """
        t1 = time.time()
        try:
            self.driver.get(url)
            logger.info("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    # maximize_window方法浏览器最大化
    def maximize_browser_window(self):
        """
        Set browser window maximized.
        Usage:

        PySelenium.maximize_browser_window(self)
        """
        # t1 = time.time()
        try:
            self.driver.maximize_window()
            # logger.info("{0} Set browser window maximized, Spend {1} seconds".format(success,time.time() - t1))
        except Exception:
            # logger.info("{0} Unable set browser window maximized, Spend {1} seconds".format(fail,time.time() - t1))
            raise

    # minimize_window方法浏览器最大化
    def minimize_browser_window(self):
        """
        Set browser window minimized.

        Usage:
        PySelenium.minimize_browser_window(self)
        """
        # t1 = time.time()
        self.driver.maximize_window()
        # logger.info("{0} Set browser window minimized, Spend {1} seconds".format(success, time.time() - t1))

    # set_window_size方法指定浏览器大小
    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        PySelenium.set_window_size(self,wide,high)
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        logger.info("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success, wide, high, time.time() - t1))

    # close方法浏览器关闭(关闭当前窗口)
    def close_browser(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        PySelenium.close_browser(self)
        """
        # t1 = time.time()
        self.driver.close()
        # logger.info("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    # close_all方法浏览器关闭所有窗口
    def close_all_browser(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        PySelenium.close_all_browser(self)
        """
        # t1 = time.time()
        self.driver.close_all()
        # logger.info("{0} Closed all window, Spend {1} seconds".format(success, time.time() - t1))

    # quit方法浏览器退出(退出整个浏览器)
    def quit_browser(self):
        """
        Quit the driver and close all the windows.

        Usage:
        PySelenium.quit_browser(self)
        """
        # t1 = time.time()
        self.driver.quit()
        # logger.info("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    # refresh方法浏览器刷新(刷新当前页面)
    def reload_page(self):
        """
        Refresh the current page.

        Usage:
        PySelenium.reload_page(self)
        """
        t1 = time.time()
        try:
            self.driver.refresh()
            logger.info("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable refresh the current page, Spend {1} seconds".format(fail, time.time() - t1))

    # back方法浏览器后退(后退箭头)
    def go_back(self):
        """
        Browser Back.

        Usage:
        PySelenium.go_back(self)
        """
        t1 = time.time()
        try:
            self.driver.back()
            logger.info("{0} Browser back, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable browser back, Spend {1} seconds".format(fail, time.time() - t1))

    # forward方法浏览器前进(前进箭头)
    def go_forward(self):
        """
        Browser Forward.

        Usage:
        PySelenium.go_forward(self)
        """
        t1 = time.time()
        try:
            self.driver.forward()
            logger.info("{0} Browser forward, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable {0} browser forward, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # 调用webdriver的API方法获取元素id属性
    def findId(self, id):
        """
        Usage:
        PySelenium.findId(self,'id->kw')
        """
        t1 = time.time()
        try:
            if "->" not in id:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = id.split("->")[0].strip()
            value = id.split("->")[1].strip()
            if by == "id":
                element = self.driver.find_element_by_id(value)
                logger.info("{0} Typed element id: <{1}>, Spend {2} seconds".format(success, id, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element id: <{1}>, Spend {2} seconds".format(fail, id, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'id'.")

    # 调用webdriver的API方法获取元素name属性
    def findName(self, name):
        """
        Usage:
        PySelenium.findName(self,'name->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "name":
                element = self.driver.find_element_by_name(value)
                logger.info("{0} Typed element name: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element name: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'name'.")

    # 调用webdriver的API方法获取元素class属性
    def findClassName(self, name):
        """
        Usage:
        PySelenium.findClassName(self,'class->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "class":
                element = self.driver.find_element_by_class_name(value)
                logger.info("{0} Typed element class: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element class: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'class'.")

    # 调用webdriver的API方法获取元素name属性
    def findTagName(self, name):
        """
        Usage:
        PySelenium.findTagName(self,'tagname->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "tagname":
                element = self.driver.find_element_by_tag_name(value)
                logger.info("{0} Typed element tagname: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element tagname: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'tagname'.")

    # 调用webdriver的API方法获取元素link_text属性
    def findLinkText(self, text):
        """
        Usage:
        PySelenium.findLinkText(self,'linktext->kw')
        """
        t1 = time.time()
        try:
            if "->" not in text:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = text.split("->")[0].strip()
            value = text.split("->")[1].strip()
            if by == "linktext":
                element = self.driver.find_element_by_link_text(value)
                logger.info("{0} Typed element linktext: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element linktext: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'linktext'.")

    # 调用webdriver的API方法获取元素partial_link_text属性
    def findPLinkText(self, text):
        """
        Usage:
        PySelenium.findPLinkText(self,'plinktext->kw')
        """
        t1 = time.time()
        try:
            if "->" not in text:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = text.split("->")[0].strip()
            value = text.split("->")[1].strip()
            if by == "plinktext":
                element = self.driver.find_element_by_partial_link_text(value)
                logger.info("{0} Typed element plinktext: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element plinktext: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'plinktext'.")

    # 调用webdriver的API方法获取元素xpath属性
    def findXpath(self, name):
        """
        Usage:
        PySelenium.findXpath(self,'xpath->kw')
        """
        t1 = time.time()
        try:
            t1 = time.time()
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "xpath":
                element = self.driver.find_element_by_xpath(value)
                logger.info("{0} Typed element xpath: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element xpath: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'xpath'.")

    # 调用webdriver的API方法获取元素css属性
    def findCss(self, name):
        """
        Usage:
        PySelenium.findCss(self,'css->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            t1 = time.time()
            if by == "css":
                element = self.driver.find_element_by_css_selector(value)
                logger.info("{0} Typed element css: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return element
        except Exception:
            logger.info("{0} Unable find element css: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'css'.")

    # 调用webdriver的API方法获取元素一组id属性
    def findsId(self, id):
        """
        Usage:
        PySelenium.findsId(self,'id->kw')
        """
        t1 = time.time()
        try:
            if "->" not in id:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = id.split("->")[0].strip()
            value = id.split("->")[1].strip()
            if by == "id":
                elements = self.driver.find_elements_by_id(value)
                logger.info("{0} Typed element id: <{1}>, Spend {2} seconds".format(success, id, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element id: <{1}>, Spend {2} seconds".format(fail, id, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'id'.")

    # 调用webdriver的API方法获取元素一组name属性
    def findsName(self, name):
        """
        Usage:
        PySelenium.findsName(self,'name->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "name":
                elements = self.driver.find_elements_by_name(value)
                logger.info("{0} Typed element name: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element name: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'name'.")

    # 调用webdriver的API方法获取元素一组class属性
    def findsClassName(self, name):
        """
        Usage:
        PySelenium.findsClassName(self,'class->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "class":
                elements = self.driver.find_elements_by_class_name(value)
                logger.info("{0} Typed element class: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element class: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'class'.")

    # 调用webdriver的API方法获取元素一组name属性
    def findsTagName(self, name):
        """
        Usage:
        PySelenium.findsTagName(self,'tagname->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "tagname":
                elements = self.driver.find_elements_by_tag_name(value)
                logger.info("{0} Typed element tagname: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element tagname: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'tagname'.")

    # 调用webdriver的API方法获取元素一组link_text属性
    def findsLinkText(self, text):
        """
        Usage:
        PySelenium.findsLinkText(self,'linktext->kw')
        """
        t1 = time.time()
        try:
            if "->" not in text:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = text.split("->")[0].strip()
            value = text.split("->")[1].strip()
            if by == "linktext":
                elements = self.driver.find_elements_by_link_text(value)
                logger.info("{0} Typed element linktext: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element linktext: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'linktext'.")

    # 调用webdriver的API方法获取元素一组partial_link_text属性
    def findsPLinkText(self, text):
        """
        Usage:
        PySelenium.findsPLinkText(self,'plinktext->kw')
        """
        t1 = time.time()
        try:
            if "->" not in text:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = text.split("->")[0].strip()
            value = text.split("->")[1].strip()
            if by == "plinktext":
                elements = self.driver.find_elements_by_partial_link_text(value)
                logger.info("{0} Typed element plinktext: <{1}>, Spend {2} seconds".format(success, text, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element plinktext: <{1}>, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'plinktext'.")

    # 调用webdriver的API方法获取元素一组xpath属性
    def findsXpath(self, name):
        """
        Usage:
        PySelenium.findsXpath(self,'xpath->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "xpath":
                elements = self.driver.find_elements_by_xpath(value)
                logger.info("{0} Typed element xpath: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element xpath: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'xpath'.")

    # 调用webdriver的API方法获取元素一组css属性
    def findsCss(self, name):
        """
        Usage:
        PySelenium.findsCss(self,'css->kw')
        """
        t1 = time.time()
        try:
            if "->" not in name:
                raise NameError("Positioning syntax errors, lack of '->'.")
            by = name.split("->")[0].strip()
            value = name.split("->")[1].strip()
            if by == "css":
                elements = self.driver.find_elements_by_css_selector(value)
                logger.info("{0} Typed element css: <{1}>, Spend {2} seconds".format(success, name, time.time() - t1))
            return elements
        except Exception:
            logger.info("{0} Unable find element css: <{1}>, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'css'.")

    # 调用webdriver的API方法获取元素属性
    def get_element(self, css):
        """
        Judge element positioning way, and returns the element.

        Usage:
        PySelenium.get_element(self,'id->kw')
        PySelenium.get_element(self,'name->kw')
        PySelenium.get_element(self,'class->kw')
        PySelenium.get_element(self,'linktext->kw')
        PySelenium.get_element(self,'plinktext->kw')
        PySelenium.get_element(self,'xpath->kw')
        PySelenium.get_element(self,'css->kw')
        PySelenium.get_element(self,'tagname->kw')
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        t1 = time.time()
        # 调用webdriver的API方法获取元素id属性
        try:
            if by == "id":
                element = self.driver.find_element_by_id(value)
                logger.info(
                    "{0} Typed element id: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element id: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'id'.")
        try:
            # 调用webdriver的API方法获取元素name属性
            if by == "name":
                element = self.driver.find_element_by_name(value)
                logger.info(
                    "{0} Typed element name: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element name: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'name'.")
        try:
            # 调用webdriver的API方法获取元素class属性
            if by == "class":
                element = self.driver.find_element_by_class_name(value)
                logger.info(
                    "{0} Typed element class: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element class: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,''class'.")
        try:
            # 调用webdriver的API方法获取元素link全部(完全匹配)超链接属性
            if by == "linktext":
                element = self.driver.find_element_by_link_text(value)
                logger.info(
                    "{0} Typed element linktext: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element linktext: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'linktext'.")
        try:
            # 调用webdriver的API方法获取元素link部分(模糊匹配)超链接属性
            if by == "plinktext":
                element = self.driver.find_element_by_partial_link_text(value)
                logger.info(
                    "{0} Typed element plinktext: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element plinktext: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'plinktext'.")
        try:
            # 调用webdriver的API方法获取元素xpath属性
            if by == "xpath":
                element = self.driver.find_element_by_xpath(value)
                logger.info(
                    "{0} Typed element xpath: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element xpath: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'xpaht'.")
        try:
            # 调用webdriver的API方法获取元素css属性
            if by == "css":
                element = self.driver.find_element_by_css_selector(value)
                logger.info(
                    "{0} Typed element css: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element css: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'css'.")
        try:
            # 调用webdriver的API方法获取元素tag标签属性
            if by == "tagname":
                element = self.driver.find_element_by_tag_name(value)
                logger.info(
                    "{0} Typed element tagname: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element tagname: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'tagname'.")
        return element

    # 调用webdriver的API方法获取一组元素属性
    def get_elements(self, css):
        """
        Judge element positioning way, and returns the element.

        Usage:
        PySelenium.get_elements(self,'id->kw')
        PySelenium.get_elements(self,'name->kw')
        PySelenium.get_elements(self,'class->kw')
        PySelenium.get_elements(self,'linktext->kw')
        PySelenium.get_elements(self,'plinktext->kw')
        PySelenium.get_elements(self,'xpath->kw')
        PySelenium.get_elements(self,'css->kw')
        PySelenium.get_elements(self,'tagname->kw')
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        t1 = time.time()
        # 调用webdriver的API方法获取元素id属性
        try:
            if by == "id":
                elements = self.driver.find_elements_by_id(value)
                logger.info(
                    "{0} Typed element id: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element id: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'id'.")
        try:
            # 调用webdriver的API方法获取元素name属性
            if by == "name":
                elements = self.driver.find_elements_by_name(value)
                logger.info(
                    "{0} Typed element name: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element name: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'name'.")
        try:
            # 调用webdriver的API方法获取元素class属性
            if by == "class":
                elements = self.driver.find_elements_by_class_name(value)
                logger.info(
                    "{0} Typed element class: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element class: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,''class'.")
        try:
            # 调用webdriver的API方法获取元素link全部(完全匹配)超链接属性
            if by == "linktext":
                elements = self.driver.find_elements_by_link_text(value)
                logger.info(
                    "{0} Typed element linktext: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element linktext: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'linktext'.")
        try:
            # 调用webdriver的API方法获取元素link部分(模糊匹配)超链接属性
            if by == "plinktext":
                elements = self.driver.find_elements_by_partial_link_text(value)
                logger.info(
                    "{0} Typed element plinktext: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element plinktext: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'plinktext'.")
        try:
            # 调用webdriver的API方法获取元素xpath属性
            if by == "xpath":
                elements = self.driver.find_elements_by_xpath(value)
                logger.info(
                    "{0} Typed element xpath: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element xpath: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'xpaht'.")
        try:
            # 调用webdriver的API方法获取元素css属性
            if by == "css":
                elements = self.driver.find_elements_by_css_selector(value)
                logger.info(
                    "{0} Typed element css: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element css: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'css'.")
        try:
            # 调用webdriver的API方法获取元素tag标签属性
            if by == "tagname":
                elements = self.driver.find_elements_by_tag_name(value)
                logger.info(
                    "{0} Typed element tagname: <{1}->{2}>, Spend {3} seconds".format(success, by, value, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable find element tagname: <{1}->{2}>, Spend {3} seconds".format(fail, by, value, time.time() - t1))
            raise NameError(
                "Please enter the correct targeting elements,'tagname'.")
        return elements

    # sleep强制等待
    def sleep(self, t):
        """
        Sleep time.

        Usage:
        PySelenium.sleep(self,10)
        """
        t1 = time.time()
        try:
            time.sleep(int(t))
            logger.info("{0} Sleep time: {1}s, Spend {2} seconds".format(success, t, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to get sleep time: {1}s, Spend {2} seconds".format(fail, t, time.time() - t1))
            raise

    # implicitly_wait方法隐性等待
    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        PySelenium.wait(self,10)
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        logger.info("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success, secs, time.time() - t1))

    # webDriverWait方法显性等待公式
    def element_wait(self, css, secs=5):
        """
        Waiting for an element to display.

        Usage:
        PySelenium.element_wait(self,"id->kw",10)
        PySelenium.element_wait(self,"name->kw",10)
        PySelenium.element_wait(self,"class->kw",10)
        PySelenium.element_wait(self,"linktext->kw",10)
        PySelenium.element_wait(self,"xpath->kw",10)
        PySelenium.element_wait(self,"css->kw",10)
        """
        t1 = time.time()
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")
        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)
        try:
            # 根据id元素属性设置等待时间
            if by == "id":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                     by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail ,by, value, secs, time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'id'.")
        try:
            # 根据name元素属性设置等待时间
            if by == "name":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                    by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail, by, value, secs, time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'name'.")
        try:
            # 根据class元素属性设置等待时间
            if by == "class":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)),messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                    by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail, by, value, secs, time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'class'.")
        try:
            # 根据link元素属性设置等待时间
            if by == "linktext":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)),messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                    by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail, by, value, secs, time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'linktext'.")
        try:
            # 根据xpath元素属性设置等待时间
            if by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                    by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail,by, value,secs,time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'xpaht'.")
        try:
            # 根据css元素属性设置等待时间
            if by == "css":
                WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),messages)
                logger.info(
                    "{0} Set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(success,
                    by, value, secs, time.time() - t1))
        except Exception:
            logger.info(
                    "{0} Unable set wait current element: <{1}->{2}> display in {3} seconds, Spend {4} seconds".format(
                    fail, by, value, secs, time.time() - t1))
            raise NameError(
                    "Please enter the correct targeting elements,'css'.")

    # send_keys方法输入文本内容
    def input_text(self, css, text):
        """
        input element.

        Usage:
        PySelenium.input_text(self,'xpath->is',text)
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            el.send_keys(text)
            logger.info("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success, css, text, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to send element: <{1}> content: {2}, Spend {3} seconds".format(fail, css, text, time.time() - t1))
            raise

    # clear方法清除文本内容和send_keys方法输入文本内容
    def clear_input_text(self, css, text):
        """
        Clear and input element.

        Usage:
        PySelenium.clear_input_text(self,"id->kw","selenium")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            # el.clear()
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACK_SPACE)
            el.send_keys(text)
            logger.info("{0} Clear and send element: <{1}> content: {2}, Spend {3} seconds".format(success, css, text, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to clear and send element: <{1}> content: {2}, Spend {3} seconds".format(fail, css, text, time.time() - t1))
            raise

    # 清除输入框内容后输入内容并点击ENTER回车键
    def input_and_enter(self, css, text, secs=2):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        PySelenium.send_and_keys(self,'id->kw','beck')
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACK_SPACE)
            el.send_keys(text)
            time.sleep(secs)
            el.send_keys(Keys.ENTER)
            logger.info("{0} Typed element <{1}> input content: {2}, sleep {3}s,input ENTER key, Spend {4} seconds".format(
                        success, css, text, secs, time.time() - t1))
        except Exception:
            logger.info("{0} Unable element <{1}> input content: {2}, sleep {3}s,input ENTER key, Spend {4} seconds".format(
                        fail, css, text, secs, time.time() - t1))
            raise

    # clear方法清除文本内容和send_keys方法输入文本内容
    def clear_element_text(self, css):
        """
        Clear element.

        Usage:
        PySelenium.clear(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            # el.clear()
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.BACK_SPACE)
            logger.info("{0} Clear element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to clear element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # click方法点击某个元素
    def click_element(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        PySelenium.click_element(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            el.click()
            logger.info("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 循环点击一组元素中的每个元素
    def click_elements(self,css):
        '''
        循环点击一组元素中的每个元素
        :param selector:
        :return:

        Usage:
        PySelenium.click_elements(self,"id->kw")
        '''
        counts = PySelenium.get_element_count(self,css)
        t1 = time.time()
        try:
            for i in range(counts):
                els = PySelenium.get_elements(self, css)
                els[i].click()
                logger.info("{0} Clicked elements: <{1}>, number: [{2}], Spend {3} seconds".format(success, css, i, time.time() - t1))
        except Exception:
            logger.info("{0} Unable clicked elements: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 点击一组元素中的指定第几个元素
    def click_elements_num(self, css, num):
        '''
        点击一组元素中的第几个元素
        :param selector:
        :param i: 第几个元素
        :return:

        Usage:
        PySelenium.click_elements_num(self,"id->kw",2)
        '''
        t1 = time.time()
        try:
            els = PySelenium.get_elements(self, css)
            els[num].click()
            logger.info("{0} Clicked elements: <{1}>, to connect number: [{2}], Spend {3} seconds".format(success, css, num, time.time() - t1))
        except Exception:
            logger.info("{0} Unable clicked elements: <{1}>, to connect number: [{2}], Spend {3} seconds".format(fail, css, num, time.time() - t1))
            raise

    # 在某个元素做回车操作
    def click_by_enter(self, css):
        """
        It can type any text / image can be located  with ENTER key

        Usage:
        PySelenium.click_by_enter(self,"id->su")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            el.send_keys(Keys.ENTER)
            logger.info("{0} Clicked element: <{1}>, operate the Enter key, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable clicked element: <{1}>, operate the Enter key, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # submit方法提交表单
    def submit_element(self, css):
        """
        Submit the specified form.

        Usage:
        PySelenium.submit_element(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            el.submit()
            logger.info("{0} Submit form args element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 调用webdriver的API方法获取元素link部分(模糊匹配)超链接属性,点击部分连接内容
    def click_link(self, text):
        """
        Click the element by the link text

        Usage:
        PySelenium.click_link(self,"新闻")
        """
        t1 = time.time()
        try:
            self.driver.find_element_by_partial_link_text(text).click()
            logger.info("{0} Click by text content: {1}, Spend {2} seconds".format(success, text, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to Click by text content: {1}, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise

    # 通过所有index定位元素
    def select_by_index(self, css, index):
        """
        通过所有index，0开始定位元素
        
        Usage:
        PySelenium.select_by_index(self,"name->q",2)
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            Select(el).select_by_index(index)
            logger.info("{0} Select the current element index: <{1}>, connect: {2}, Spend {3} seconds".format(success, css, index, time.time() - t1))
        except Exception:
            logger.info("{0} Unable select the current element index: <{1}>, connect: {2}, Spend {3} seconds".format(fail, css, index, time.time() - t1))
            raise

    # 通过所有value定位元素
    def select_by_value(self, css, value):
        """
        通过所有value开始定位元素

        Usage:
        PySelenium.select_by_value(self,"name->q",'20')
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            Select(el).select_by_value(value)
            logger.info("{0} Select the current element value: <{1}>, connect: {2}, Spend {3} seconds".format(success, css, value, time.time() - t1))
        except Exception:
            logger.info("{0} Unable select the current element value: <{1}>, connect: {2}, Spend {3} seconds".format(fail, css, value, time.time() - t1))
            raise

    # 通过所有visible_text定位元素
    def select_by_text(self, css, text):
        """
        通过所有visible_text开始定位元素

        Usage:
        PySelenium.select_by_visible_text(self,"name->q",'每页20条')
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            Select(el).select_by_visible_text(text)
            logger.info("{0} Select the current element text: <{1}>, connect: {2}, Spend {3} seconds".format(success, css, text, time.time() - t1))
        except Exception:
            logger.info("{0} Unable select the current element text: <{1}>, connect: {2}, Spend {3} seconds".format(fail, css, text, time.time() - t1))
            raise

    # 获取select元素的选择的内容
    def get_select_text(self, css):
        """
        获取 Select 元素的选择的内容
        :param css: 选择字符 "i, xxx"
        :return: 字符串

        Usage:
        PySelenium.get_select_text(self,"name->q")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            selected_opt = Select(el).first_selected_option()
            logger.info("{0} Get the current element text content: {1}, Spend {3} seconds".format(success, css, time.time() - t1))
            return selected_opt.text
        except Exception:
            logger.info("{0} Unable get the current element text content: {1}, Spend {3} seconds".format(fail, css, time.time() - t1))
            raise

    # context_click方法模拟鼠标右键点击操作
    def right_click_element(self, css):
        """
        Right click element.

        Usage:
        PySelenium.right_click_element(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            ActionChains(self.driver).context_click(el).perform()
            logger.info("{0} Right click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # move_to_element鼠标悬停在一个元素上(出现下拉列表框)
    def mouse_over(self, css):
        """
        Mouse over the element.

        Usage:
        PySelenium.mouse_over(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("{0} Move to element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable move to element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # move_to_element\move_by_offset鼠标移除元素
    def mouse_out(self, css):
        """
        Simulates moving mouse away from the element.

        See the `Locating elements` section for details about the locatorsyntax.
        Usage:
        PySelenium.mouse_out(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            size = el.size
            offsetx = (size['width'] / 2) + 1
            offsety = (size['height'] / 2) + 1
            ActionChains(self.driver).move_to_element(el).move_by_offset(offsetx, offsety).perform()
            logger.info("{0} Move out element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} unable move out element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # click_and_hold按下鼠标左键在一个元素上
    def mouse_down(self, css):
        """
        Left click on an element.

        Usage:
        PySelenium.mouse_down(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            ActionChains(self.driver).click_and_hold(el).perform()
            logger.info("{0} Click and hold to element: <{1}>, Spend {2} seconds".format(success, css,time.time() - t1))
        except Exception:
            logger.info("{0} Unable click and hold to element: <{1}>, Spend {2} seconds".format(fail, css,time.time() - t1))
            raise

    # release释放鼠标左键在一个元素上
    def mouse_up(self, css):
        """
        Simulates releasing the left mouse button on the element.

        See the `Locating elements` section for details about the locatorsyntax.
        Usage:
        PySelenium.mouse_up(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            ActionChains(self.driver).release(el).perform()
            logger.info("{0} Releasing mouse button  element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable releasing mouse button  element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # double_click方法模拟鼠标双击操作
    def double_click_element(self, css):
        """
        Double click element.

        Usage:
        PySelenium.double_click_element(self,"id->kw")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            ActionChains(self.driver).double_click(el).perform()
            logger.info("{0} Double click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # drag_and_drop(source,target)方法鼠标拖拽(source：鼠标按下的源元素；target：鼠标释放的目标元素)
    def drag_and_drop(self, el_css, ta_css):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        PySelenium.drag_and_drop(self,"id->kw","id->su")
        """
        t1 = time.time()
        try:
            element = PySelenium.get_element(self,el_css)
            target = PySelenium.get_element(self,ta_css)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            logger.info("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                el_css, ta_css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                el_css, ta_css, time.time() - t1))
            raise

    # drag_and_drop_by_offset(source,x,y)定义鼠标拖放动作
    def drag_and_drop_by_offset(self, source, xoffset, yoffset):
        """
        Left click on an element.

        Usage:
        PySelenium.drag_and_drop_by_offset(self,sorce,800,900)
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,source)
            ActionChains(self.driver).drag_and_drop_by_offset(el, int(xoffset), int(yoffset)).perform()
            logger.info("{0} Drag and drop by offset element: <{1}>, Spend {2} seconds".format(success, source, time.time() - t1))
        except Exception:
            logger.info("{0} Unable drag and drop by offset element: <{1}>, Spend {2} seconds".format(fail, source, time.time() - t1))
            raise

    # execute_script方法页面滑动至某个位置
    def js_execute(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        PySelenium.js_execute(self,"window.scrollTo(200,1000);")
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            logger.info("{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail, script, time.time() - t1))
            raise

    # execute_script方法滑动到页面顶部
    def js_scroll_top(self):
        """
        Execute JavaScript script to top.

        Usage:
        PySelenium.js_scroll_top(self)
        """
        t1 = time.time()
        try:
            js = "window.scrollTo(0,0)"
            self.driver.execute_script(js)
            logger.info("{0} Execute javascript script to top: {1}, Spend {2} seconds".format(success, js, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to execute javascript script to top: {1}, Spend {2} seconds".format(fail, js, time.time() - t1))
            raise

    # execute_script方法滑动到页面底部
    def js_scroll_end(self):
        """
        Execute JavaScript script to the bottom.

        Usage:
        PySelenium.js_scroll_end(self)
        """
        t1 = time.time()
        try:
            js = "window.scrollTo(0, document.body.scrollHeight)"
            # js = 'window.scrollTo(0,100000000000)'
            self.driver.execute_script(js)
            logger.info("{0} Execute javascript script to the bottom: {1}, Spend {2} seconds".format(success, js, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to execute javascript script to the bottom: {1}, Spend {2} seconds".format(fail, js, time.time() - t1))
            raise

    # execute_script方法聚焦元素
    def set_focus_to_element(self, css):
        """
        Execute script focus element.

        Usage:
        PySelenium.set_focus_to_element(self,'linktext->新闻')
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            logger.info("{0} Execute script focus element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable execute script focus element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))

    # get_attribute方法获取元素属性值
    def get_attribute(self, css, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        PySelenium.get_attribute(self,"id=su","value")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            attr = el.get_attribute(attribute)
            logger.info("{0} Get attribute element: <{1}>, attribute: {2}, Spend {3} seconds".format(success, css, attr, time.time()-t1))
            return attr
        except Exception:
            logger.info("{0} Unable to get attribute element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def get_value(self, css):
        """
        返回元素的 value
        :param css: 定位字符串
        :return:

        Usage:
        PySelenium.get_value(self,"id=su")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self,css)
            logger.info("{0} Get attribute element: <{1}>, value: {2}, Spend {3} seconds".format(success, css, el.get_attribute("value"), time.time()-t1))
            return el.get_attribute("value")
        except Exception:
            logger.info("{0} Unable to get attribute element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # text获取元素值
    def get_text(self, css):
        """
        Returns the text value of element identified by ``locator``.

        Usage:
        PySelenium.get_text(self,"id=su")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            elt = el.text
            logger.info("{0} Get element: <{1}>, connect: {2}, Spend {3} seconds".format(success, css, elt, time.time() - t1))
            return elt
        except Exception:
            logger.info("{0} Unable get element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 获取一组元素的多个文本内容
    def get_text_list(self, css):
        """
        根据css 获取多个元素，取得元素的text 列表
        :param css:
        :return: list

        Usage:
        PySelenium.get_text_list(self,"id=su")
        """
        t1 = time.time()
        try:
            el_list = PySelenium.get_elements(self, css)
            results = []
            for el in el_list:
                results.append(el.text)
            logger.info("{0} Get element: <{1}>, return list: {2}, Spend {3} seconds".format(success, css, results, time.time() - t1))
            return results
        except Exception:
            logger.info("{0} Unable get element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # title获取窗口标题
    def get_title(self):
        """
        Returns the title of current page.

        Usage:
        PySelenium.get_title(self)
        """
        t1 = time.time()
        try:
            el = self.driver.title
            logger.info("{0} Get current window title: {1}, Spend {2} seconds".format(success, el, time.time() - t1))
            return el
        except Exception:
            logger.info("{0} Unable get current window title, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # len获取元素的总数
    def get_element_count(self, css):
        """
        Returns number of elements matching ``locator``.

        Usage:
        PySelenium.get_element_count(self,"id=su")
        """
        t1 = time.time()
        try:
            els = PySelenium.get_elements(self, css)
            logger.info("{0} Get the number of current elements: {1}, count: {2}, Spend {3} seconds".format(success, css, len(els), time.time() - t1))
            return len(els)
        except Exception:
            logger.info("{0} Unable get the number of current elements: {1}, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 获取元素坐标
    def get_element_size(self, css):
        """
        Returns width and height of element identified by ``locator``.
        
        Usage:
        PySelenium.get_element_size(self,"id=su")
        """
        t1 = time.time()
        try:
            el = PySelenium.get_element(self, css)
            logger.info("{0} Typed element: <{1}>, width:{2} x height:{3}, Spend {4} seconds".format(success, css,
                        el.size['width'], el.size['height'], time.time() - t1))
            return el.size['width'], el.size['height']
        except Exception:
            logger.info("{0} Unable typed element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 获取当前会话的session id
    def get_session_id(self):
        """
        Returns the currently active browser session id.

        Usage:
        PySelenium.get_session_id(self)
        """
        t1 = time.time()
        try:
            el = self.driver.session_id
            logger.info("{0} Return current browser session id: {1}, Spend {2} seconds".format(success, el, time.time() - t1))
            return  el
        except Exception:
            logger.info("{0} Unable return current browser session id, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def get_source(self):
        """
        Returns the entire HTML source of the current page or frame.
        
        Usage:
        PySelenium.get_source(self)
        """
        t1 = time.time()
        try:
            el = self.driver.page_source
            logger.info("{0} Return current page source: {1}, Spend {2} seconds".format(success, el, time.time() - t1))
            return el
        except Exception:
            logger.info("{0} Unable return current page source, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def get_url(self):
        """
        Returns the current browser URL.
        
        Usage:
        PySelenium.get_url(self)
        """
        t1 = time.time()
        try:
            el = self.driver.current_url
            logger.info("{0} Get current page url: {1}, Spend {2} seconds".format(success, el, time.time() - t1))
            return el
        except Exception:
            logger.info("{0} Unable get current page url, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # 元素是否显示(可见)
    def get_displayed(self, css):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        PySelenium.get_displayed("id->su")
        """
        t1 = time.time()
        try:
            if PySelenium.get_element(self, css).is_displayed():
                logger.info("{0} Get current element: <{1}>, return: True, Spend {2} seconds".format(success, css, time.time() - t1))
                return True
            else:
                logger.info("{0} Unable get current element: <{1}>, return: False, Spend {2} seconds".format(fail, css, time.time() - t1))
                return False
        except Exception:
            raise

    # 元素是否可点击(是否被禁用)
    def get_enabled(self,css):
        '''
        判断页面元素是否可点击
        :param selector: 元素定位
        :return: 布尔值

        Usage:
        PySelenium.get_enabled("id->su")
        '''
        t1 = time.time()
        try:
            if PySelenium.get_element(self, css).is_enabled():
                logger.info("{0} Get current element: <{1}>, return: True, Spend {2} seconds".format(success, css, time.time() - t1))
                return True
            else:
                logger.info("{0} Get current element: <{1}>, return: False, Spend {2} seconds".format(success, css, time.time() - t1))
                return False
        except Exception:
            logger.info("{0} Unable get current element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))

    # 元素是否被选中
    def get_selected(self,css):
        '''
        判断页面元素是否被选中
        :param selector: 元素定位
        :return: 布尔值

        Usage:
        PySelenium.get_selected("id->su")
        '''
        t1 = time.time()
        try:
            if PySelenium.get_element(self, css).is_selected():
                logger.info("{0} Get current element: <{1}>, return: True, Spend {2} seconds".format(success, css, time.time() - t1))
                return True
            else:
                logger.info("{0} Get current element: <{1}>, return: False, Spend {2} seconds".format(success, css, time.time() - t1))
                return False
        except Exception:
            logger.info("{0} Unable get current element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))

    def get_window_handles(self):
        """
        Return all current window handles as a list.

        Usage:
        PySelenium.get_window_handles(self)
        """
        t1 = time.time()
        try:
            el = self.driver.window_handles
            logger.info("{0} Return all current window handles:{1}, Spend {2} seconds".format(success, el, time.time() - t1))
            return el
        except Exception:
            logger.info("{0} Unable return all current window handles, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # ASCIA密钥代码到密钥的映射关系
    def _map_ascii_key_code_to_key(self, key_code):
        map = {
            0: Keys.NULL,
            8: Keys.BACK_SPACE,
            9: Keys.TAB,
            10: Keys.RETURN,
            13: Keys.ENTER,
            24: Keys.CANCEL,
            27: Keys.ESCAPE,
            32: Keys.SPACE,
            42: Keys.MULTIPLY,
            43: Keys.ADD,
            44: Keys.SEPARATOR,
            45: Keys.SUBTRACT,
            56: Keys.DECIMAL,
            57: Keys.DIVIDE,
            59: Keys.SEMICOLON,
            61: Keys.EQUALS,
            127: Keys.DELETE
        }
        key = map.get(key_code)
        if key is None:
            key = chr(key_code)
        return key

    # 键盘使用ASCIA密钥操作使用
    def press_key(self, css, key):
        """
        Deprecated use `Press Keys` instead.
        
        Usage:
        PySelenium.press_key(self,"id=su","\\13")
        """
        t1 = time.time()
        try:
            if key.startswith('\\') and len(key) > 1:
                key = self._map_ascii_key_code_to_key(int(key[1:]))
            el = PySelenium.get_element(self, css)
            el.send_keys(key)
            logger.info("{0} Elements to be operated: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable elements to be operated: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # accept方法选择弹窗的"确定"按钮
    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        PySelenium.accept_alert(self)
        """
        t1 = time.time()
        try:
            self.driver.switch_to.alert.accept()
            logger.info("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable accept warning box, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # dismiss方法选择弹窗的"取消"按钮
    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        PySelenium.dismiss_alert(self)
        """
        t1 = time.time()
        try:
            self.driver.switch_to.alert.dismiss()
            logger.info("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable dismisses the alert available, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # text方法选择弹窗的文本内容
    def text_alert(self):
        """
        Getting text content.

        Usage:
        PySelenium.text_alert(self)
        """
        t1 = time.time()
        try:
            self.driver.switch_to.alert.text()
            logger.info("{0} Getting text content, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable getting text content, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # switch_to.frame多表单切换到指定frame中
    def switch_to_frame(self, css):
        """
        Switch to the specified frame.

        Usage:
        PySelenium.switch_to_frame(self,"id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            iframe_el = PySelenium.get_element(self, css)
            self.driver.switch_to.frame(iframe_el)
            logger.info("{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 返回上一级的当前窗体计算机窗体与switch_to_frame()方法的对应关系
    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        PySelenium.switch_to_frame_out(self)
        """
        t1 = time.time()
        try:
            self.driver.switch_to.default_content()
            logger.info("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable switch to frame out, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # switch_to.window方法多窗口切换(切换至某个窗口)
    def select_new_window(self, css):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        PySelenium.select_new_window(self,"id=kw")
        """
        t1 = time.time()
        try:
            current_windows = self.driver.current_window_handle
            el = PySelenium.get_element(self, css)
            el.click()
            all_handles = self.driver.window_handles
            for new_handle in all_handles:
                if new_handle != current_windows:
                    self.driver.switch_to.window(new_handle)
            logger.info("{0} Click element: <{1}> open new window and switch success, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            logger.info("{0} Unable click element: <{1}> open new window switch fail, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    # 通过索引切换窗口,左边从0开始，-1是右边第一个窗口
    def switch_new_window(self):
        """
        Into the new window.

        Usage:
        PySelenium.switch_new_window(self)
        """
        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            logger.info("{0} Switch to the new window, new window's url: {1}, Spend {2} seconds".format(success,
                        self.driver.current_url,time.time() - t1))
        except Exception:
            logger.info("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # 通过页面标题切换窗口
    def switch_window_title(self, title):
        t1 = time.time()
        try:
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                time.sleep(3)
                if self.driver.title == title:
                    logger.info("{0} Window title: {1} switch window success, Spend {2} seconds".format(success, title, time.time() - t1))
                    break
                else:
                    self.driver.title != title
                    logger.info("{0} Window title: {1} failed to switch window, Spend {2} seconds".format(success, title, time.time() - t1))
                    continue
        except Exception:
            raise

    # get_screenshot_as_file(filename)方法截取当前页面
    def take_screenshot(self):
        """
        Get the current window screenshot.

        Usage:
        PySelenium.take_screenshot(self,'c:/test.png')
        """
        t1 = time.time()
        try:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            reportPath = globalparam.img_path
            imagePath = current_time + '.png'
            pic_path = reportPath + '\\' + imagePath
            self.driver.get_screenshot_as_file(pic_path)
            logger.info("{0} Get the current window screenshot, path: {1}, Spend {2} seconds".format(success, pic_path, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to get the current window screenshot, path: {1}, Spend {2} seconds".format(fail, pic_path, time.time() - t1))
            raise

    # save_screenshot方法保存截图
    def save_screenshot(self):
        """
        Get the current window screenshot.

        Usage:
        PySelenium.save_screenshot(self,'c:/test.png')
        """
        t1 = time.time()
        try:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            reportPath = globalparam.img_path
            imagePath = current_time + '.png'
            pic_path = reportPath + '\\' + imagePath
            self.driver.save_screenshot(pic_path)
            logger.info("{0} Get the current window screenshot, path: {1}, Spend {2} seconds".format(success, pic_path, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to get the current window screenshot, path: {1}, Spend {2} seconds".format(fail, pic_path, time.time() - t1))
            raise

    # get_screenshot_as_base64方法保存截图
    def base64_screenshot(self):
        """
        Get the current window screenshot.

        Usage:
        PySelenium.base64_screenshot(self)
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_base64()
            logger.info("{0} Get the current window base64 screenshot, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to get the current window base64 screenshot, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    # 判断元素是否存在返回结果为true或false
    def element_exist(self, css):
        """
        Judge element is exist,The return result is true or false.

        Usage:
        PySelenium.element_exist(self,"id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            logger.info("{0} Find element: <{1}> is exist, Spend {2} seconds".format(success,css, time.time() - t1))
            return True
        except TimeoutException:
            logger.info("{0} Unable find element: <{1}> is not exist, Spend {2} seconds".format(fail, css, time.time() - t1))
            return False

    # 获取浏览器cookie
    def get_cookie(self, name):
        """

        """
        t1 = time.time()
        try:
            self.driver.get_cookie(name)
            logger.info("{0} Get cookie name: {1}, Spend {2} seconds".format(success, self.driver.get_cookie(), time.time() - t1))
        except Exception:
            logger.info("{0} Unable get cookie name: {1}, Spend {2} seconds".format(fail, self.driver.get_cookie(), time.time() - t1))
            raise

    # 清除所有浏览器cookies
    def clear_cookies(self):
            """
            clear all cookies after driver init

            Usage:
            PySelenium.clear_cookies(self)
            """
            t1 = time.time()
            try:
                self.driver.delete_all_cookies()
                logger.info("{0} Delete all cookies, Spend {1} seconds".format(success, time.time() - t1))
            except Exception:
                logger.info("{0} Unable delete all cookie, Spend {1} seconds".format(fail, time.time() - t1))
                raise

    # 添加多个cookies
    def add_cookies(self, cookies):
            """
            Add cookie by dict
            :param cookies:
            :return:

            Usage:
            PySelenium.add_cookies(self,cookie_dict=cookies)
            """
            t1 = time.time()
            try:
                self.driver.add_cookie(cookie_dict=cookies)
                logger.info("{0} Add cookies by: {1}, Spend {2} seconds".format(success, cookies, time.time() - t1))
            except Exception:
                logger.info("{0} Unable add cookies: {1}, Spend {2} seconds".format(fail, cookies, time.time() - t1))
                raise

    # 添加单个cookie
    def add_cookie(self, cookie_dict):
            """
            Add single cookie by dict
            添加 单个 cookie
            如果该 cookie 已经存在，就先删除后，再添加
            :param cookie_dict: 字典类型，有两个key：name 和 value
            :return:

            Usage:
            PySelenium.add_cookie(self,cookie_dict)
            """
            cookie_name = cookie_dict["name"]
            cookie_value = self.driver.get_cookie(cookie_name)
            t1 = time.time()
            try:
                if cookie_value is not None:
                    self.driver.delete_cookie(cookie_name)
                self.driver.add_cookie(cookie_dict)
                logger.info("{0} Add cookie by: {1}, Spend {2} seconds".format(success, cookie_dict, time.time() - t1))
            except Exception:
                logger.info("{0} Unable add cookie: {1}, Spend {2} seconds".format(fail, cookie_dict, time.time() - t1))
                raise

    # 移除指定的cookie
    def remove_cookie(self, name):
        """
        移除指定 name 的cookie
        :param name:
        :return:

        Usage:
        PySelenium.remove_cookie(self,cookie)
        """
        # 检查 cookie 是否存在,存在就移除
        old_cookie_value = self.driver.get_cookie(name)
        t1 = time.time()
        try:
            if old_cookie_value is not None:
                self.driver.delete_cookie(name)
                logger.info("{0} Delete cookie name: {1}, Spend {2} seconds".format(success, name, time.time() - t1))
        except Exception:
            logger.info("{0} Unable delete cookie name: {1}, Spend {2} seconds".format(fail, name, time.time() - t1))
            raise

    # input类型上传文件
    def choose_file(self,css,file):
        '''
        上传文件 （ 标签为 input 类型，此类型最常见，最简单）
        :param css: 上传按钮定位
        :param file: 将要上传的文件（绝对路径）
        :return: 无

        Usage:
        PySelenium.choose_file(self,'class->ss',D:\\黄雷\\1.jpg')
        '''
        t1 = time.time()
        try:
            PySelenium.get_element(self, css).send_keys(file)
            logger.info("{0} Get file path: {1}, upload file success, Spend {2} seconds".format(success, file, time.time() - t1))
        except Exception:
            logger.info("{0} Get file path: {1}, failed to upload file, Spend {2} seconds".format(fail, file, time.time() - t1))
            raise

    # # 非input类型上传文件火狐浏览器
    # def upload_file_firefox(self,file):
    #     '''
    #     上传文件 （ 标签不是 input 类型，使用 win32gui,得先安装 pywin32 依赖包）
    #     pip install pywin32
    #     :param browser_type: 浏览器类型（Chrome浏览器和Firefox浏览器的有区别）
    #     :param file: 将要上传的文件（绝对路径）
    #     单个文件：file1 = 'C:\\Users\\list_tuple_dict_test.py'
    #     同时上传多个文件：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
    #     :return: 无

    #     Usage:
    #     PySelenium.upload_file_firefox(self,'D:\\黄雷\\1.jpg')
    #     '''
    #     # Firefox 浏览器是'文件上传'
    #     # 对话框
    #     # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
    #     t1 = time.time()
    #     try:
        #     dialog = win32gui.FindWindow('#32770', u'文件上传')
        #     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        #     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        #     time.sleep(1)
        #     # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        #     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        #     # 确定按钮Button
        #     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        #     # 往输入框输入绝对地址
        #     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
        #     time.sleep(2)
        #     # 按button
        #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        #     logger.info("{0} Get file path: {1}, upload file success, Spend {2} seconds".format(success, file, time.time() - t1))
        # except Exception:
        #     logger.info("{0} Get file path: {1}, failed to upload file, Spend {2} seconds".format(fail, file, time.time() - t1))
        #     raise

    # # 非input类型上传文件谷歌浏览器
    # def upload_file_chrome(self,file):
    #     '''
    #     上传文件 （ 标签不是 input 类型，使用 win32gui,得先安装 pywin32 依赖包）
    #     pip install pywin32
    #     :param browser_type: 浏览器类型（Chrome浏览器和Firefox浏览器的有区别）
    #     :param file: 将要上传的文件（绝对路径）
    #     单个文件：file1 = 'C:\\Users\\list_tuple_dict_test.py'
    #     同时上传多个文件：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
    #     :return: 无

    #     Usage:
    #     PySelenium.upload_file_chrome(self,'D:\\黄雷\\1.jpg')
    #     '''
    #     # Chrome 浏览器是'打开'
    #     # 对话框
    #     # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
    #     t1 = time.time()
    #     try:
    #         dialog = win32gui.FindWindow('#32770', u'打开')
    #         ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #         ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #         # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #         Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #         time.sleep(1)
    #         # 确定按钮Button
    #         button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #         # 往输入框输入绝对地址
    #         win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
    #         time.sleep(2)
    #         # 按button
    #         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #         logger.info("{0} Get file path: {1}, upload file success, Spend {2} seconds".format(success, file, time.time() - t1))
    #     except Exception:
    #         logger.info("{0} Get file path: {1}, failed to upload file, Spend {2} seconds".format(fail, file, time.time() - t1))
    #         raise

    # # 非input类型上传文件IE浏览器
    # def upload_file_ie(self,file):
    #     '''
    #     上传文件 （ 标签不是 input 类型，使用 win32gui,得先安装 pywin32 依赖包）
    #     pip install pywin32
    #     :param browser_type: 浏览器类型（Chrome浏览器和Firefox浏览器的有区别）
    #     :param file: 将要上传的文件（绝对路径）
    #     单个文件：file1 = 'C:\\Users\\list_tuple_dict_test.py'
    #     同时上传多个文件：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
    #     :return: 无

    #     Usage:
    #     PySelenium.upload_file_chrome(self,'D:\\黄雷\\1.jpg')
    #     '''
    #     # IE 浏览器是'选择要加载的文件'
    #     # 对话框
    #     # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
    #     t1 = time.time()
    #     try:
    #         dialog = win32gui.FindWindow('#32770', u'选择要加载的文件')
    #         ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #         ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #         # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #         Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #         time.sleep(1)
    #         # 确定按钮Button
    #         button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #         # 往输入框输入绝对地址
    #         win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
    #         time.sleep(2)
    #         # 按button
    #         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #         logger.info("{0} Get file path: {1}, upload file success, Spend {2} seconds".format(success, file, time.time() - t1))
    #     except Exception:
    #         logger.info("{0} Get file path: {1}, failed to upload file, Spend {2} seconds".format(fail, file, time.time() - t1))
    #         raise

if __name__ == '__main__':
    # driver = browser('chrome')
    pass