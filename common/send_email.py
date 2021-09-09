from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from config import read_email_config
import smtplib


def send_email(subject, mail_body, file_names=list()):
    # 获取邮件相关信息
    smtp_server = read_email_config.smtp_server
    port = read_email_config.port
    user_name = read_email_config.user_name
    password = read_email_config.password
    sender = read_email_config.sender
    receiver = read_email_config.receiver
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8") ###邮件内容，content邮件内容，plain为邮件类型，charset为字符集
    msg["Subject"] = Header(subject, "utf-8")   ##邮件主题
    msg["From"] = user_name
    msg["To"] = receiver  #邮件接收人
    msg.attach(body)  #发送邮件内容
    fp = open("C://Users//59621//Pictures//Camera Roll//22.png", 'rb') #正文图片
    images = MIMEImage(fp.read())
    fp.close()
    images.add_header('Content-ID', '<image1>')
    msg.attach(images)
    # 附件:附件名称用英文
    for file_name in file_names:
        att = MIMEText(open(file_name, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = "attachment;filename='report.html'"  # filename为邮件中附件显示的名字
        msg.attach(att)

    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        #smtp.starttls()   ##启动安全传输模式
        smtp.login(user_name, password)
        smtp.sendmail(sender, receiver.split(','), msg.as_string())
    except Exception as e:
        print(e)
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


if __name__ == '__main__':
    subject = "AMI接口测试"  #测试标题
    mail_body = "本邮件由系统自动发出，无需回复！<br>"+" <br>\n" \
                "<br>各位同事，大家好，以下为amirobot自动化测试项目接口测试信息\n" \
                "<br><br>项目名称 ：amirobt \n" \
                "<br>构建编号 ：ami_001 \n " \
                "<br>触发原因 ： \n " \
                "<br>构建状态 ： \n " \
                "<br>构建日志 ： \n " #测试本文
    bobyone = """
        <h3>Hi all</h3>
        <p>本邮件由系统自动发出，无需回复！</p>
        <p>各位同事，大家好，以下为amirobot自动化测试项目接口测试信息。</p>
        <p>项目名称 ：amirobt</p>
        <p>构建编号 ：amirobt</p>
        <p>触发原因 ：amirobt</p>
        <p>构建状态 ：amirobt</p>
        <p>构建日志 ：amirobt</p>
        <p>send by <a herf = "http://v30.edge.customs.k8s.amiintellect.com/#/account/sign-in" >python</a></p>
        <p> 
        <br><img src="cid:image1">superlucy</br> 
        </p>
        <p>
    """
    #receiver = "596211206@qq.com,shudalong@163.com"  # 接收人邮件地址 用逗号分隔
    #file_names = [r'D:\PycharmProjects\AutoTest\result\2020-02-23 13_38_41report.html']
    file_nameone = [r'D:\testdata\gitami\pythonami\AutoTest-master\report\2020_02_24_11_43_24-report.html']
    #send_email(subject, mail_body, receiver, file_names)
    send_email(subject=subject, mail_body=bobyone, file_names=file_nameone)
