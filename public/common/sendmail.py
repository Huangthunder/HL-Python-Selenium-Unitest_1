# coding:utf-8

import os
import csv
import time
# 导入smtplib邮件模块
import smtplib
from config import globalparam
from public.common.log import Log
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 测试报告的路径
reportPath = globalparam.report_path
# 测试数据的路径
emailkeyPath = globalparam.data_path
# 调用log日志模块
logger = Log()
# 配置recvaddress收邮件人list
recvaddress = ['huangcius@126.com', '1591310641@qq.com', '1007486707@qq.com', 'huangcius@sina.cn',
               'huanglei@hongwangtech.com']
# 配置发邮件人获取本地csv文件用户名和密码操作
# emailkey = "D:\\HL-Python-Selenium-Untest\\data\\testdata\\emailKey.csv"
emailkey = os.path.join(emailkeyPath, "emailKey.csv")
sendemail = csv.reader(open(emailkey))
for sendaddr in sendemail:
    sendaddr_name = sendaddr[0]
    sendaddr_pswd = sendaddr[1]

class SendMail:
    """
    用于读取最新测试报告后发送测试报告邮件
    """
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '自动化测试巡检报告' + now
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.126.com', 25)
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()