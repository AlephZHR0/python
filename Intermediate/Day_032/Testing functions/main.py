import smtplib
import datetime as dt
import pandas
from random import choice

MY_EMAIL = "mail@example.com"
PASSWORD = "1234567890"


now = dt.datetime.now()
with open("quotes.txt") as quotes_file:
    data = quotes_file.readlines()
    quote = choice(data)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="another_mail@example.com",
            msg="Subject: New quote\n\n{}".format(quote)
       )