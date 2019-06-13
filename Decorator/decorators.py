
#DECORATORS INTRO
def hello():
    return 'Hi Ale!'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func())

other(hello)

#ORIGINAL FUNCTION
def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before original func')
        original_func()
        print('Some extra code after original func')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

#This returns the original function wrapped by other code
decorated_func = new_decorator(func_needs_decorator)
#We execute the decorated function
decorated_func()

#Easier syntax
@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
#Run the decorated function, if we comment the @ we run the normal func
func_needs_decorator()
