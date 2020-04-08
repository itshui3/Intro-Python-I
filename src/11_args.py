# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

#positional arguments
#javascript uses these for function args as default
#args passed into a function are associated with params used within the function on the basis of the relative positions
#def thisFunc(x, y)
#   dosomethingto(x)

#^^^ in the above example, anything passed as the first arg in thisFunc will be evaluated as the param x when the function is called

#arbitrary arguments

#keyword arguments

#properties of keyword arguments
#functions declared with keyword args allow for default args that are used if nothing is passed in when the function is called

#dont have to pass in all the params expected args

#don't have to pass in args in the same order as the params, because there is a way to specify which param is to be given an arg

#if used in conjunction with positional args, positional args need to come first and need to be filled in before any keyword args can be passed in and assigned to a keyword param?

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(a, b):
    return sum([a, b])
print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
# What about just an array that gets passed in? 

# YOUR CODE HERE

# [1, 2, 3]
def f2(*numbers):
    summed = 0
    for num in numbers:
        if(type(num) == int):
            summed += num
            continue
        
        if(type(num) == list):
            # numberList = num
            for listNum in num:
                if(type(listNum) != int):
                    print('list arg contains non-number value, cannot sum')
                    # fatal error in python 
                    continue
        
                summed += listNum

    return summed

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(a, b=False):
    if(b):
        return a + b
    else:
        return a + 1
print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9

def f3_1(a, b=1):
    return a + b

# # Write a function f4 that accepts an arbitrary number of keyword arguments and
# # prints out the keys and values like so:
# #
# # key: foo, value: bar
# # key: baz, value: 12
# #
# # Note: Google "python keyword arguments".

# # YOUR CODE HERE
def f4(**kwargs):
    for key in kwargs:
        if(type(kwargs[key]) == dict):
            print(key)
        else:
            print(f"key: {key}, value: {kwargs[key]}")


# # Should print
# # key: a, value: 12
# # key: b, value: 30
f4(a=12, b=30)

# # Should print
# # key: city, value: Berkeley
# # key: population, value: 121240
# # key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# # How do you have to modify the f4 call below to make this work?
f4(**d)
f4(monster=d["monster"], hp=d["hp"])
