__author__ = 'Huangthunder'
# coding=utf-8

def baiduindex01(self):
    self.dr.open_browser("https://www.baidu.com/")
    self.dr.input_text('id->kw',"测试04")
    self.dr.click_element('id->su')

def baiduindex02(self):
    self.dr.open_browser("https://www.baidu.com/")
    self.dr.wait(10)
    self.dr.get_element("name->wd")
    self.dr.get_element("id->kw")
    self.dr.get_element("class->quickdelete")
    self.dr.get_element('xpath->//*[@id="kw"]')
    self.dr.findXpath('xpath->//*[@id="kw"]')
    self.dr.findId("id->kw")
    self.dr.findId('id->kw')
    # self.dr.element_wait("class->_ipt", 5)
    self.dr.element_wait("class->s_ipt", 5)
    self.dr.input_text("class->s_ipt","测试05")
    self.dr.element_wait('id->su',5)
    self.dr.findId('id->su').click()
    self.dr.click_element('id->su')
    self.dr.clear_input_text("class->s_ipt","测试05")
    self.dr.clear_element_text("class->s_ipt")
    self.dr.wait(10)

def baiduindex03(self):
    self.dr.open_browser("https://www.baidu.com/")
    self.dr.sleep(2)
    self.dr.click_link("新闻")
    self.dr.set_focus_to_element('linktext->新闻')
    self.dr.get_value('id->su', 'id')
    t1 = self.dr.get_value('id->su', 'textContent')
    self.dr.log(t1)
    t2 = self.dr.get_value('id->su', 'innerHTML')
    self.dr.log(t2)
    t3 = self.dr.get_value('id->su', 'outerHTML')
    self.dr.log(t3)
    t4 = self.dr.get_value('id->su', 'value')
    self.dr.log(t4)
    self.dr.log('测试一下打印')
    self.dr.sleep(1)
    self.dr.input_text('id->ww','刷新')
    # self.dr.reload_page()
    # self.dr.go_forward()
    # self.dr.go_back()
    self.dr.js_execute("window.scrollTo(200,1000);")
    self.dr.sleep(3)
    # self.dr.js_scroll_end()
    # self.dr.js_scroll_top()

def baiduindex04(self):
    self.dr.open_browser("https://www.baidu.com/")
    self.dr.sleep(2)
    # self.dr.click_linktext("新闻")
    self.dr.set_focus_to_element('linktext->新闻')
    self.PySelenium.get_value('id->su', 'id')
    self.dr.get_value('id->su', 'textContent')
    self.dr.get_value('id->su', 'innerHTML')
    self.dr.get_value('id->su', 'outerHTML')
    t = self.dr.get_value('id->su', 'value')
    self.dr.log('测试一下打印')
    self.dr.log(t)
    self.dr.sleep(1)

def baiduindex05(self):
    self.dr.open_browser("https://www.baidu.com/")
    self.dr.sleep(2)
    self.dr.get_value('id->su', 'id')
    self.dr.input_text('id->kw','selenium')
    t = self.dr.get_value('id->su', 'value')
    self.dr.log('测试一下打印')
    self.dr.log(t)
    self.dr.sleep(1)
    self.dr.sleep(3)
    self.dr.log('测试一下调用basepage')