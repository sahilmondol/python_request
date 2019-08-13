import requests
import sys
import json
from json import dumps
from datetime import datetime

from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self):
		url = "https://slack.com/api/chat.postMessage"
		payload = {"channel": "CGQB47LKV",
  					"text": "Hello, from StackStorm!!!"}
		header = {'Content-Type': 'application/json',
			'Accept': 'application/json',
        	'Authorization' :'Bearer xoxp-569934227830-706838758277-724192098436-0a37281e9e840fe25677eb91f7d8f029'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)
