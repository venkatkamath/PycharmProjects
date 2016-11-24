import pandas_datareader.data as web
import datetime
import time

start = datetime.datetime(2015, 11, 11)
end = datetime.datetime(2016, 11, 10)

df =web.DataReader("F", 'yahoo', start, end)

for index, row in df.iterrows():
    time1 = int(time.mktime(index.date().timetuple()) * 1000)
    print time1, row['Adj Close']