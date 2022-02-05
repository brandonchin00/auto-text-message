import email, smtplib, ssl
from providers import PROVIDERS
import requests

city = "New York City"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5b7c0160aba9fac1ce81db90f1ed4411&units=metric'.format(city)
res = requests.get(url)
data = res.json()

temp = data['main']['temp'] #temperature 
wind_speed = data['wind']['speed'] #windspeed
feels = data['main']['feels_like'] #what the temperature feels like

message1 = (
    f"Good Morning Brandon."
    f" Today's temperature is {temp} celsius but it feels like {feels} celsius."
    f" Current wind speed is {wind_speed}."
    f" Please dress accordingly."
)

def send_sms_via_email(
    number: str, 
    message: str, 
    provider: str, 
    sender_credentials: tuple, 
    subject: str = "Via Python", 
    smtp_server: str = "smtp.gmail.com", 
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():
    number = "6465205900" #6178746880
    message = message1
    provider = "T-Mobile"

    sender_credentials = ("brandonzchin@gmail.com", "wmdf gsfx rybt mjew")
        
    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == "__main__":
    main()