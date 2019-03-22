from sys import argv

script, filename = argv

print "We're going to erase %r." % filename 
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for three lines."

# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")

# print "I'm going to write these to the file."
# 
# 
# target.write("hello world.")
# target.write("\n")
# target.write("My name is Leon.")
# target.write("\n")
# target.write("What's your name?")
# target.write("\n")

print "I'm going to write these to the file."
a = [1, 2, 3]
for i in a:
    line = raw_input("line : ")
    target.write(line + '\n');
print "And finally, we close it."
target.close()


