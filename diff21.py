n = int(input("Pick a number: "))

def diff21(n):
	
	if n <= 21:
		print(21 - n)
	else:
		print((n-21) * 2)
	
diff21(n)