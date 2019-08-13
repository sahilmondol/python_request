import requests
import sys
import json
from json import dumps
from datetime import datetime

from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self, url):
		url1 = 'https://slack.com/api/chat.postMessage'
		payload = {'channel': 'xoxp-569934227830-706838758277-708758560834-9f695114116fbb7339f5e4da466fdf0c',
  					'text': 'Hello, from StackStorm!!!'}
		header = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
		}
		data=json.dumps(payload)
		r = requests.post(url1,data,headers = header)
		result = r.json()
		print(result)
