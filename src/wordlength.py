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
   f = open(args.filename)
except:
   print "Failed to open file"
   sys.exit(2)

line = f.readline()
count = 0
matches = []

if args.length_of_words_to_list < 1 or args.length_of_words_to_list > 100:
   parser.error("Invalid word length entered,",repr(length_of_words_to_list))


# while not EOF
while line != '':
   line = f.readline()

   # split the line into words
   words = line.split()
   for i in range(len(words)):

      # strip any non alpha characters
      words[i] = re.sub("[^A-Za-z]", "", words[i])

      # test to see if we have the correct number of characters
      if len(words[i]) == args.length_of_words_to_list:
         matches.append(words[i].lower())

# order list alphabetically
matches.sort()

# remove any duplicate entries
unique = []
for x in matches:
   if x not in unique:
      unique.append(x)
      count = count + 1

# print the result
for i in range(len(unique)):
   print unique[i]
print
print "Total words found", count
f.close()