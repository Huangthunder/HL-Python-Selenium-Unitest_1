__author__ = 'Huangthunder'
from public.variable.guizeyinqingvariable import  guizeyinqing_page_url

def openbrowse(self):
    self.dr.maximize_browser_window()
    self.dr.open_browser(guizeyinqing_page_url)
    self.dr.wait(10)
    self.dr.log(u"开始测试")