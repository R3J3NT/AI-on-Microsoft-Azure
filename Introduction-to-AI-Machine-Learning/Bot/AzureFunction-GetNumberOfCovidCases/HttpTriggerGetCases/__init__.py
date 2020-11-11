import logging

import azure.functions as func

import requests
import json
from datetime import datetime, timedelta


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    now = datetime.now()
    yesterday = now - timedelta(days=1)

    dt_now = now.strftime("%Y-%m-%dT00:00:00Z")
    dt_yesterday = yesterday.strftime("%Y-%m-%dT00:00:00Z")

    response = requests.get("https://api.covid19api.com/country/poland/status/confirmed?from=" + dt_yesterday +"&to="+ dt_now)

    casesNumber = 0

    cases = json.loads(response.text)
    if cases[0]['Cases']:
        casesNumber = cases[0]['Cases']

    return func.HttpResponse(
        str(casesNumber),
        status_code=200
    )
