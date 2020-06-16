from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib

""" ========== 发送电子邮件 ========== """

'''
def main():
    sender = '1255783906@qq.com'
    receivers = ['1255783906@qq.com', '381172032@qq.com', '18021055980@163.com']
    message = MIMEText('用python发送邮件', 'plain', 'utf-8')
    message['from'] = sender
    message['To'] = receivers
    message['Subject'] = Header('邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, 'xompmrotwjdbhfah')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
'''


# 发送带有附件的邮件
def main():
    # 闯将一个带有附件的邮件消息对象
    message = MIMEMultipart()
    # 创建文本内容
    text_content = MIMEText('利用python自动发送邮件,附件中有好东西，请查收', 'plain', 'utf-8')
    message['Subject'] = Header('自动发送邮件', 'utf-8')
    # 将文本内容添加到消息对象中
    message.attach(text_content)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('D:/小东西/PythonStudy/Python语言基础/70_1104.jpg', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=70_1104.jpg'
        message.attach(txt)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    # 创建SMTP对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全链接
    sender = '1255783906@qq.com'
    receivers = ['18021055980@163.com', '381172032@qq.com']
    # 登录到SMTP服务器，此处不是使用密码登录，而是使用邮件客户端授权码登录
    smtper.login(sender, 'xompmrotwjdbhfah')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送邮件完成!')


if __name__ == '__main__':
    main()
