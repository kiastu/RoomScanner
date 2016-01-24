import requests

'''
Before using, create a config folder and a file named credentials.py.
Create a Credentials class and put your google server api key there under SERVER_KEY
'''
from config.credentials import Credentials

parameters = {}
parameters['key'] = Credentials.SERVER_KEY
parameters['origins'] = "Sunnyvale, California"
parameters['destinations'] = "Los Angeles, California"

testRequest = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json', params = parameters)

print(testRequest.text)
print(testRequest.json)