# coding=utf-8

from public.common import basepage

class BaiduIndexPage(basepage.Page):
    def into_baidu_page(self):
        """打开百度首页"""
        self.dr.open_browser('http://www.baidu.com')

    def input_search_key(self,values):
        """输入搜索关键词"""
        self.dr.input_text('id->kw',values)
        # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(current_time)
        # print(current_time1)
        # imagePath = current_time + '.png'
        # # 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
        # pic_path = 'D:\\Huangcius-Python-Selenium\\report\\image\\' + '\\' + imagePath  #设置存储图片路径，测试结果图片可以按照每天进行区分
        # self.dr.save_screenshot(pic_path)

    def click_search_button(self):
        """点击搜索按钮"""
        self.dr.click_element('id->su')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()