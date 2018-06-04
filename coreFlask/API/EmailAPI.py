import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_forgot_password_email(user_email, token):
    gmail_user = 'flow.blood.donation@gmail.com'
    gmail_password = 'frigider'

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(gmail_user, gmail_password)
    header = 'To:' + user_email + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
    msg = header + '\n To reset your password, access the following link: ' \
                   'http://zario.go.ro:5000/forgot?token=%s \n\n' \
                   % token
    smtp_server.sendmail(gmail_user, user_email, msg)
    print('done!')
    smtp_server.close()


if __name__ == "__main__":
    # send_forgot_password_email('eric@zario.go.ro', 'asdzxcqweasd56yhbvfrt6u')
    pass
