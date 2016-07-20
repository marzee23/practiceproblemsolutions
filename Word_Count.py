#Count Words in a String - Counts the number of individual words in a string.
#For added complexity read these strings in from a text file and generate a summary.

text = input("Enter the text you would like me to count: ")

def word_count(text):
    words = text.split()
    print("There are", len(words), "words in that text.")

word_count(text)
