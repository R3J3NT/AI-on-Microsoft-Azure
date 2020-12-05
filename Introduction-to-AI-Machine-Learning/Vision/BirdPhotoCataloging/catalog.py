import os
import sys
import requests
from PIL import Image
from io import BytesIO

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

def call_custom_vision_API(path):

    analyze_image_data = open(path, "rb").read()
    headers = {'Prediction-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {}
    response = requests.post(endpoint, headers=headers, params=params, data = analyze_image_data)
    response.raise_for_status()
    analysis = response.json()

    return analysis

load_env_variables()
print(subscription_key)
print(endpoint)

analyze_image_path = r''

analysis = call_custom_vision_API(analyze_image_path)
print(str(analysis))
