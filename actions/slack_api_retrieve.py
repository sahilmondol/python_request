import requests
import sys
import json
from json import dumps
from datetime import datetime
from st2common.runners.base_action import Action

class slack_api_retrieve(Action):
	def run(self,token,time):
		#time_taken = time
		resp = requests.get('https://slack.com/api/conversations.history?token={0}&channel=CGQB47LKV&latest={1}&limit=1&inclusive=true'.format(token,timestamp))
		data = resp.json()
		message = data['messages']
		print(message)

