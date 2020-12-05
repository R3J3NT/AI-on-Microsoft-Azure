import os
import sys
import requests

subscription_key = ""
endpoint = ""

def load_env_variables():

    global subscription_key
    global endpoint

    if 'SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['SUBSCRIPTION_KEY']
    else:
        print('ERROR - Set SUBSCRIPTION_KEY environment variable')
        sys.exit()

    if 'ENDPOINT' in os.environ:
        endpoint = os.environ['ENDPOINT']
    else:
        print('ERROR - Set ENDPOINT environment variable')
        sys.exit()
        
load_env_variables()
print(subscription_key)
print(endpoint)