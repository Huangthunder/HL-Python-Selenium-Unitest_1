__author__ = 'Huangthunder'
# coding:utf-8
import unittest
import time
from report.htmltestreport import HTMLTestRunnernew
# from public.common import sendmail
from config import globalparam
from testcase.test_guizeyinqing import IotPage
from testcase.test_guizeyinqing import IotGuize01
from testcase.test_guizeyinqing import IotGuize02
from testcase.test_baidu import TestBaiduIndex01
from testcase.test_baidu import TestBaiduIndex02
from testcase.test_baidu import TestBaiduIndex03
from testcase.test_baidu import TestBaiduIndex04
from testcase.test_baidu import TestBaiduIndex05
from testcase.test_baidu import TestBaiduIndex06
from testcase.test_baidu import TestBaiduIndex07
from testcase.test_taobao import TestTaobao01

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IotPage))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IotGuize01))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IotGuize02))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex01))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex02))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex03))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex04))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex05))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex06))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBaiduIndex07))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTaobao01))
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filePath = 'SeleniumTestReport' + now + '.html'
    reportPath = globalparam.report_path
    fp = open(reportPath + "\\" + filePath, 'wb')
    runner = HTMLTestRunnernew.HTMLTestRunner(stream=fp,
                                              title='自动化巡检报告',
                                              description='详情可见如下列表显示：',
                                              verbosity=2)
    runner.run(suite)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()