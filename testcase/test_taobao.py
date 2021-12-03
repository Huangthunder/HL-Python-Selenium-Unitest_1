__author__ = 'Huangthunder'
# coding:utf-8
# from public.common import untest
from public.common import untest

class TestTaobao01(untest.UnTest):
    """淘宝登录测试01"""
    def test_hh01(self):
        """淘宝登录测试001"""
        # self.dr.open("https://www.taobao.com")
        self.dr.open_browser("https://www.taobao.com")
        self.dr.sleep(10)
        self.dr.get_elements('name->q')
        self.dr.get_element_count('name->q')
        self.dr.input_text('name->q','selenium')
        self.dr.sleep(3)
        # self.dr.save_screenshot()
        self.dr.input_and_enter('name->q','男士冬装')
        # self.dr.sleep(10)
        # self.dr.take_screenshot()
        # sousuo = self.dr.get_text('class->search-button')
        # self.dr.log(sousuo)
        # # self.dr.press_key('name->q','\\13')
        # self.dr.sleep(10)
        # title = self.dr.get_title()
        # self.dr.log(title)
        # self.dr.get_url()
        # self.dr.get_element_size('name->q')
        # self.dr.get_window_handles()
        # # self.assertIn('ceshi',title)
        # # self.dr.log('测试通过！！！')
        # self.dr.mouse_over('class->site-nav-menu-hd')
        # # self.dr.sleep(10)
        # self.dr.sleep(10)
