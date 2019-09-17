import st2client
import st2client.client
import st2client.commands.action
import st2client.models
import time
import sys

import requests
requests.packages.urllib3.disable_warnings()

from st2common.runners.base_action import Action

class Action_Run(Action):
    def run(self):
        PENDING_STATUSES = [
        st2client.commands.action.LIVEACTION_STATUS_REQUESTED,
        st2client.commands.action.LIVEACTION_STATUS_SCHEDULED,
        st2client.commands.action.LIVEACTION_STATUS_RUNNING,
        st2client.commands.action.LIVEACTION_STATUS_CANCELING
        ]
        server = "192.168.0.4"
        username = "st2admin"
        password = "C1sc0@123"
        ref = "hello_st2.greet"
        run_action(server, username, password, ref)

    def run_action(server, username, password, ref):
        client = st2client.client.Client(base_url="https://{}/".format(server),
                                         auth_url="https://{}/auth/v1".format(server),
                                         api_url="https://{}/api/v1".format(server))

        # login
        token_instance = st2client.models.Token()
        token = client.tokens.create(token_instance, auth=(username, password))
        client = st2client.client.Client(base_url="https://{}/".format(server),
                                         auth_url="https://{}/auth/v1".format(server),
                                         api_url="https://{}/api/v1".format(server),
                                         token=token.token)

        # execute
        execution_instance = st2client.models.LiveAction()
        execution_instance.action = ref
        execution = client.liveactions.create(execution_instance)

        # wait for the execution to finish
        while execution.status in PENDING_STATUSES:
            time.sleep(1)
            sys.stdout.write('.')
            sys.stdout.flush()
            print("waiting for execution {}".format(execution.id))
            execution = client.liveactions.get_by_id(execution.id)

        # execution is done, print out the details
        print(execution.__dict__)
