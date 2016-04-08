#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found
import sys
arg_string = " ".join(sys.argv[1:])

vowels = {"a", "e", "i", "o", "u"}
vowels_in_string = 0
vowel_counts = dict()

for letter in arg_string:
    if letter in vowels:
        vowels_in_string += 1
        new_count = vowel_counts.get(letter, 0) + 1
        vowel_counts[letter] = new_count

print("There are", vowels_in_string, "vowels in '{}'".format(arg_string))
for vowel in sorted(list(vowels)):
    print("There are", vowel_counts.get(vowel, 0), vowel.upper(), "'s!")
