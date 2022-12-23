notes = dict() # id -> {dict(), tag -> [notes list]}

def note_impl(text, state):
	if len(state) == 2:
		state.append(text)
		return "Now write your text"
	elif len(state) == 3:
		state.append(text)
		if state[1] not in notes:
			notes[state[1]] = dict()
		if state[2] not in notes[state[1]]:
			notes[state[1]][state[2]] = []
		notes[state[1]][state[2]].append(state[3])
		state[0] = 0
		return f"Note with tag {state[2]} successfully created"

def note_statistics_impl(text, state):
	if len(state) == 2:
		if state[1] not in notes or text not in notes[state[1]]:
			return "no notes with such tag"
		state[0] = 0
		return "You have several notes:\n" + '\n'.join(notes[state[1]][text])