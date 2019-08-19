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
        	'access_token' : '569934227830.732642180198.a002ec897ba43768097edd4939fa1a110f1bba924d12baf725e626a20fbdcc1f'
        	}
		data=json.dumps(payload)
		r = requests.post(url,data,headers = header)
		result = r.json()
		print(result)



