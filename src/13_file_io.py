"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
filePath = os.path.abspath(__file__)
foo = open(os.path.dirname(filePath) + '\\foo.txt', 'r')
# open('foo.txt', 'r')
# YOUR CODE HERE
for i in foo:
    print(i)
foo.close()

with open(os.path.dirname(filePath) + '\\textFiles\\bar.txt', 'r') as myBar:
    for i in myBar:
        print(i)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open(os.path.dirname(filePath) + '\\bar.txt', 'w') as bar:
    bar.write("line 1\n")
    bar.write("line 2\n")
    bar.write("line 3\n")