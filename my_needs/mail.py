# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
textfile="sample.txt"
with open(textfile,"w") as fp:
    fp.write("test mail :")

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = 'balakrishna.maduru@noodle.ai'
msg['To'] = 'balakrishna.maduru@noodle.ai'

# Send the message via our own SMTP server.
with smtplib.SMTP() as s:
    s.connect("localhost")
    s.login('balakrishna.maduru@noodle.ai', '')
    s.send_message(msg)
