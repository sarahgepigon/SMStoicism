# https://realpython.com/api-integration-in-python/

import requests

resp = requests.get('https://philosophy-quotes-api.glitch.me/quotes/philosophy/Stoicism')
# why do i need the / at the end? 

if resp.status_code != 200:
	#This means something went wrong. 
	raise ApiError('GET /Stoicism {}'.format(resp.status_code))


for quote in resp.json():

	print('{} - {}'.format(quote['quote'], quote['source']))
