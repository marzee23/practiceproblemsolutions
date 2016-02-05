initial_string = input("Enter a word to check if it is a palindrome: ")

initial_string = initial_string.lower()

reverse_string = initial_string[::-1]

if reverse_string == initial_string:
	print("%s appears to be a palindrome. Kewl beans!" % initial_string)
else:
	print("Nope, %s is definitely not a palindrome." % initial_string)
