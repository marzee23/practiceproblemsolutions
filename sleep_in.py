#The parameter weekday is True if it is a weekday, and the parameter 
#vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

def sleep_in(weekday, vacation):
	if not weekday or vacation: 
		print("Yay! You can sleep in!")
	else:
		print("Sucks to suck...gotta wake up early!")
	
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

vacation_Yes_No = input("Are you on vacation?: ")

if vacation_Yes_No == "yes":
	vacation = True
else:
	vacation = False

today = input("What day of the week is it?: ")
weekday = today in weekdays

sleep_in(weekday, vacation)
