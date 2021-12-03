__author__ = 'Huangcius-HL'

from time import sleep
from public.common import location
from public.common.pyselenium import PySelenium
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

def createguize01(self):
        # 输入用户名密码
        # location.get_element(self.driver,username_inputbox_xpath)
        location.open(self,guizeyinqing_page_url)
        location.send(self.driver,username_inputbox_xpath,username_inputcontent)
        location.wait(self.driver,2)
        # location.clear(self.driver,username_inputbox_xpath)
        location.clear_send(self.driver,username_inputbox_xpath,username_inputcontent)
        location.send(self.driver,password_inputbox_xpath,password_inputcontent)
        # 点击登录按钮
        location.click(self.driver,login_button_xpath)
        sleep(5)
        location.wait(self.driver,10)
        # 点击创建规则按钮
        location.click(self.driver,createguize_button_xpath)
        sleep(5)
        location.element_wait(self.driver,createguize_button_xpath,10)
        # 点击直接创建按钮
        location.click(self.driver,zhijiecreate_button_xpath)
        sleep(2)
        # 输入规则描述
        location.send(self.driver,guizemiaoshu_inputbox_xpath,guizemiaoshu_inputcontent)
        sleep(2)
        # 点击产品的选择按钮
        location.click(self.driver,chanpinxuanze_button_xpath)
        sleep(2)
        # 选择对应产品
        location.click(self.driver,duiyingchanpin_button_xpath)
        # 点击确定按钮
        location.click(self.driver,queding_button_xpath)
        sleep(2)
        # 输入规则内容
        location.send(self.driver,guizeneirong_inputbox_xpath,guizeneirong_inputcontent)
        # 点击确定按钮
        location.click(self.driver,queding_button_xpath1)
        sleep(5)

def createguize02(self):
        location.open(self,guizeyinqing_page_url)
        # 输入用户名密码
        location.findXpath(self.driver,username_inputbox_xpath).send_keys(username_inputcontent)
        location.findXpath(self.driver,password_inputbox_xpath).send_keys(password_inputcontent)
        # 点击登录按钮
        location.findXpath(self.driver,login_button_xpath).click()
        sleep(5)
        # 点击创建规则按钮
        location.findXpath(self.driver,createguize_button_xpath).click()
        sleep(5)
        # 点击直接创建按钮
        location.findXpath(self.driver,zhijiecreate_button_xpath).click()
        sleep(2)
        # 输入规则描述
        location.findXpath(self.driver,guizemiaoshu_inputbox_xpath).send_keys(guizemiaoshu_inputcontent)
        sleep(2)
        # 点击产品的选择按钮
        location.findXpath(self.driver,chanpinxuanze_button_xpath).click()
        sleep(2)
        # 选择对应产品
        location.findXpath(self.driver,duiyingchanpin_button_xpath).click()
        # 点击确定按钮
        location.findXpath(self.driver,queding_button_xpath).click()
        sleep(2)
        # 输入规则内容
        location.findXpath(self.driver,guizeneirong_inputbox_xpath).send_keys(guizeneirong_inputcontent)
        # 点击确定按钮
        location.findXpath(self.driver,queding_button_xpath1).click()
        sleep(5)
        # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(current_time)
        # print(current_time1)
        # imagePath = current_time + '.png'
        # # 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
        # pic_path = 'D:\\Huangcius-Python-Selenium\\report\\image\\' + '\\' + imagePath  #设置存储图片路径，测试结果图片可以按照每天进行区分
        # print (pic_path)  #打印图片路径
        # time.sleep(2)
        # self.dr.get_screenshot_as_file(pic_path)


