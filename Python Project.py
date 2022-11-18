import yfinance as y
import matplotlib.pyplot as m

m.style.use('fivethirtyeight')

a=input('Enter Stock : ').upper()

# import data
graph = y.Ticker(a+'-USD')

data = graph.history(period='1y')

data['SMA5'] = data['Close'].rolling(5).mean()
data['SMA15'] = data['Close'].rolling(15).mean()

# removing all the NULL values using
data.dropna(inplace=True)

# data[['Close', 'SMA5','SMA15']].plot(figsize=(16, 8),color=['black','g','r'],linewidth=10)
x = data['Close']
y1 = data['SMA5']
y2 = data['SMA15']

m.plot(x,label='Close',linewidth=2,color='black')
m.plot(y1,label='SMA5',linewidth=1,color='green')
m.plot(y2,label='SMA15',linewidth=1,color='red')

m.xlabel('Date')
m.ylabel('Price in USD')
m.title(a+' Stock in 1 Year Period')
m.legend(loc='upper right')

m.show()

print(data)
