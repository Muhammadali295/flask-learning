from abc import ABCMeta, abstractmethod
class vehicle (metaclass=ABCMeta):
     def __init__(self,m,n):
          self.model=m
          self.no_of_wheels=n
     @abstractmethod
     def print(self):
         pass

class Car(Vehicle):

definit (self,m,n,t,s): super()...init (m, n)

setr, typest

self sizes

def print(ont):

print (ael.model, self.no_of_wheels, self.type, self.size)

class Truck(Vehicle):

definit (self,m,n.p.1):

super(). init (m, n)

self.pricep
[1:12 AM, 7/1/2022] Ali: super().init__(m, n)

self.price-p

21

self.miles-mi

def print(self):

print(self.model, self.no_of_wheels, self.price, self.miles)

176

soles

I

class Motorcycle (Vehicle):

definit__(self, m, n, e):

super().init__(m, n)

self.make m

self.engine-e

def print(self):

print(self.model, self.no_of_wheels, self.make, selt.engine)

c=Truck(2,5,2021,1)

c.print()

