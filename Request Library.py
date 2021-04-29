# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:43:53 2021

@author: Uday Sharma
"""

import requests

url = "https://udaysharma.online/"

response = requests.get(url)
response.content