#!/usr/bin/python 
#_*_ coding:utf-8 _*_
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying form %s to %s" % (from_file, to_file)

we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)
# 
# print "Does the output file exists? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."


out_file.close()
in_file.close()

# The whole script in one line
open("outfile.txt", 'w').write(open("infile.txt").read())


