import requests
import sys
import json
from json import dumps
from datetime import datetime
from st2common.runners.base_action import Action

class slack_api_retrieve(Action):
	def run(self,time):
		#time_taken = time
		resp = requests.get('https://slack.com/api/conversations.history?token=xoxp-569934227830-706838758277-714640004003-28ab51eaee2bfb43bcd286185cdfc594&channel=CGQB47LKV&latest={0}&limit=1&inclusive=true'.format(timestamp))
		data = resp.json()
		message = data['messages']
		print(message)

