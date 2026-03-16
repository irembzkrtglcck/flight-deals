import smtplib
from dotenv import load_dotenv
import os

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_EMAIL_PASSWORD"]

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject: Cheap flight found! Ucuz ucus bulundu! \n\n{message}".encode("utf-8")
            )