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
    
    def getPrice(self):
        try:
            uh = urllib.urlopen(self.url)
            data = uh.read()
            
            info = json.loads(data)
            return info['price']
        except:
            return '#'
