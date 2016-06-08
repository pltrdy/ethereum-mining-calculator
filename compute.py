import requests
import json
import sys
import time

from api import *

blockTime = get_block_time()
difficulty = get_difficulty()
usd_price = get_usd_price()

data = {
    'blockTime': blockTime,
    'difficulty': difficulty,
    'priceUsd': usd_price,
    'lastUpdate': time.time(),
}
file(sys.argv[1], 'w').write('ethereumStats = ' + json.dumps(data) + ';')
