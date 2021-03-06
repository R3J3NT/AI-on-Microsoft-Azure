import requests
import json
from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)

dt_now = now.strftime("%Y-%m-%dT00:00:00Z")
dt_yesterday = yesterday.strftime("%Y-%m-%dT00:00:00Z")

response = requests.get("https://api.covid19api.com/country/poland/status/confirmed?from=" + dt_yesterday +"&to="+ dt_now)

cases = json.loads(response.text)
if cases[0]['Cases']:
    print(cases[0]['Cases'])

