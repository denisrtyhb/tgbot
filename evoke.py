import notifier
def evoke_impl(text, state):
	print(state)
	if len(state) == 2:
		state.append(text)
		return "How long do I have to wait to remind you this?"
	if len(state) == 3:
		try:
			t = int(text)
			state.append(t)
		except:
			return "excepted integer"
		state[0] = 0
		print(state)
		notifier.add_job(state[1], state[2], state[3])
		return "got you"