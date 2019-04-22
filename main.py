# -*- coding: utf-8 -*-

import sys
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import xbmc
import requests
import json

session = requests.Session()

response = session.post('https://mass.mako.co.il/ClicksStatistics/entitlementsServicesV2.jsp', params={'et':'gt', 'lp':'/hls/live/512033/CH2LIVE_HIGH/index.m3u8?as=1','rv':'AKAMAI'})

response_json = json.loads(response.text)
url = 'https://keshethlslive-i.akamaihd.net/hls/live/512033/CH2LIVE_HIGH/index.m3u8?as=1&' + response_json['tickets'][0]['ticket']

xbmc.Player().play(url)
