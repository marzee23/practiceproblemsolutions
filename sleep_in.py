#The parameter weekday is True if it is a weekday, and the parameter 
#vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True
#

def sleep_in(weekday, vacation):
	if not weekday or vacation: 
		print("Yay! You can sleep in!")
	else:
		print("Sucks to suck...gotta wake up early!")
	

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

vacation_Yes_No = input("Are you on vacation?: ")

if "yes" in vacation_Yes_No:
	vacation = True
else:
	vacation = False
	
weekday_Yes_No = input("What day of the week is it?: ")

for weekday in weekday_Yes_No:
	weekday = True
else: 
	weekday = False

sleep_in(weekday, vacation)