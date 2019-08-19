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
        	'access_token' : 'xoxp-569934227830-706838758277-730251995415-73ec11d4ebd26e275e64e32a2de92a3b'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)



