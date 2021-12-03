__author__ = 'Huangthunder'
# coding=utf-8
import time
import unittest
from report.htmltestreport import HTMLTestRunnernew
from config import globalparam
from public.common import sendmail

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    # now = time.strftime('%Y-%m-%d %H_%M_%S')
    # reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filePath = 'SeleniumTestReport' + now + '.html'
    reportPath = globalparam.report_path
    # fp = open("D:\HL-Python-Selenium框架\report\testreport\\%s" % filePath, 'wb')
    with open(reportPath + "\\" + filePath, 'wb') as f:
        runner = HTMLTestRunnernew.HTMLTestRunner(
            stream=f,
            title='自动化巡检报告',
            description='详情可见如下列表显示：'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()

if __name__=='__main__':
    run()