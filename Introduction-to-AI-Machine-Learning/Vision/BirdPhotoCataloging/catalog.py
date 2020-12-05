import os
import sys
import requests
from PIL import Image
from io import BytesIO

bird_types = ["tit","thrush","bullfinch","jay"]
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

def check_output_catalogs():
    
    for bird in bird_types:
        if not os.path.isdir('./'+bird):
            os.makedirs('./'+bird)

load_env_variables()
check_output_catalogs()
print(subscription_key)
print(endpoint)

if os.path.isdir('./photos'):
    for file in os.listdir("./photos"):
        if file.endswith(".jpg"):
            print(os.path.abspath(os.path.join("./photos", file)))
else:
    print('ERROR - Can not found photos directory')
    sys.exit()


