#DEFINITION OF FUNCTIONS AND CLASSES
def func():
    print('func() in one.py')

print('Top level in one.py')

#If we run this directly, this condition is true
if __name__ == '__main__':
    #EXECUTE FUNCTIONS AND CLASSES
    print('One.py is being run directly')
else:
    print('One.py has been imported!')
