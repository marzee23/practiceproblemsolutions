#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found
import sys

def count_each_vowel(in_string):
    vowels = {"a", "e", "i", "o", "u"}
    vowel_counts = dict()
    for letter in arg_string:
        if letter in vowels:
            new_count = vowel_counts.get(letter, 0) + 1
            vowel_counts[letter] = new_count
    return vowel_counts

def tabulate_vowel_count(vowel_counts):
    return sum(vowel_counts.values())

if __name__ == '__main__':
    arg_string = " ".join(sys.argv[1:])
    vowel_counts = count_each_vowel(arg_string)
    total_vowels = tabulate_vowel_count(vowel_counts)
    print("There are", total_vowels, "vowels in '{}'".format(arg_string))
    for vowel in sorted(vowel_counts.keys()):
        print("There are", vowel_counts.get(vowel, 0), vowel.upper(), "'s!")
