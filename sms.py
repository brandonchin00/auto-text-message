import email, smtplib, ssl

def send_sms_via_email(number:str, message:str, provider:str, sender_credentials:tuple, subject:str="message was sent by using python", smtp_server="smtp.gmail.com", smtp_port:int): pass