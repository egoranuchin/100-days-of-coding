import smtplib
import datetime as dt
import random




my_email = "my_email"
password = "app_password"



# now = dt.datetime.now()
# year = now.year
# # if year == 2022:
#     # print("Wear face mask")
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)


now = dt.datetime.now()

with open("quotes.txt", mode="r") as file:
    # print(file)
    text = file.readlines()
    # print(text)
    # quotes_list = [line.split(" \n") for line in text]
    # print(quotes_list)

random_quote = random.choice(text)
print(random_quote)

if now.weekday() == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="supermoonfire@gmail.com", msg=f"Subject:Hello\n\n{random_quote}")

