import requests
import sys
import json
from json import dumps
from datetime import datetime
import os
import slack
from st2common.runners.base_action import Action

class slack_api(Action):
	def run(self):
		# url = "https://slack.com/api/chat.postMessage"
		# payload = {"channel": "CGQB47LKV",
  # 					"text": "Hello, from StackStorm!!!"
  # 					}
		# header = {'Content-Type': 'application/json',
		# 	'Accept': 'application/json',
  #       	'Authorization' :'Bearer xoxp-569934227830-706838758277-724784231925-a65485fecc32e290a4f7f3bae4979103'
  #       	}
		# data=json.dumps(payload)
		# r = requests.post(url,data,headers = header)
		# result = r.json()
		# print(result)
		token=os.environ['xoxp-569934227830-706838758277-724784231925-a65485fecc32e290a4f7f3bae4979103']
		client = slack.WebClient(token)

		response = client.chat_postMessage(
        	channel='CGQB47LKV',
        	text="Hello world!")
		print(response.json())


