__author__ = 'Huangcius-HL'
# coding:utf-8
from public.common import untest
from public.common.pyselenium import  PySelenium

class TestCnbLogin01(untest.UnTest):
    """博客园登录测试01"""
    def test_hh01(self):
        """博客园登录测试001"""
        dr = PySelenium
        dr.open_browser(self,"https://account.cnblogs.com")
        dr.click_link(self,"登录")
        # dr.click(self,'xpath->// *[ @ id = "span_userinfo"] / a[1]')
        # dr.send(self,'class->form-control','test')
        dr.input_text(self,'id->LoginName','test')
        dr.input_text(self,'id->Password','123456')
        dr.click_element(self,'class->ladda-label')
        dr.sleep(self,3)
        # # 定位滑块元素
        # slider = self.driver.find_element_by_class_name("geetest_slider_button")
        # # 定义鼠标拖放动作
        # # weizhi = [188, 198, 137, 131]
        # ActionChains(self.driver).drag_and_drop_by_offset(slider, 1000, 0).perform()
        dr.sleep(self,3)
        dr.drag_and_drop_by_offset(self,'class->geetest_slider_button',2000,0)
        dr.sleep(self,10)
