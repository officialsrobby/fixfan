import requests
import time
from requests.exceptions import Timeout
a = list(range(211500001,211650000))
i=1
for tokens in a:
	try:
		headers={'User-Agent':'Mozilla/5.0','Authorization':'Token b2bfaff03ca2789dcf2ca1387e7d7d5a321da038'}
		response = requests.post('https://id-api.spooncast.net/users/'+str(tokens)+'/follow/',headers=headers,timeout=1)
		response2 = requests.post('http://id-api.spooncast.net/users/'+str(tokens)+'/fanmessages/',headers=headers,json={'contents':'Fan back dong kk'},timeout=1)
		print(response)
		print(response2)
		print(i)
		i+=1
		print(tokens)
	except Timeout:
		print('ke '+str(tokens)+' gagal')
	except:
		print('error internet')
