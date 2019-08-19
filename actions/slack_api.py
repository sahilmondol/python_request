import requests
import sys
import json
from json import dumps
from datetime import datetime
from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self,message):
		url = "https://slack.com/api/chat.postMessage"
		payload = {"channel": "CGQB47LKV",
  					"text": message
  					}
		header = {'Content-Type': 'application/json',
			'Accept': 'application/json',
        	'Authorization' : '569934227830.719077425731.2d0b362092a66b528cbfa5b9994067784bde3a43f0b46b5973822820d53814c3'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)



