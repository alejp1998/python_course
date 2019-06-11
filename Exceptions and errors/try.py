try:
    #Want to attemp this code, may have an error
    result = 10 + 10
except:
    #If there is an exception
    print('Errors while adding')
else:
    #If there is no error
    print('Add went well')
    print(result )

try:
    f = open('textfile','w')
    f.write('Write a text line')
except TypeError:
    print('There was a type error')
except OSError:
    print('Hey you have an OS Error')
except:
    print('All other exceptions')
finally:
    print('I always run')

def ask_for_int():
    #Keep running until no exception
    while True:
        try:
            result = int(input('Please provide a number'))
        except:
            print('Whoops! That isnt a number')
            continue
        else:
            print('Thank u')
            break
        finally:
            print('Im going to ask u again')

#HOMEWORK
#1. Handle the exception
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('Cannot multiply a char')

#2. Handle and use finally
try:
    x = 5
    y = 0
    z = x/y
except:
    print('Cannot divide by zero')
finally:
    print('All done')

#3. Ask for integer and print square
def ask():
    while True:
        try:
            value = int(input('Square an integer'))
        except:
            print('Not a number. Try again')
            continue
        else:
            print('The square of {} is {}'.format(value,value**2))
            break

ask()
