#!/usr/bin/env python3

import sys
from count_vowels import count_each_vowel, tabulate_vowel_count

arg_string = " ".join(sys.argv[1:])
vowel_counts = count_each_vowel(arg_string)
total_vowels = tabulate_vowel_count(vowel_counts)
print("There are", total_vowels, "vowels in '{}'".format(arg_string))
for vowel in sorted(vowel_counts.keys()):
    print("There are", vowel_counts.get(vowel, 0), vowel.upper(), "'s!")
