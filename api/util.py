import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta


class Util:
    @staticmethod
    def get_percent(start_data, end_data, name):
        # CREATE TICKER INSTANCE FOR AMAZON
        stock = yf.Ticker(name)
        # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
        end_date = datetime.now().strftime('%Y-%m-%d')

        date = datetime.strptime(start_data, "%Y-%m-%d")
        new_date = date + timedelta(days=1)
        new_date_str = new_date.strftime("%Y-%m-%d")
        print(new_date.strftime("%Y-%m-%d"))
        history = stock.history(start=start_data, end=new_date_str)
        print(history)
        df = pd.DataFrame(history, columns=['Open', 'High', 'Low', 'Close'])

        start_open = 0
        start_High = 0
        start_Close = 0
        start_Low = 0
        for index, row in df.iterrows():
            print('Index: ', index)
            print('Open: ', row['Open'])
            start_open = row['Open']
            print('High: ', row['High'])
            start_High = row['High']
            print('Close: ', row['Close'])
            start_Close = row['Close']
            start_Low = row['Low']

        date = datetime.strptime(end_date, "%Y-%m-%d")
        new_date = date + timedelta(days=1)
        new_date_str = new_date.strftime("%Y-%m-%d")
        print(new_date.strftime("%Y-%m-%d"))
        history = stock.history(start=end_data, end=new_date_str)
        df = pd.DataFrame(history, columns=['Open', 'High', 'Low', 'Close'])
        end_open = 0
        end_High = 0
        end_Close = 0
        end_Low = 0
        for index, row in df.iterrows():
            print('Index: ', index)
            print('Open: ', row['Open'])
            end_open = row['Open']
            print('High: ', row['High'])
            end_High = row['High']
            print('Close: ', row['Close'])
            end_Close = row['Close']
            end_Low = row['Low']

        item = dict()
        item['star_data'] = start_data
        item['Open'] = f'%.2f' % start_open
        item['High'] = f'%.2f' % start_High
        item['Close'] = f'%.2f' % start_Close
        item['Low'] = f'%.2f' % start_Low
        nlist = []
        nlist.append(item)
        item1 = dict()
        item1['end_data'] = end_data
        item1['Open'] = f'%.2f' % end_open
        item1['High'] = f'%.2f' % end_High
        item1['Close'] = f'%.2f' % end_Close
        item1['Low'] = f'%.2f' % end_Low
        nlist.append(item1)
        return nlist

