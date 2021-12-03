__author__ = 'Huangcius-HL'
# coding:utf-8
from public.common import untest
from public.common.pyselenium import  PySelenium

class TestJdLogin01(untest.UnTest):
    """京东登录测试01"""
    def test_hh01(self):
        """京东登录测试001"""
        dr = PySelenium
        dr.open_browser(self,"https://www.jd.com")
        dr.sleep(self,3)
        dr.js_scroll_end(self)
        dr.sleep(self,3)
        # dr.click_element(self,'class->link-login')
        # dr.sleep(self,3)
        # dr.click_link(self,'账户登录')
        # dr.sleep(self,3)
        # dr.input_text(self,'name->loginname','test')
        # dr.input_text(self,'name->nloginpwd','123456')
        # dr.click_element(self,'id->loginsubmit')
        # dr.sleep(self,10)
        # # # 定位滑块元素
        # # slider = self.driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
        # # # 定义鼠标拖放动作
        # # # weizhi = [188, 198, 137, 131]
        # # ActionChains(self.driver).drag_and_drop_by_offset(slider, 1000, 0).perform()
        # dr.sleep(self,3)
        # dr.drag_and_drop_by_offset(self,'xpath->//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]',1000, 0)
        # dr.sleep(self,10)
