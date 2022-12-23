from time import *
import notifier
def get_year():
	return int(str(localtime(time()).tm_year)[-2:])
def beg_of_year():
	year = get_year()
	beg = strptime(f"1 Jan {year}", "%d %b %y")
	return mktime(beg)

def end_of_year():
	year = get_year() + 1
	end = strptime(f"1 Jan {year}", "%d %b %y")
	return mktime(end)

def percent_to_time(per: int):
	beg = beg_of_year()
	end = end_of_year()
	return beg + (end - beg) * per / 100

def time_to_percent(tm = time()):
	beg = beg_of_year()
	end = end_of_year()
	return (tm - beg) / (end - beg) * 100