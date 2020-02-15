import logging
import os
import azure.functions as func
from twilio.rest import Client


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    phone_number = req.params.get('phone_number')
    if phone_number:
        try:
            isValidPhoneNumber = client.lookups.phone_numbers(
                phone_number).fetch(type=['carrier'])
            return func.HttpResponse(f"Phone Number is valid {isValidPhoneNumber.carrier}!")
        except:
            return func.HttpResponse("Invalid phone number",
                                     status_code=400)
    else:
        return func.HttpResponse(
            "Please pass a phone_number on the query string",
            status_code=400
        )
