import math
import string

#STARTING FUNCTIONS

def hello_world ():
    print('Hello World')

def hello_name (name):
    print('Hello ' + name)

def greeting (a):
    if a:
        return 'Hello'
    else:
        return 'Goodbye'

def xyz (x,y,z):
    if z:
        return x
    else:
        return y

def sum (a,b):
    return a + b

def is_even (value):
    if (value % 2) == 0:
        return True
    else:
        return False

def is_greater (a,b):
    if a > b:
        print('{} is greater than {}'.format(a,b))
        return True
    else:
        print('{} is not greater than {}'.format(a,b))
        return False

#INFINITE ARGS FUNCTIONS

def infinite_sum (*args):
    sum = 0
    for value in args:
        sum += value
    return sum

def kwargs_test (**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit there')

def both_test (*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

def evens (*args):
    evens = []
    for value in args:
        if (value % 2) == 0:
            evens.append(value)
    return evens

def casing (string):
    count = 0
    new_string = ''
    for letter in string:
        if (count % 2) == 0:
            new_string += letter.lower()
        else:
            new_string += letter.upper()
        count += 1
    return new_string

#CHALLENGING PROBLEMS

def spy_game(nums):
    string = ''
    for num in nums:
        string += str(value)
    return '007' in string

def count_primes(num):
    primes = 0
    divisible = False
    if num > 1:
    for number in range(2,num):
        for prime in range(2,number):
            divisible = (number % prime) == 0
            if divisible:
                break
        if not divisible:
            primes +=1
        divisible = False
    return primes

#HOMEWORK

def vol(rad):
    return (4/3)*math.pi*(rad**3)

def ran_check(num,low,high):
    if (num>=low) and (num<=high):
        print('{} is between {} and {}'.format(num,low,high))
        return True
    else:
        print('{} is not between {} and {}'.format(num,low,high))
        return False

def up_low(string):
    uppers = 0
    lowers = 0
    for letter in string:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1
    print('No. of Upper case characters : {}'.format(uppers))
    print('No. of Lower case characters : {}'.format(lowers))

def ispangram(str1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_str = str1.lower()
    for letter in alphabet:
        if letter in new_str:
            ispangram = True
            continue
        else:
            ispangram = False
            break
    return ispangram