def createguize03(self):
        PySelenium.open_browser(self, guizeyinqing_page_url)
        # 输入用户名密码
        PySelenium.findXpath(self, username_inputbox_xpath).send_keys(username_inputcontent)
        PySelenium.findXpath(self, password_inputbox_xpath).send_keys(password_inputcontent)
        # 点击登录按钮
        # PySelenium.findXpath(self, login_button_xpath).click()
        PySelenium.sleep(self,1)
        PySelenium.submit_element(self, login_button_xpath)
        PySelenium.sleep(self,5)
        # 点击创建规则按钮
        PySelenium.findXpath(self, createguize_button_xpath).click()
        PySelenium.mouse_over(self, createguize_button_xpath)
        PySelenium.right_click_element(self, createguize_button_xpath)
        PySelenium.double_click_element(self, createguize_button_xpath)
        PySelenium.mouse_down(self, createguize_button_xpath)
        PySelenium.drag_and_drop_by_offset(self, createguize_button_xpath,800,900)
        # PySelenium.drag_and_drop(self, createguize_button_xpath,zhijiecreate_button_xpath)
        PySelenium.sleep(self,5)
        # # 点击直接创建按钮
        # PySelenium.findXpath(self, zhijiecreate_button_xpath).click()
        # PySelenium.sleep(self,2)
        # # 输入规则描述
        # PySelenium.findXpath(self, guizemiaoshu_inputbox_xpath).send_keys(guizemiaoshu_inputcontent)
        # PySelenium.sleep(self,2)
        # # 点击产品的选择按钮
        # PySelenium.findXpath(self, chanpinxuanze_button_xpath).click()
        # PySelenium.sleep(self,2)
        # # 选择对应产品
        # PySelenium.findXpath(self, duiyingchanpin_button_xpath).click()
        # # 点击确定按钮
        # PySelenium.findXpath(self, queding_button_xpath).click()
        # PySelenium.sleep(self,2)
        # # 输入规则内容
        # PySelenium.findXpath(self, guizeneirong_inputbox_xpath).send_keys(guizeneirong_inputcontent)
        # # 点击确定按钮
        # PySelenium.findXpath(self, queding_button_xpath1).click()
        # PySelenium.sleep(self,5)

def createguize04(self):
        self.dr.open_browser(guizeyinqing_page_url)
        # 输入用户名密码
        self.dr.findXpath(username_inputbox_xpath)
        self.dr.input_text(username_inputbox_xpath,username_inputcontent)
        self.dr.findXpath(password_inputbox_xpath)
        self.dr.input_text(password_inputbox_xpath,password_inputcontent)
        # 点击登录按钮
        # self.dr.findXpath(login_button_xpath)
        # self.dr.click_element(login_button_xpath)
        self.dr.sleep(1)
        self.dr.submit_element(login_button_xpath)
        self.dr.sleep(5)
        # 点击创建规则按钮
        self.dr.findXpath(createguize_button_xpath)
        self.dr.click_element(createguize_button_xpath)
        # self.dr.mouse_over(createguize_button_xpath)
        # self.dr.right_click_element(createguize_button_xpath)
        # self.dr.double_click_element(createguize_button_xpath)
        # self.dr.mouse_down(createguize_button_xpath)
        # self.dr.drag_and_drop_by_offset(createguize_button_xpath,800,900)
        # self.dr.drag_and_drop(createguize_button_xpath,zhijiecreate_button_xpath)
        self.dr.sleep(5)
        # 点击直接创建按钮
        self.dr.findXpath(zhijiecreate_button_xpath)
        self.dr.click_element(zhijiecreate_button_xpath)
        self.dr.sleep(2)
        # 输入规则描述
        self.dr.findXpath(guizemiaoshu_inputbox_xpath)
        self.dr.input_text(guizemiaoshu_inputbox_xpath,guizemiaoshu_inputcontent)
        self.dr.sleep(2)
        # 点击产品的选择按钮
        self.dr.findXpath(chanpinxuanze_button_xpath)
        self.dr.click_element(chanpinxuanze_button_xpath)
        self.dr.sleep(2)
        # 选择对应产品
        self.dr.findXpath(duiyingchanpin_button_xpath)
        self.dr.click_element(duiyingchanpin_button_xpath)
        # 点击确定按钮
        self.dr.findXpath(queding_button_xpath)
        self.dr.click_element(queding_button_xpath)
        self.dr.sleep(2)
        # 输入规则内容
        self.dr.findXpath(guizeneirong_inputbox_xpath)
        self.dr.input_text(guizeneirong_inputbox_xpath,guizeneirong_inputcontent)
        # 点击确定按钮
        self.dr.findXpath(queding_button_xpath1)
        self.dr.click_element(queding_button_xpath1)
        self.dr.sleep(5)