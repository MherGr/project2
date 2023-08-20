import subprocess
import smtplib
from email.mime.text import MIMEText

sender_email = "mhergrig03@gmail.com"
sender_password = "hgoulldvmqqbiwoz"
receiver_email = "mhergrig03@gmail.com"


def send_email(new_ip):
    subject = "IP address detected"
    body = f"IP address detect: {new_ip}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['FROM'] = sender_email
    msg['TO'] = receiver_email


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

ip_address = "/home/kali/ipaddresses.log"
with open(ip_address, "r") as log_file:
    lines = log_file.readlines()
    if lines:
        new_ip = lines[-1]
        send_email(new_ip)
