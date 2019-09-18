from st2common.runners.base_action import Action

class execution(Action):
	def run(self,execution_id):
		print("Execution Id is: {}".format(execution_id))