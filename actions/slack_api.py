import requests
import sys
import json
from json import dumps
from datetime import datetime

from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self):
		url = "https://slack.com/api/chat.postMessage"
		payload = {"channel": "CLSA44LA0",
  					"text": "Hello, from StackStorm!!!"}
		header = {'Content-Type': 'application/json',
			'Accept': 'application/json',
        	'Authorization' :'Bearer xoxp-569934227830-706838758277-713216048418-17cacc26cf397d395dd6122ef41dd2a9'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)
