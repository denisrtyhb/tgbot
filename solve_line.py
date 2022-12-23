def check_format(text):
	return True

def solve_linear_impl(text, state):
    if not check_format(text):
        return "format should be ax + b = c, where a, b and c are integer values"
    text = text.replace(' ', '').replace('=', 'x')
    a, b, c = map(int, text.split('x'))
    c -= b
    if a == 0 and c != 0:
        return "No solutions"
    if a == 0 and c == 0:
        return "All x are solutions"
    return "x = " + str(c / a)