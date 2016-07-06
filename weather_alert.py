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

	# login_data1 = {'Email':'jltertiaryemailacct', 'requestlocation':'https://accounts.google.com/ServiceLogin?service=cl&passive=1209600&osid=1&continue=https://calendar.google.com/calendar/render&followup=https://calendar.google.com/calendar&scc=1#identifier',
 # 'bgresponse':'!jo2ljaxC8KFMTdeZrsVEMPVqMXkRM0cCAAAAVlIAAAAQmQFrbtdpSXRU25JrGi0w-vibjhxbQSW51wK0yUpn0KbjeC-l2t7Lc892ubmh03ypcpwh8eKJXFfrHenEdiNi39j6ygyRnZtZxNLhJrm9ppzAJX1K9C5oBJTdpCLyerWySRipapolFiF28c7FuDF7859GAlVpSzjdD-0UVjznMhADlVgSRHXYNXy84SOVHMBYwL4HirujKBGPaCGe4uArroKRo_qDqRZxoIVPZ2dfdq3Yprtp0iZ_0ActyAT-GWn6Ehf3U-rRBGbhrBp6C2Jo9I9NgDQ74Py9AXw5IxsSAR-haMXjIf9Wv3XqOX-THj8yA4NTKvWYmuj_8Per3AarCaRXBXrPKEyPzPUZoCcupivRON2feOLoFQXoXHtxIBS6HtzvWsy2jGrrTG2KGdN96Ta8BuC1bZHQaulIVgv8O6tm3z4MquXLjMOBxjdzvcz-m3recoh56TIKyGLx0vQtorGALDqiEaATidHVb1ax',
 # 'Page':'PasswordSeparationSignIn','GALX':'v9TH4pT0dFY','gxf':'AFoagUWQ9DScZrB3ODzj32aOZ1u9WtesCg:1467827779751','continue':'https://calendar.google.com/calendar/render','followup':'https://calendar.google.com/calendar',
 # 'service':'cl','scc':'1','osid':'1','_utf8':snowman,'pstMsg':'1','checkConnection':'youtube:144:1','checkedDomains':'youtube','rmShown':'1'}
	# c.post(url, data=login_data1)
	# page = c.get('https://calendar.google.com/calendar/render#main_7')
	# this = open('this.html', 'w+') 
	# this.write(page.content)
	# this.close()

# google-accounts-signin:email="jltertiaryemailacct@gmail.com", sessionindex=0, obfuscatedid="113572385592190371503"

# Email:jltertiaryemailacct
# requestlocation:https://accounts.google.com/ServiceLogin?service=cl&passive=1209600&osid=1&continue=https://calendar.google.com/calendar/render&followup=https://calendar.google.com/calendar&scc=1#identifier
# bgresponse:!jo2ljaxC8KFMTdeZrsVEMPVqMXkRM0cCAAAAVlIAAAAQmQFrbtdpSXRU25JrGi0w-vibjhxbQSW51wK0yUpn0KbjeC-l2t7Lc892ubmh03ypcpwh8eKJXFfrHenEdiNi39j6ygyRnZtZxNLhJrm9ppzAJX1K9C5oBJTdpCLyerWySRipapolFiF28c7FuDF7859GAlVpSzjdD-0UVjznMhADlVgSRHXYNXy84SOVHMBYwL4HirujKBGPaCGe4uArroKRo_qDqRZxoIVPZ2dfdq3Yprtp0iZ_0ActyAT-GWn6Ehf3U-rRBGbhrBp6C2Jo9I9NgDQ74Py9AXw5IxsSAR-haMXjIf9Wv3XqOX-THj8yA4NTKvWYmuj_8Per3AarCaRXBXrPKEyPzPUZoCcupivRON2feOLoFQXoXHtxIBS6HtzvWsy2jGrrTG2KGdN96Ta8BuC1bZHQaulIVgv8O6tm3z4MquXLjMOBxjdzvcz-m3recoh56TIKyGLx0vQtorGALDqiEaATidHVb1ax
# Page:PasswordSeparationSignIn
# GALX:v9TH4pT0dFY
# gxf:AFoagUWQ9DScZrB3ODzj32aOZ1u9WtesCg:1467827779751
# continue:https://calendar.google.com/calendar/render
# followup:https://calendar.google.com/calendar
# service:cl
# scc:1
# osid:1
# _utf8:
# pstMsg:1
# checkConnection:youtube:144:1
# checkedDomains:youtube
# rmShown:1

# Page:PasswordSeparationSignIn
# GALX:1QFq8AeQGhQ
# gxf:AFoagUW-n4ROpT1QfjYBVh3pYUb6hoM-Cw:1467827628126
# continue:https://calendar.google.com/calendar/render
# followup:https://calendar.google.com/calendar
# service:cl
# scc:1
# osid:1
# ProfileInformation:APMTqunZqqLX4Dw5ywxVorARViQbkdD9_69bDfspDBbMaKK4r6gBx8yLgIuTgMnMzgBotDsJxGdpZGwhKMZZB2IYTC3slAx8TDh8GjW1xFuusPg-U2xfGBw
# _utf8:
# bgresponse:!srGlsZBC1Ur6PzLJO8tES64G-Z2A470CAAAAXlIAAAAXmQF6S0wdaeb-JbnnSfNsCPGWISx9h_LIxcy6UUccafir-ga9auNnkXhhimkbtzIsFdetkUBqiKzFwn99Y0FZnl3_147g2AZEg7rbAKlH7Non_R9840IHuoGUI1VZHkp69eIpBNTwMZF6x-DwR0OxjfVTEmZN40hCFjicZUoW3gebviRpv8BqCd3Ejqa_LBsZAActLP2Y0Ls9qUSf95MiMoQnQF5eREp4uUln4w2FkYoMESWQZ3w3qzdXdIWed0Ks92M3AR9rver-x9URO9YlLp5SMGqkyWQwoK2zHMNUDHdlXNRPYiFz8JdEeNseQ1-VJW-VlXSMilXy5MhOkNk8WVhRRLU09URxD_DVWafKEEcbIW7aS-k2Z6-lWRW9ncosN5zDXqDxhHafE7d6b8edxyVpnZ_olFzOHDC0VG9xYUETNwL8iN6WXZWXii1RwXAdPWikx0nA9jrDMOsEX0reMjlYZk67AhvuNKLj-bxRb89pYADBO4ckVu9TnsUp
# pstMsg:1
# dnConn:
# checkConnection:youtube:153:1
# checkedDomains:youtube
# identifiertoken:
# identifiertoken_audio:
# identifier-captcha-input:
# Email:jltertiaryemailacct
# Passwd:
# PersistentCookie:yes
# rmShown:1


# weeks = soup.findAll('div', {'class' : 'mv-event-container'})
# .findAll('div', {'class' : 'month-row'})

print start - time.time() 

