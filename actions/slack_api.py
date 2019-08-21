import requests
import sys
import json
from json import dumps
from datetime import datetime
from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self,message,token):
		url = "https://slack.com/api/chat.postMessage"
		payload = {"channel": "CGQB47LKV",
  					"text": message
  					}
		header = {'Content-Type': 'application/json',
			'Accept': 'application/json',
        	'Authorization' : token
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)



