import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_api_key = "OTYY93N4JTKBF1FR"
news_api_key = "a157db9baa2847bc9ba3961866cadec7"

news_api_params = {
    "q": COMPANY_NAME,
    "from": "2022-12-152022-12-16",
    "to": "2022-12-16",
    "sortBy": "popularity",
    "apikey": news_api_key
}

stock_function = "TIME_SERIES_DAILY_ADJUSTED"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo

stock_api_params = {
    "function": stock_function,
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_api_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# print(data)
# print(data["Time Series (Daily)"]['2022-12-16']["4. close"])
data_list = [value for (key, value) in data.items()]
# print(data_list)

yesterday_sum = float(data_list[0]["4. close"])
before_yesterday_sum = float(data_list[1]["4. close"])

# today_sum = float(data["Time Series (Daily)"]["2022-12-16"]["4. close"])
# yesterday_sum = float(data["Time Series (Daily)"]["2022-12-15"]["4. close"])

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# old_sum = 50
# cur_sum = 100
# change_percent = (old_sum - cur_sum)/old_sum * 100
# abs() returns an absolute value of an integer or float number
# print(abs(change_percent))

difference = (yesterday_sum - before_yesterday_sum)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

change_rate = round(abs(difference/yesterday_sum * 100), 2)
# = 4.7

# print(change_rate)



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# https://newsapi.org/v2/everything?q=Apple&from=2022-12-19&sortBy=popularity&apiKey=API_KEY

# news = []

if change_rate > 4.5:
    # print("Get News")
    response = requests.get(url=NEWS_ENDPOINT, params=news_api_params)
    response.raise_for_status()
    articles = response.json()['articles']
    # print(articles)


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{change_rate}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
                        .create(
                             body=article,
                             from_='+14092543489',
                             to='+381616441296'
                         )

    # print(message.sid)

#Optional TODO: Format the message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

