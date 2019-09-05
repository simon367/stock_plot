import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

print('This program will plot stock prices for you, just follow the prompts as they come...')
date_entry = input('Enter the start date for your plot YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
start = dt.datetime(year, month, day)
date_entry2 = input('Enter the end date for your plot YYYY-MM-DD format: ')
year, month, day = map(int, date_entry2.split('-'))
end = dt.datetime(year, month, day)


ticker = input('Enter the ticker you wish to plot: ')

while True:
     query = input('Do you want to compare it to the market index? ')
     first_l = query[0].lower()
     if query == '' or not first_l in ['y','n']:
        print('Please answer with yes or no!')
     else:
        break
if first_l == 'y':
    df = web.DataReader([ticker, 'SPY'],'yahoo',start,end)
    df['Adj Close'].plot()
    plt.show()
if first_l == 'n':
    df = web.DataReader([ticker],'yahoo',start,end)
    df['Adj Close'].plot()
    plt.show()
