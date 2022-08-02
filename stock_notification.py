import smtplib
from email.message import EmailMessage
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


#Make the program work continuously

api_key = '65CVB0ENIXNFZIEX'


def email_alert(subject, body, to):
  message = EmailMessage()
  message.set_content(body)
  message['subject'] = subject
  message['to'] = to
  
  username = 'achacko10nba@gmail.com'
  message['from'] = username
  password = 'ykoewncjpaqxgjkr'
  
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(username, password)
  server.send_message(message)
  
  server.quit()


ticker = input('Enter stock ticker (ex. AAPL): ')
ticker = ticker.upper()

notification_price = input('Enter the price you want to be notified at (ex. 132.4): ')
ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol = ticker, interval = '1min', outputsize = 'full')
print(data)

# This doesn't work because of the to_excel
#while True:
  #data, meta_data = ts.get_intraday(symbol = ticker, interval = '1min', outputsize = 'full')
  #data.to_excel("output.xlsx")
  #time.sleep(60)

closing_data = data['1. open']

last_close = closing_data[0]

if last_close > float(notification_price):
  email_alert(ticker + ' ALERT', ticker + ' has hit ' + notification_price, '22chackoa@abschools.org')
    