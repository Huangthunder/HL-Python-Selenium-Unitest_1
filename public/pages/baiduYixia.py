__author__ = 'Huangcius-HL'

from public.common import basepage

class baiDu(basepage.Page):
    def baidu(self):
        self.dr.open_browser(self,"https://www.baidu.com/")
        self.dr.input_text('id->kw',"ceshi")
        self.dr.click_element('id->dddu')