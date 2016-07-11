from __future__ import print_function

import datetime
import httplib2
import oauth2client
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from twilio.rest import TwilioRestClient
from datetime import date, timedelta

ACCOUNT_SID = 'ACbf6ce5600928a164340f6f4b086e643d'
AUTH_TOKEN = '30c506a6affa75080179ae8227a77321'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """
    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    day_start = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
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
        	print ('You have', event['summary'][:-3], 'scheduled at', str(event['start'].get('dateTime'))[11:16])

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	client.messages.create(
	    to = '12078389206',
	    from_ = '12078353209',
	    body = 'Marcelo Huertas = POINT GOD',
	)

if __name__ == '__main__':
    main()