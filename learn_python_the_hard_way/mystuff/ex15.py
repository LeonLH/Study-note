# import a module named argv form package called sys
from sys import argv

# unpack the arguments from command line
script, filename = argv

# open a file and return a file object, then assign it to txt. 
txt = open(filename)

# using file's method read() to read the content
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
