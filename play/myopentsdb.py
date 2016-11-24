import potsdb
import time
import datetime
import pandas_datareader.data as web

tickers = ['MSFT', 'ABG']
start = datetime.datetime(2011, 04, 15)
end = datetime.datetime(2012, 04, 16)


def import_time_series(ticker):
    df = web.DataReader(ticker, 'yahoo', start, end)
    metrics = potsdb.Client('localhost')
    for index, row in df.iterrows():
        cob = int(time.mktime(index.date().timetuple()) * 1000)
        metrics.send('test.ts.equity.adjclose', row['Adj Close'], timestamp=cob, ticker=ticker)
    metrics.wait()
    metrics.close()


def import_equity_options():
    ticker = web.Options('aapl', 'yahoo')
    data = ticker.get_all_data()


EquityOption( ticker, optionType, expiryType)
 element(expiryDate, Strike)


def run():
    print 'import started...'
    import_time_series()
    print 'import done'


run()




