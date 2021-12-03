# coding=utf-8

from time import sleep
from public.common import basepage
from public.variable.guizeyinqingvariable import  guizeyinqing_page_url
from public.variable.guizeyinqingvariable import username_inputbox_xpath
from public.variable.guizeyinqingvariable import username_inputcontent
from public.variable.guizeyinqingvariable import password_inputbox_xpath
from public.variable.guizeyinqingvariable import password_inputcontent
from public.variable.guizeyinqingvariable import login_button_xpath
from public.variable.guizeyinqingvariable import createguize_button_xpath
from public.variable.guizeyinqingvariable import zhijiecreate_button_xpath
from public.variable.guizeyinqingvariable import guizemiaoshu_inputbox_xpath
from public.variable.guizeyinqingvariable import guizemiaoshu_inputcontent
from public.variable.guizeyinqingvariable import chanpinxuanze_button_xpath
from public.variable.guizeyinqingvariable import duiyingchanpin_button_xpath
from public.variable.guizeyinqingvariable import queding_button_xpath
from public.variable.guizeyinqingvariable import guizeneirong_inputbox_xpath
from public.variable.guizeyinqingvariable import guizeneirong_inputcontent
from public.variable.guizeyinqingvariable import queding_button_xpath1

class IotGuizePage(basepage.Page):
    """规则引擎创建"""

    def open_iotguize_page(self):
        """打开规则引擎页面"""
        self.dr.open_browser(guizeyinqing_page_url)
        self.dr.wait(20)

    def open_iotguize_page1(self):
        """打开规则引擎页面"""
        self.dr.open_browser(guizeyinqing_page_url)
        self.dr.wait(20)

    def create_iotguize_page(self):
        """创建规则引擎"""
        self.dr.sleep(5)
        # self.dr.get_element('//*[@id="fm1"]/div[1]/div/div[1]/input')
        # 输入用户名密码
        self.dr.input_text(username_inputbox_xpath,username_inputcontent)
        self.dr.sleep(5)
        self.dr.input_text(password_inputbox_xpath, password_inputcontent)
        # 点击登录按钮
        self.dr.click_element(login_button_xpath)
        self.dr.sleep(5)
        # 点击创建规则按钮
        self.dr.click_element(createguize_button_xpath)
        sleep(2)
        # 点击直接创建按钮
        self.dr.click_element(zhijiecreate_button_xpath)
        sleep(2)
        # 输入规则描述
        self.dr.input_text(guizemiaoshu_inputbox_xpath, guizemiaoshu_inputcontent)
        sleep(2)
        # 点击产品的选择按钮
        self.dr.click_element(chanpinxuanze_button_xpath)
        sleep(2)
        # 选择对应产品
        self.dr.click_element(duiyingchanpin_button_xpath)
        # 点击确定按钮
        self.dr.click_element(queding_button_xpath)
        sleep(2)
        # 输入规则内容
        self.dr.input_text(guizeneirong_inputbox_xpath, guizeneirong_inputcontent)
        # 点击确定按钮
        self.dr.click_element(queding_button_xpath1)
        self.dr.sleep(5)