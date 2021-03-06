#!/usr/bin/python
"""Parse a text file, and display words of the length specified."""

import re, sys, argparse

#-------------------------------------- command-line options ----------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to be processed')
parser.add_argument('required_word_length' , help='search for words with this many letters', type=int)
args = parser.parse_args()
# -----------------------------------------main -----------------------------------------------------------
   
try:
   file = open(args.filename)
except:
   print "Failed to open file"
   sys.exit(2)

number_of_words_found = 0
words_of_correct_length = []

if args.required_word_length < 1 or args.required_word_length > 100:
   parser.error("Invalid word length entered,",repr(required_word_length))

while True:
   line = file.readline()
   # "if f.readline() returns an empty string,  
   # the end of the file has been reached, " - python docs
   if line == '':
      break
   words = line.split()
   for i in range(len(words)):

      # strip any non alpha characters
      words[i] = re.sub("[^A-Za-z]", "", words[i])

      if len(words[i]) == args.required_word_length:
         words_of_correct_length.append(words[i].lower())

file.close()

# remove any duplicate entries
unique_words_of_correct_length = []
for word in words_of_correct_length:
   if word not in unique_words_of_correct_length:
      unique_words_of_correct_length.append(word)
      number_of_words_found = number_of_words_found + 1

# order list alphabetically
unique_words_of_correct_length.sort()

# print all matching words
for i in range(len(unique_words_of_correct_length)):
   print unique_words_of_correct_length[i]

print "\nTotal words found", number_of_words_found
