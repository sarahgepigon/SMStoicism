#import shortest to longest module
import os
import random
import requests
from twilio.rest import Client

#pulled Stoicism quotes from the internet using a 
#philosophy quotes API in python https://github.com/KaranDahiya/philosophy-quotes-API

# https://realpython.com/api-integration-in-python/

#get all Stoicism quotes from this list of dictionaries
print("Getting philosophy quotes.")

resp = requests.get('https://philosophy-quotes-api.glitch.me/quotes/philosophy/Stoicism')

if resp.status_code != 200:
	#This means something went wrong. 
	raise ApiError('GET /Stoicism {}'.format(resp.status_code))

print("Received (philosophy quotes).")

#pick single quote from API response

random_dictionary = random.choice(resp.json())

text_message = '"{}" - {}'.format(random_dictionary['quote'], random_dictionary['source'])


# send a quote to my phone via Twilio

#"Send an outbound SMS with Python" https://www.twilio.com/docs/sms/quickstart/python#install-python-and-the-twilio-helper-library

print("Sending text message...")

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
#create variables for secure #s
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
my_phone_number = os.environ['MY_PHONE_NUMBER']
client = Client(account_sid, auth_token)

message = client.messages \
				.create(
					body=text_message,
					from_=twilio_phone_number,
					to=my_phone_number
					)

print("Received (text message).")
