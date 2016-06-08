#!/usr/bin/env python3
from lxml import html
import requests


def get_usd_price():
	"""
	Returning Krpyton current price in USD as float
	Using coinmarketcap scrapping
	Kinda hardcoded and dirty
	"""

	
	url = "https://coinmarketcap.com/currencies/krypton/"
	xpath = "//span[@class='text-large']/text()"
	
	page = requests.get(url)
	tree = html.fromstring(page.content)	
	res  = tree.xpath(xpath) 
	
	usd = float(res[0].replace("$", "") )
	return usd
def get_difficulty():
	"""
	Returns current difficulty as float using official API
	"""
	url = "http://explorer.krypton.rocks/api.php?page=difficulty"
	page = requests.get(url)
	difficulty = float(page.content.decode('utf-8'))
	
	return difficulty

def get_block_time():
	"""
	Returns block time
	Currently hardcoded
	"""
	return 0.25

