#!/usr/bin/python
"""Parse a text file, and display words of the length specified."""

import re, sys, argparse

# globals

__version__ = "0.9"

#-------------------------------------- command-line options ----------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to be processed')
parser.add_argument('length_of_words_to_list' , help='search for words with this many letters', type=int)
args = parser.parse_args()
# -----------------------------------------main -----------------------------------------------------------
   
try:
   file = open(args.filename)
except:
   print "Failed to open file"
   sys.exit(2)

line = file.readline()
count = 0
words_of_correct_length = []

if args.length_of_words_to_list < 1 or args.length_of_words_to_list > 100:
   parser.error("Invalid word length entered,",repr(length_of_words_to_list))


# while not EOF
while line != '':
   line = file.readline()

   # split the line into words
   words = line.split()
   for i in range(len(words)):

      # strip any non alpha characters
      words[i] = re.sub("[^A-Za-z]", "", words[i])

      # test to see if we have the correct number of characters
      if len(words[i]) == args.length_of_words_to_list:
         words_of_correct_length.append(words[i].lower())

file.close()
# order list alphabetically
words_of_correct_length.sort()

# remove any duplicate entries
unique_words_of_correct_length = []
for word in words_of_correct_length:
   if word not in unique_words_of_correct_length:
      unique_words_of_correct_length.append(word)
      count = count + 1

# print the result
for i in range(len(unique_words_of_correct_length)):
   print unique_words_of_correct_length[i]
print
print "Total words found", count
