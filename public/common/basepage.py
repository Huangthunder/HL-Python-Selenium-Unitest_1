#coding=utf-8
from config import globalparam
from public.common.pyselenium import PySelenium

class Page(object):
    """
    这是页面对象的基类
    """
    def __init__(self, dr):
        driver = globalparam.driver
        dr = PySelenium(driver)
        self.dr = dr



