# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:55:21 2021

@author: Admin
"""

import websocket 
import json

api_key = 'TCJ_4ZUQv782L2eh4yQJ5Pp3pQujT8yAJvSsi2RC'
secret = 'Pt2pFNNiz48aWPv1bU_0Uy6-FgJCndrEkOTMBth4'

url = 'wss://ftx.com/ws/'

msg = {'op': 'subscribe', 'channel': 'orderbooks', 'market': 'BTC-PERP'}

msg = json.dumps(msg)

ws = websocket.create_connection(url)

ws.send(msg)