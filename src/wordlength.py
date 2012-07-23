"""Parse a text file, and display words of the length specified."""

import re, sys, argparse

# globals

__version__ = "0.9"

#-------------------------------------- command-line options ----------------------------------------------------------
# class OptionParser (optparse.OptionParser):

#     def check_required (self, opt):
#       option = self.get_option(opt)

#       # Assumes the option's 'default' is set to None!
#       if getattr(self.values, option.dest) is None:
#           self.error("%s option not supplied" % option)


# def getCommandLineParser():
#    usage = "usage: %prog [OPTIONS]\n" + __doc__
   
#    option_list = [
#       optparse.make_option("-l", "--length", type = "int", dest = "length_of_words_to_list",
#                            help = "The length of the words that are to be searched for in the document"),
#       optparse.make_option("-f", "--filename", dest = "filename",
#                            help = "The document to be searched"),
#    ]
   
#    parser = optparse.OptionParser(usage, version = __version__, option_list = option_list)

#    return parser

parser = argparse.ArgumentsParser(description='decription TODO..')
parser.add_argument('--filename', metavar='f', type=string, help='the file to be processed')
# -----------------------------------------main -----------------------------------------------------------


# parser = getCommandLineParser()
# (options, args) = parser.parse_args()
# parser.check_required("-f")
# parser.check_required("-l")

# # validate options
# if options.filename is None or options.length_of_words_to_list is None:
#    parser.error("You must specify all arguments.")
   
try:
   f = open(options.filename)
except:
   print "Failed to open file"
   sys.exit(2)

line = f.readline()
count = 0
matches = []

if options.length_of_words_to_list < 1 or options.length_of_words_to_list > 100:
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
      if len(words[i]) == options.length_of_words_to_list:
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