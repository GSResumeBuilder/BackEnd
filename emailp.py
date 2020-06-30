import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendMail(reciever_address, resource_name) :
	fromaddr = os.environ.get("SENDER_EMAIL", None)
	password = os.environ.get("PASSWORD", None)
	toaddr = reciever_address
	try:
		msg = MIMEMultipart()

		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Resume Generated Through Resume Builder"

		body = "Below is the attach file of your Resume. Hope we will meet again"

		msg.attach(MIMEText(body, 'plain'))
		filename = os.path.basename("./"+resource_name)
		attachment = open(filename, "rb")

		p = MIMEBase('application', 'octet-stream')

		p.set_payload((attachment).read())

		encoders.encode_base64(p)

		p.add_header('Content-Disposition', "attachment; filename= %s" %resource_name)

		msg.attach(p)

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(fromaddr, password)
		text = msg.as_string()
		s.sendmail(fromaddr, toaddr, text)
		s.quit()

	except:
		print("Mail Not Send")

	return
