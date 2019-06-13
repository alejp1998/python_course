#Instead of storing the results we return them
def create_cubes(n):
    for x in range(n):
        yield x**3

def gen_gibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_gibon(10):
    print(number)

#This function return the values of the range one by one
def simple_gen():
    for x in range(3):
        yield x

#Prints all the number
for number in simple_gen():
    print(number)

#We assign g a yielding function
g = simple_gen

g
#Prints the next value according to the formula
#print(next(g))
#If we try to get more than three values it will return an error
#We dont get this error on for loops because it catches the error and stops iterating

s = 'hello'
#s supports iteration because we run it with a for
for letter in s:
    print(letter)

#We transform the string into an iterator
s = iter(s)
#And now we can use next in it
print(next(s))
print(next(s))
print(next(s))


#HOMEWORK

#Generate squares of a number up to N
def gensquares(N):
    for x in range(N):
        yield x**2

import random
#Generate 10 random number between low and high
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

#When you want the value and its next values, but do not want to store them all in memory

my_list = [1,2,3,4,5]
#We define a generator for the number in my_list bigger than 3
#Turn list comprehesion into generator comprehension
gen_comp = (item for item in my_list if item>3)
#We use this generator in a for loop
for item in gen_comp:
    print(item)
