import requests
from bs4 import BeautifulSoup
import time
import unicodedata


start = time.time()

# temp_output = open('soup.html', 'w+')
# cal_url = 'https://calendar.google.com/calendar/render#main_7'
# url_request = requests.get(cal_url)
# html = url_request.text
# soup = BeautifulSoup(html, 'html.parser')
# temp_output.write(str(soup))
# temp_output.close()

# html = open('soup.html', 'r')
# soup = BeautifulSoup(html)
# print soup

snowman = unicodedata.lookup('Snowman')

with requests.Session() as c:

	r = requests.get('https://calendar.google.com/calendar/render#main_7')
	headers = dict(r.headers)

	url = 'https://calendar.google.com/calendar/render#main_7'
	c.get(url)
	print c.headers

scope = 'https://www.googleapis.com/auth/calendar'

# weeks = soup.findAll('div', {'class' : 'mv-event-container'})
# .findAll('div', {'class' : 'month-row'})

print start - time.time() 

