from __future__ import print_function
from apiclient import discovery
from bs4 import BeautifulSoup
from datetime import date, timedelta
from oauth2client import client
from oauth2client import tools
from twilio.rest import TwilioRestClient

import datetime
import httplib2
import oauth2client
import os
import requests
import schedule
import time

def get_gcal_credentials():
    home_dir = os.path.expanduser('~')
    cal_credential_dir = os.path.join(home_dir, '.credentials')
    scopes = 'https://www.googleapis.com/auth/calendar.readonly'
    client_secret_file = 'client_secret.json'
    application_name = 'Google Calendar API Python Quickstart'

    if not os.path.exists(cal_credential_dir):
        os.makedirs(cal_credential_dir)
    credential_path = os.path.join(cal_credential_dir, 'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    cal_credentials = store.get()

    if not cal_credentials or cal_credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        flow.user_agent = application_name
        if flags:
            cal_credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            cal_credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return cal_credentials

def get_gcal_events():
    cal_credentials = get_gcal_credentials()
    http = cal_credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    day_start = datetime.datetime.utcnow().isoformat() + 'Z'
    day_offset = timedelta(days=1)
    day_end = (datetime.datetime.now() + day_offset).isoformat() + 'Z'

    eventsResult = service.events().list(
        calendarId='primary', timeMin=day_start, timeMax=day_end, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    return events

def main():

    account_sid = 'ACbf6ce5600928a164340f6f4b086e643d'
    auth_token = '30c506a6affa75080179ae8227a77321'
    client = TwilioRestClient(account_sid, auth_token)
    events = get_gcal_events()
    vcard = True

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        tag = event['summary'][-2:]

        if (tag == '-o'):

            time = str(event['start'].get('dateTime'))[11:16]
            hour = time[:2]
            url = 'http://www.accuweather.com/en/us/university-fl/32826/hourly-weather-forecast/2274320?hour=' + hour

            if vcard:
                url_request = requests.get(url)
                html = url_request.text
                soup = BeautifulSoup(html, 'html.parser')
                rain_percent = (soup.find('div', {'class' : 'data-bar'}).span['style'][8:-2])
                vcard = False

            else:
                rain_percent = (soup.find('div', {'class' : 'data-bar'}).span['style'][8:-2])
            
            text = 'You have \'' + event['summary'][:-3] + '\' scheduled at ' + \
                    time + ', and there is a ' + rain_percent + ' chance of rain.'
            
            client.messages.create(to = '12078389206', from_ = '12078353209', body = text)

def execute():

    schedule.every().minutes.do(main)
    schedule.every().day.at("21:31").do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    execute()