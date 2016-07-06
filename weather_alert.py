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





# weeks = soup.findAll('div', {'class' : 'mv-event-container'})
# .findAll('div', {'class' : 'month-row'})

print weeks
print start - time.time() 