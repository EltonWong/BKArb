from config.py import *
from binance.client import Client as bClient
from kucoin.client import Client as kClient

#Login Data:
bclient = bClient(bKey, bSecret)	
kclient = kClient(kKey, kSecret)

# get market depth
bdepth = bclient.get_order_book(symbol='BNBBTC')
kdepth = kclient.get_order_book('KCS-BTC', limit=50)
