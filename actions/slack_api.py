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
		api_token=("xoxp-569934227830-706838758277-726031710261-9d6a78696381f3eea854de12d91f25a9")
		client = slack.WebClient(api_token)

		response = client.chat_postMessage(
        		channel='#general',
        		text="Hello!")


