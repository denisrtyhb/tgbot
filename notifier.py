import time as tm

class Job:
	dialog_id: int
	text: str
	time: int
	def __init__(self, a1, a2, a3):
		self.dialog_id = a1
		self.text = a2
		self.time = a3

	def ready():
		return False
		return self.time < tm.time()

job_list = [Job(0, 0, 1e20)]

def add_job(id, text, t):
	job_list.append(Job(id, text, tm.time() + t))
	for i in range(len(job_list) - 2, 0, -1):
		if job_list[i].time < job_list[i + 1].time:
			job_list[i], job_list[i + 1] = job_list[i + 1], job_list[i]

def pop_job():
	job_list.pop_back()