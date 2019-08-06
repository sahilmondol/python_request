import requests
import sys
import json
from json import dumps
from datetime import datetime

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,ID,Title,Description,PageCount,Excerpt):
		url = 'http://fakerestapi.azurewebsites.net/api/Books'
		time = str(datetime.utcnow())
		payload = {'ID': ID,
					'Title': Title,
					'Description': Description,
					'PageCount': PageCount,
					'Excerpt': Excerpt,
					'PublishDate':time}
		header = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
		}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)
