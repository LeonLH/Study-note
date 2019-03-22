# from math import pi
# Flo = pi
# print "%03g %.9f %G %E" % (Flo, Flo, Flo, Flo)
# R = round(4.33333)
# print "R = %r" % R
# print "%r" % pi

##################################################
# #!/usr/bin/python
# 
# # Open a file
# fo = open("foo.txt", "ra+")
# print "Name of the file: ", fo.name
# 
# # Assuming file has following 5 lines
# # This is 1st line
# # This is 2nd line
# # This is 3rd line
# # This is 4th line
# # This is 5th line
# 
# # line = fo.readline()
# # print "Read Line: %s" % (line)
# 
# # Now truncate remaining file.
# fo.truncate(28)
# 
# # Try to read file now
# line = fo.readline()
# print "Read Line: %s" % (line)
# 
# # Close opend file
# fo.close()

#################################################################

# Test for `Will print print a \n? `
# Yes, It will, and If you don't want it act like this, you can put a
# `,` after print sentence. 

# print "Hello world" 
# print "I'm Leon. "

#################################################################

# Test for coercive transformation

# def add(a, b):
#     return a + b
# 
# a = 
# print "%d + %d = %d" % (a, b, add(a, b))
#################################################################

# Test for formatted string

# print "The number is \x42"
# print "The number is \103"
#################################################################

# This is test for file.truncate()

txt = open("test.txt", 'r+w')
# txt.truncate(20);
print txt.readline()
line = txt.readline()
print line
txt.seek(1)             
line = txt.readline()
print line
#################################################################
