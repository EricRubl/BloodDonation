import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":

    fromaddr = 'iss@zario.go.ro'
    toaddr = 'razvan.pop1998@yahoo.com'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "TATAAA"

    body = "Roade-mi-ai toate carurile să mi le rozi pe rând"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('zario.go.ro', 25)
    server.starttls()
    server.login(fromaddr, "iss")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
