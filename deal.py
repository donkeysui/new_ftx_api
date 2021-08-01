# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 01:09:54 2021

@author: Admin
"""

import json
import time
from itertools import zip_longest


url = 'C:/Users/Admin/Desktop/data_future_2'

with open(url) as file:
    raw_text = file.read()
    
l = raw_text.split('\n')

first = json.loads(l[0])['data']

asks = {l[0]:l[1] for l in first['asks']}
bids = {l[0]:l[1] for l in first['bids']}
    
start = time.time()
gg = []
for i in range(160000):
    
    now_data = json.loads(l[i])
    now_bids = now_data['data']['bids']
    now_asks = now_data['data']['asks']
    
    for bid in now_bids:
        if bid[1] != 0.0:
            bids[bid[0]] = bid[1]
            if len(bids.keys())>100:
                print('out bid',min(bids.keys()))
                bids.pop(min(bids.keys()))
        else:
            if bid[0] in bids.keys():
                bids.pop(bid[0])
            
    for ask in now_asks:
        if ask[1] != 0.0:
            asks[ask[0]] = ask[1]
            if len(asks.keys())>100:
                print('out ask',max(asks.keys()))
                asks.pop(max(asks.keys()))
        else:
            if ask[0] in asks.keys():
                asks.pop(ask[0])
                
    gg.append( - max(bids) + min(asks))
            
end = time.time()