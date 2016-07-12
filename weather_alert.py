from __future__ import print_function
from apiclient import discovery
from datetime import date, timedelta
from oauth2client import client
from oauth2client import tools
from twilio.rest import TwilioRestClient

import datetime
import httplib2
import oauth2client
import os
import requests



def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    scopes = 'https://www.googleapis.com/auth/calendar.readonly'
    client_secret_file = 'client_secret.json'
    application_name = 'Google Calendar API Python Quickstart'

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        flow.user_agent = application_name
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():

    account_sid = 'ACbf6ce5600928a164340f6f4b086e643d'
    auth_token = '30c506a6affa75080179ae8227a77321'

    client = TwilioRestClient(account_sid, auth_token)
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    vcard = True
    day_start = datetime.datetime.utcnow().isoformat() + 'Z'
    day_end = date.today()
    day_offset = timedelta(days=1)
    day_end = (datetime.datetime.now() + day_offset).isoformat() + 'Z'

    eventsResult = service.events().list(
        calendarId='primary', timeMin=day_start, timeMax=day_end, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        if (event['summary'][-2:]) == '-o':

            time = str(event['start'].get('dateTime'))[11:16]
            hour = int(time[:2])

            url = 'http://www.accuweather.com/en/us/university-fl/32826/hourly-weather-forecast/2274320?hour=' + str(hour)

            # if vcard:
            #     url_request = requests.get(url)
            #     html = url_request.text
            #     soup = BeautifulSoup(html, 'html.parser')
            #     vcard = False

            # else:
            #     rain_percent = int(soup.find('div', {'class' : 'data-bar'}).span['style'][8:-2])
            
            text = 'You have ' + event['summary'][:-3] + ' scheduled at '
            print (text)
        	# client.messages.create(to = '12078389206', from_ = '12078353209', body = text)

if __name__ == '__main__':
    main()