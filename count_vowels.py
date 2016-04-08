#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found
import sys
import unittest

vowels = {"a", "e", "i", "o", "u"}

def count_each_vowel(in_string):
    vowel_counts = dict()
    for letter in in_string.lower():
        if letter in vowels:
            new_count = vowel_counts.get(letter, 0) + 1
            vowel_counts[letter] = new_count
    return vowel_counts

def tabulate_vowel_count(vowel_counts):
    return sum(vowel_counts.values())

class TestCountVowels(unittest.TestCase):
    def vowel_dict(self, *args):
        sorted_vowels = ['a','e','i','o','u']
        return {v:c for v,c in zip(sorted_vowels, args) if c > 0}

    def check_count_each_vowel(self, test_string, expected_output):
        self.assertEqual(count_each_vowel(test_string), self.vowel_dict(*expected_output))

    def test_count_each_vowel_01(self):
        self.check_count_each_vowel('aeiou', [1,1,1,1,1])

    def test_count_each_vowel_02(self):
        self.check_count_each_vowel('What is your name?', [2,1,1,1,1])

    def test_count_each_vowel_03(self):
        self.check_count_each_vowel('AeIoU', [1,1,1,1,1])

    def test_count_each_vowel_04(self):
        self.check_count_each_vowel('AeoU', [1,1,0,1,1])

if __name__ == '__main__':
    unittest.main()
