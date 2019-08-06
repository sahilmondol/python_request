import requests
import sys
import json
from json import dumps
from datetime import datetime

from st2common.runners.base_action import Action

class requests_api(Action):
	def run(self,ID,Title,Description,PageCount,Excerpt):
		url = 'https://api.github.com/some/endpoint'
		time = str(datetime.utcnow())
		payload = {'ID': ID,
					'Title': Title,
					'Description': Description,
					'PageCount': PageCount,
					'Excerpt': Excerpt,
					'PublishDate':time}
		r = requests.post(url, data=json.dumps(payload))
		print(r)
