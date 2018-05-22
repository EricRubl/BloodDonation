import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":

    from_address = 'iss@zario.go.ro'
    to_address = 'razvan.pop1998@yahoo.com'

    msg = MIMEMultipart()

    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "TATAAA"

    body = "Roade-mi-ai toate carurile să mi le rozi pe rând"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('zario.go.ro', 25)
    server.starttls()
    server.login(from_address, "iss")
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
