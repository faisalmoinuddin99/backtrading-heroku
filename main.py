from datetime import datetime
import backtrader as bt
import requests
from strategies import TestStrategy
from strategies import SmaCross


strategy = SmaCross
cerebro = bt.Cerebro()
cerebro.broker.setcash(5000.0)
cerebro.addstrategy(strategy)

data = bt.feeds.YahooFinanceData(dataname="INFY.csv", fromdate=datetime(2015,1,1),
                                 todate=datetime(2021,1,1))

cerebro.adddata(data)
print(cerebro.run())
cerebro.plot()