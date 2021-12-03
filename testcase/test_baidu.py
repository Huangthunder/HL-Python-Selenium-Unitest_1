#coding=utf-8
import unittest
from time import sleep
from public.common import untest
from public.common.log import Log
from public.common import location
from public.common.location import browser
from public.keyword.baiduPage import baiduindex01
from public.keyword.baiduPage import baiduindex02
from public.keyword.baiduPage import baiduindex03
from public.keyword.baiduPage import baiduindex04
from public.keyword.baiduPage import baiduindex05


class TestBaiduIndex01(untest.UnTest):
    """百度搜索测试01"""
    def test_hh01(self):
        """百度搜索测试001"""
        location.open(self, "https://www.baidu.com/")
        location.send(self.driver, 'id->kw', "测试01")
        location.click(self.driver, 'id->su')
        sleep(4)
        title = self.driver.title
        self.assertIn('测试01', title)

    def test_hh02(self):
        """百度搜索测试002"""
        location.open(self, "https://www.baidu.com/")
        location.send(self.driver, 'id->w', "测试02")
        location.click(self.driver, 'id->su')
        sleep(4)
        title = self.driver.title
        self.assertIn('测试02', title)

    def test_hh03(self):
        """百度搜索测试003"""
        location.open(self, "https://www.baidu.com/")
        location.send(self.driver, 'id->kw', "测试03")
        location.click(self.driver, 'id->su')
        sleep(0)
        title = self.driver.title
        self.assertIn('测试03', title)

class TestBaiduIndex02(untest.UnTest):
    """百度搜索测试02"""
    def test_hh04(self):
        """百度搜索测试004"""
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys("测试02")
        self.driver.find_element_by_id('su').click()
        sleep(0)
        title = self.driver.title
        self.assertIn('测试02',title)

class TestBaiduIndex03(unittest.TestCase):
    """百度搜索测试03"""
    @classmethod
    def setUpClass(cls):
        cls.logger = Log()
        cls.logger.info('############################### START ###############################')
        cls.driver = browser('chrome')
        location.max_window(cls)

    def test_hh05(self):
        """百度搜索测试005"""
        location.open(self, "https://www.baidu.com/")
        location.max_window(self)
        location.send(self.driver, 'id->kw', "测试03")
        location.click(self.driver, 'id-su')
        sleep(0)
        title = self.driver.title
        self.assertIn('测试03', title)

    @classmethod
    def tearDownClass(cls):
        location.quit(cls)
        cls.logger.info('###############################  END  ###############################')

class TestBaiduIndex04(untest.UnTest):
    """百度搜索测试04"""
    def test_hh06(self):
        """百度搜索测试006"""
        baiduindex01(self)
        sleep(5)
        title = self.dr.get_title()
        self.assertIn('测试04', title)

class TestBaiduIndex05(untest.UnTest):
    """百度搜索测试05"""
    def test_hh07(self):
        """百度搜索测试007"""
        baiduindex02(self)
        sleep(0)
        title = self.dr.get_title()
        self.assertIn('测试01', title)

    def test_hh08(self):
        """百度搜索测试008"""
        baiduindex02(self)
        sleep(5)
        title = self.dr.get_title()
        self.assertIn('测试01', title)

class TestBaiduIndex06(untest.UnTest):
    """百度搜索测试06"""
    def test_hh09(self):
        """百度搜索测试009"""
        baiduindex03(self)
        sleep(5)

    def test_hh10(self):
        """百度搜索测试010"""
        baiduindex04(self)
        sleep(5)

    def test_hh11(self):
        """百度搜索测试010"""
        baiduindex05(self)
        sleep(5)

