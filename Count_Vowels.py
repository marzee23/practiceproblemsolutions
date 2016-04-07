#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found

#list function cuts user-inputted string into letters
StringToCount = list(input("Enter a phrase to count the vowels: "))

#make lowercase using list comprehension
[letter.lower() for letter in StringToCount]


#sets can only contain unique values
vowels = {"a", "e", "i", "o", "u"}

def CountVowels (StringToCount):
	NumberOfVowels = 0
	for vowel in StringToCount:
		NumberOfVowels += 1
	print(NumberOfVowels)
	
CountVowels(StringToCount)