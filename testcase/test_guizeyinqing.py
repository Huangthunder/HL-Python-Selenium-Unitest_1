__author__ = 'Huangthunder'
# coding:utf-8
from public.common import untest
from public.pages import iotShinengPage
from public.keyword.closebrowsekeyword import closebrowse
from public.keyword.openandmaxbrowsekeyword import openbrowse
from public.keyword.createguizeyinqingkeyword import createguize01
from public.keyword.createguizeyinqingkeyword import createguize02
from public.keyword.createguizeyinqingkeyword import createguize03
from public.keyword.createguizeyinqingkeyword import createguize04

class IotPage (untest.UnTest):
    """规则引擎测试"""
    def setUp(self):
        # 调用打开浏览器及最大化浏览器关键字
        openbrowse(self)
    def test_iot01(self):
        # 调用创建规则步骤关键字
        createguize01(self)
    def tearDown(self):
        # 调用关闭浏览器关键字
        closebrowse(self)

class IotGuize01(untest.UnTest):
    """规则引擎001"""
    def test_guize01(self):
        createguize03(self)
        title = self.dr.get_title()
        self.assertIn('规则引擎 _ AEP', title)

class IotGuize02(untest.UnTest):
    """规则引擎002"""
    def test_guize02(self):
        createguize04(self)
        title = self.dr.get_title()
        self.assertIn('规则引擎 _ AEP', title)


class Iot01(untest.UnTest):
    def test001(self):
        self.dr.open_browser('https://dm.aeptest.ctwing.cn/index.html?token=4&true#/product?t=1&token=c4')
        self.dr.sleep(10)
        # 输入用户名密码
        self.dr.input_text('xpath->//*[@id="fm1"]/div[1]/div/div[1]/input','huanglei')
        self.dr.input_text('xpath->//*[@id="fm1"]/div[2]/div/div[1]/input','3er4#ER$')
        # 点击登录按钮
        self.dr.sleep(1)
        self.dr.submit_element('xpath->//*[@id="fm1"]/div[4]/div/div[1]/button')
        self.dr.sleep(30)
        self.dr.click_element('xpath->/html/body/div[1]/div/div/section/div[2]/div[1]/div[1]/div/div/div[1]/button')
        self.dr.sleep(5)
        self.dr.click_element('id->tab-subscriptionTab')
        self.dr.sleep(3)
        self.dr.click_element('xpath->//*[@id="pane-subscriptionTab"]/div/div[1]/div[3]/button')
        self.dr.sleep(3)
        t = self.dr.get_displayed('class->el-input__inne')
        # t = self.dr.get_enabled('class->el-input__inner')
        # t = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.dr.log(t)