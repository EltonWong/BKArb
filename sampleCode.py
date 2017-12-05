from binance.client import Client as bClient
from kucoin.client import Client as kClient

#Login Data:
bclient = bClient('GET9kqOyfCz2fiqCDse4wZgwXHqf2BiCEoTUnWqbzTQAiXtASMnz1kmbEEXA3XbE', 'jy79DJ5ljhLaVn080Tg5dwmJcI0iUvZIQTIC48AlV3HupZ3y3B6ZdhyP2s2m1b3z')	
kclient = kClient('5a24a009e0abb849c3933bf4', 'cbb0eae2-e6b5-4b15-91b1-3a2427a02760')

# get market depth
bdepth = bclient.get_order_book(symbol='BNBBTC')
kdepth = kclient.get_order_book('KCS-BTC', limit=50)
