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
  					"text": "Hello, from StackStorm!!!",
        		"token":"zMLzUNcdwsbGT1Bb2IlU4y07"}
		header = {'Content-Type': 'application/json',
			'Accept': 'application/json',
        	'Authorization' :'Bearer xoxp-569934227830-706838758277-718284639505-eb50b506a8afcf74aa1ea1ccf8bd85a9'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)
