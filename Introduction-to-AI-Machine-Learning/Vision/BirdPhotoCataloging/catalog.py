import os
import sys
import requests
import time
from PIL import Image
from io import BytesIO

bird_types = ["tit", "thrush", "bullfinch", "jay", "need-verification"]
probability_level = 0.98
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
    headers = {'Prediction-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {}
    response = requests.post(endpoint, headers=headers,
                             params=params, data=analyze_image_data)
    response.raise_for_status()
    analysis = response.json()

    return analysis


def check_output_catalogs():
    for bird in bird_types:
        if not os.path.isdir('./'+bird):
            os.makedirs('./'+bird)


def move_photo(from_path, to_path):
    os.rename(from_path, to_path)


load_env_variables()
check_output_catalogs()

if os.path.isdir('./photos'):
    for file in os.listdir("./photos"):
        if file.endswith(".jpg"):
            print('[CATALOGING] File: %12s' % file, end='')
            absolute_path = os.path.abspath('./')
            path = os.path.abspath(os.path.join("./photos", file))
            analysis = call_custom_vision_API(path)
            probability_result = analysis["predictions"][0]['probability']
            tag_name_result = analysis["predictions"][0]['tagName']

            if probability_result > probability_level:
                move_photo(path, absolute_path+'\\'+tag_name_result+'\\'+file)
                print(' -> [CUSTOM VISION] response: %10s' % tag_name_result + " %10s"
                      % str(probability_result) + ' -> [MOVE] Catalog: \\'+tag_name_result)
            else:
                move_photo(path, absolute_path+'\\need-verification\\'+file)
                print(' -> [MOVE] Catalog: need-verification')
            time.sleep(1)  # F0 tier restriction - maximum 2TPS

else:
    print('ERROR - Can not found photos directory')
    sys.exit()
