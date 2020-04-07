"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
foo = open('./src/foo.txt', 'r')
fooReadable = foo.read()
print(foo)
print(fooReadable)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('./src/bar.txt', 'w+')
bar.write('Hi, this is some text')

#Notes

#Python can read/write files, but before that can happen we need access to it through Python's built-in open() function

#open() returns object of the file type(?) or an IOError