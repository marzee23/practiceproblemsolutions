#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found

#list function cuts user-inputted string into letters and make lowercase
StringToCount = list(input("Enter a phrase to count the vowels: ").lower())

#sets can only contain unique values
vowels = {"a", "e", "i", "o", "u"}

VowelsInString = []
	
for letter in StringToCount:
	if letter in vowels:
		VowelsInString.append(letter)

print("There are",len(VowelsInString), "vowels in that text!")
