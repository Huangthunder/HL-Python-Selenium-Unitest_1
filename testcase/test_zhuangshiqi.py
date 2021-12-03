# coding:utf-8
# from public.common.publicfunction import screen
# from selenium import webdriver
# # from public.common import pyselenium
# from config import globalparam


# # 截图功能
# def get_screen(self):
#     '''截图'''
#     import time
    # current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # print(current_time)
    # print(current_time1)
    # imagePath = current_time + '.png'
    # # 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
    # pic_path = 'D:\\Huangcius-Python-Selenium\\report\\image\\' + '\\' + imagePath  #设置存储图片路径，测试结果图片可以按照每天进行区分
    # globalparam.driver.get_screenshot_as_file(pic_path)
#     current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     # current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
#     reportPath = globalparam.img_path
#     imagePath = current_time + '.png'
#     # 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
#     pic_path = reportPath + '\\' + imagePath  # 设置存储图片路径，测试结果图片可以按照每天进行区分
#     self.dr.save_screenshot(pic_path)

# # 自动截图装饰器
# def screen(func):
#     '''截图装饰器'''
#     def inner(*args, **kwargs):
#         try:
#             f = func(*args, **kwargs)
#             return f
#         except:
            # get_screen()  # 失败后截图
    # return inner


# @screen
# def search(self):
#     self.dr.open_browser("https://www.baidu.com")
#     self.dr.maximize_browser_window()
#     self.dr.input_text("id->kw11","python")  # 此行运行失败的
#     self.dr.click_element('id->su')
#     self.dr.quit_browser()

# search()  # 执行search