class TestBaiduIndex07(untest.UnTest):
    """百度文库测试001"""
    def test_baiduwenku01(self):
        self.dr.open_browser('https://wenku.baidu.com/')
        sleep(3)
        # t = self.driver.find_elements_by_class_name('class->type-check')
        # t = self.dr.get_elements('class->type-check')
        self.dr.log('测试1')
        self.dr.get_element_count('class->type-check')
        self.dr.log('测试2')
        # list = self.dr.get_text_list('class->type-check')
        list = self.dr.get_text_list('class->lit-team')
        self.dr.log(list)
        self.assertIn('高考',list)
        # s = self.dr.get_session_id()
        # self.dr.log('测试3')
        # # self.dr.log(t)
        # self.dr.log('测试4')
        # self.dr.log(s)
        # # self.dr.click(t[5])
        # sleep(2)
        # # self.dr.get_source()
        # # self.dr.click_elements('class->type-check')
        # self.dr.click_elements_num('class->type-check',2)
        # self.dr.sleep(2)

    # def tearDown(self):
    #     self.dr.log('测试一下单独执行清除操作01')

    def test_baiduwenku02(self):
        self.dr.open_browser('https://www.baidu.com/')
        self.dr.sleep(5)
        # self.dr.mouse_over('class->bri')
        # self.dr.select_new_window('linktext->新闻')
        self.dr.click_link('新闻')
        # self.dr.click_element('name->tj_settingicon')
        self.dr.click_link('开辟“中国之治”新境界')
        self.dr.sleep(2)
        # self.dr.switch_new_window()
        self.dr.switch_window_title('百度—海量中文资讯平台')
        # self.dr.click_element('class->setpref')
        self.dr.sleep(3)
        # self.dr.select_by_index('name->NR',2)
        self.dr.sleep(5)
        # self.dr.get_text('xpath->//*[@id="channel-all"]/div/ul/li[2]/a')
        self.dr.sleep(3)
        # f = self.dr.element_exist('xpath->//*[@id="channel-all"]/div/ul/li[2]/a')
        f = self.dr.get_text('class->news-location')
        self.dr.log(f)
        self.dr.log('元素存在！！！')

    def tearDown(self):
        self.dr.log('测试一下单独执行清除操作02')

class TestBaiduIndex08(untest.UnTest):
    """百度文库测试002"""
    def test_baiduwenku02(self):
        self.dr.open_browser('https://www.baidu.com/')
        self.dr.sleep(3)
        # t = self.driver.find_elements_by_class_name('class->type-check')
        # t = self.dr.get_elements('class->type-check')
        self.dr.log('测试1')
        # self.dr.get_element_count('class->type-check')
        self.dr.log('测试2')
        s = self.dr.get_session_id()
        self.dr.log('测试3')
        # self.dr.log(t)
        self.dr.log('测试4')
        self.dr.log(s)
        title = self.dr.get_title()
        self.assertIn('百度一下',title)
        # self.dr.clear_cookies()
        # self.dr.get_cookie('h')
        self.dr.input_text('id->kw','测试输入内容后回车操作')
        self.dr.click_by_enter('id->kw')
        value1 = self.dr.get_value('id->su')
        self.dr.log(value1)
        value2 = self.dr.get_attribute('id->su','id')
        self.dr.log(value2)
        r = self.dr.element_exist('id->su')
        self.dr.log(r)
        re = self.dr.get_displayed('id->su')
        self.dr.log(re)
        self.dr.sleep(3)
        # r1 = self.driver.find_element_by_id('dd').is_displayed()
        # self.dr.log(r1)
        r2 = self.dr.get_enabled('id->su')
        self.dr.log(r2)

class TestBaiduInput01(untest.UnTest):
    """百度上传文件测试001"""
    def test_baidufile01(self):
        self.dr.open_browser('https://www.baidu.com/')
        self.dr.sleep(3)
        self.dr.click_element('class->soutu-btn')
        self.dr.sleep(5)
        # self.dr.choose_file('class->upload-pic','D:\\黄雷\\1.jpg')
        self.dr.click_element('class->upload-wrap')
        # self.dr.click_element('xpath->/html/body/div[1]/div[1]/div/div[1]/div/form/div/div[2]/div[2]/input')
        self.dr.sleep(5)
        # self.dr.upload_file_firefox('D:\\黄雷\\1.jpg')
        self.dr.upload_file_chrome('D:\\黄雷\\1.jpg')
        self.dr.sleep(30)
