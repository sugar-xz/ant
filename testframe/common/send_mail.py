#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Sugar'

import os
import smtplib
import threading
from testframe.common.logger import Log
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from testframe.common.config_util import ConfigUtil


class SendEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if SendEmail.email is None:
            SendEmail.mutex.acquire()
            SendEmail.email = Email()
            SendEmail.mutex.release()
        return SendEmail.email


class Email:
    def __init__(self):
        # --------- 读取config.ini配置文件 ---------------
        self.HOST = ConfigUtil.get_ini("user", "HOST_SERVER")
        self.HOST = ConfigUtil.get_ini("user", "HOST_SERVER")
        self.SENDER = ConfigUtil.get_ini("user", "FROM")
        RECEIVERs = ConfigUtil.get_ini("user", "TO")
        self.USER = ConfigUtil.get_ini("user", "user")
        self.PWD = ConfigUtil.get_ini("user", "password")
        self.SUBJECT = ConfigUtil.get_ini("user", "SUBJECT")
        self.RECEIVER = []
        for n in str(RECEIVERs).split(","):
            self.RECEIVER.append(n)

        self.logger = Log.get_log()
        self.report = Log.get_report_path()

    def send_mail(self):
        """
        定义发送邮件
        :param file_new:
        :return: 成功：打印发送邮箱成功；失败：返回失败信息
        """

        # report是否存在判断
        if not self.check_file():
            self.logger.error("Test report does not exist! (`AUTO_LOG_WRITE` should be True)")
            return

        msg = MIMEMultipart('related')
        msg['Subject'] = self.SUBJECT
        msg['from'] = self.SENDER
        msg['to'] = ";".join(self.RECEIVER)

        # mail content
        with open(self.report, "rb") as f:
            mail_body = f.read()
        msg_text = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_text)

        # mail attachment
        att = MIMEText(mail_body, 'html', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename="TestingReport.html"'
        msg.attach(att)
        f.close()

        try:
            server = smtplib.SMTP()
            server.connect(self.HOST)
            server.starttls()
            server.login(self.USER, self.PWD)
            server.sendmail(msg['from'], msg['to'], msg.as_string())
            server.quit()
            print("邮件发送成功！")
        except Exception as e:
            print("失败: " + str(e))

    def check_file(self):
        """
        check test report
        :return:
        """
        if os.path.isfile(self.report) and not os.stat(self.report) == 0:
            return True
        else:
            return False

    def new_report(self, testreport):
        """
        生成最新的测试报告文件
        :param testreport:
        :return:返回文件
        """
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
        file_new = os.path.join(testreport, lists[-1])
        return file_new

if __name__ == '__main__':
    from config.setting import BASE_DIR
    pa_ss = BASE_DIR + '/export/htmlReport/2019-04-22 17_30_09_result.html'
    # mail content
    msg = MIMEMultipart('related')

    with open(pa_ss, "rb") as f:
        mail_body = f.read()
    msg_text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_text)
    print(mail_body)
    # Email().send_mail()
