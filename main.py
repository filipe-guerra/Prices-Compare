# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:28:20 2017

@author: filipeguerra
"""

import json
import urllib
import pandas as pd
import matplotlib.pyplot as plt
from BeautifulSoup import *


class exBinance():
    def __init__(self):
        self.url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
        self.bid = ''
        self.ask = ''
        
    def getPrice(self):
        try:
            uh = urllib.urlopen(self.url)
            data = uh.read()
            
            info = json.loads(data)
            aux = float(info['price'])

            return format(aux, '.2f')
        except:
            return '#'
    
    def getBid(self):
        try:
            uh = urllib.urlopen('https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT')
            data = uh.read()
            
            info = json.loads(data)
            bidP = float(info['bidPrice'])
            self.bid = format(bidP, '.2f')
            
            askP = float(info['askPrice'])
            self.ask = format(askP, '.2f')

            return self.bid
        except:
            return '#'
    
    def getAsk(self):
        return self.ask
            
class exKucoin():
    def __init__(self):
        self.url = 'https://api.kucoin.com/v1/BTC-USDT/open/tick'
        self.bid = ''
        self.ask = ''
        
    def getPrice(self):
        try:
            uh = urllib.urlopen(self.url)
            data = uh.read()
            
            info = json.loads(data)
            aux = format((info['data']['lastDealPrice']), '.2f')
            
            self.bid = format((info['data']['buy']), '.2f')
            self.ask = format((info['data']['sell']), '.2f')
            
            return aux
        except:
            return '#'
            
    def getBid(self):
        return self.bid
    
    def getAsk(self):
        return self.ask
            
class exBitfinex():
    def __init__(self):
        self.url = 'https://api.bitfinex.com/v2/ticker/tBTCUSD'
        self.bid = ''
        self.ask = ''
        
    def getPrice(self):
        try:
            uh = urllib.urlopen(self.url)
            data = uh.read()
           
            info = json.loads(data)
            aux = format(info[6], '.2f')
            
            self.bid = format(info[0], '.2f')
            self.ask = format(info[2], '.2f')
            
            # Bitfinex possui apenas 1 casa decimal
            return aux
        except:
            return '#'
            
    def getBid(self):
        return self.bid
    
    def getAsk(self):
        return self.ask
            
            