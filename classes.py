class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        xdist = abs( self.coor1(0) - self.coor2(0) )
        ydist= abs( self.coor1(1) - self.coor2(1) )
        distance = (xdist**2 + ydist**2)**0.5
        return distance

    def slope(self):
        return ( self.coor2(1) - self.coor1(1) )/( self.coor2(0) - self.coor1(0) )

class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.141592*self.height*self.radius**2

    def surface_area(self):
        return 2*3.141592*self.radius*self.height

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,money):
        self.balance += money
        print("{}$ added to {}'s account".format(money,self.owner))
        print('Your balance is {}'.format(self.balance))

    def withdraw(self,money):
        if self.balance >= money:
            self.balance -= money
            print("{}$ extracted from {}'s account".format(money,self.owner))
            print('Your balance is {}'.format(self.balance))
        else:
            print('Not enough money. You can withdraw up to {}$'.format(self.balance))

newaccount = Account('Alex')
newaccount.deposit(100)
newaccount.withdraw(50)
newaccount.withdraw(60)
