import requests
from bs4 import BeautifulSoup
import time

start = time.time()

temp_output = open('soup.html', 'w+')
cal_url = 'https://calendar.google.com/calendar/render#main_7'
url_request = requests.get(cal_url)
html = url_request.text
soup = BeautifulSoup(html, 'html.parser')
temp_output.write(str(soup))
temp_output.close()


woah = {"installed":{"client_id":"605395481450-1g7mt811gdc48q4mcfp42so0b6osr9v1.apps.googleusercontent.com","project_id":"weather-alert-1365","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"sGsB9zLLyU-2a0wGottdYbx9","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}

# client_id = '605395481450-1g7mt811gdc48q4mcfp42so0b6osr9v1.apps.googleusercontent.com'
# client_secret = 'sGsB9zLLyU-2a0wGottdYbx9'

scope = 'https://www.googleapis.com/auth/calendar'

# weeks = soup.findAll('div', {'class' : 'mv-event-container'})
# .findAll('div', {'class' : 'month-row'})

print weeks
print start - time.time() 