import requests
import sys
import json
import datetime

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,ID,Title,Description,PageCount,Excerpt):
		url = 'https://api.github.com/some/endpoint'
		payload = {'ID': ID,
					'Title': Title,
					'Description': Description,
					'PageCount': PageCount,
					'Excerpt': Excerpt,
					'PublishDate':datetime.datetime.now()}
		r = requests.post(url, data=json.dumps(payload))
		print(r)
