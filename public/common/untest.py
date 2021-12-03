__author__ = 'Huangthunder'
# coding:utf-8
import unittest
from public.common.log import Log
from public.common.pyselenium import PySelenium
from config import globalparam

# class UnTest(unittest.TestCase):
#     """
#     这个基类适合所有的测试用例
#     """
#     # 前置步骤
#     driver = globalparam.driver
#     dr = PySelenium(driver)
#     @classmethod
#     def setUpClass(cls):
#         # 调用log日志模块,打印测试用例执行步骤
#         logger = Log()
#         logger.info('############################### START ###############################')
#         cls.dr.maximize_browser_window()
#
#     # 后置步骤
#     @classmethod
#     def tearDownClass(cls):
#         logger = Log()
#         cls.dr.quit_browser()
#         logger.info('###############################  END  ###############################')

class UnTest(unittest.TestCase):
    """
    这个基类适合所有的测试用例
    """
    # 前置步骤
    driver = globalparam.driver
    dr = PySelenium(driver)
    def setUp(self):
        # 调用log日志模块,打印测试用例执行步骤
        logger = Log()
        logger.info('############################### START ###############################')
        self.dr.maximize_browser_window()

    # 后置步骤
    def tearDown(self):
        logger = Log()
        self.dr.quit_browser()
        logger.info('###############################  END  ###############################')