class Point:
    'docstring for help to explain class'
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}({},{})".format(self.__class__.__name__,self.x,self.y)
    
    def setx(self,x):
        'docstring for help to explain method'
        self.x = x

    def sety(self,y):
        self.y = y

    def get(self):
        return (self.x,self.y)

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Vector(Point):
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __mul__(self,other):
        return (self.x*other.x+self.y*other.y)

class Test:
    version = 1.02

class Rectangle:

    def __init__(self,w=0,l=0):
        self.w = w
        self.l = l

    def __repr__(self): 
        return "Rectangle({},{})".format(self.w,self.l)

    def setSize(self,w,l):
        self.w = w
        self.l = l

    def perimeter(self):
        return 2*(self.w+self.l)

    def area(self):
        return self.w*self.l

class Animal:
    def __init__(self,spec="animal",lang="make sounds"):
        self.spec = spec
        self.lang = lang

    def __repr__(self):
        return "Animal('{}','{}')".format(self.spec,self.lang)
    
    def setSpecies(self, spec):
        self.spec= spec

    def setLanguage(self, lang):
        self.lang = lang

    def speak(self):
        print('I am a {} and I {}.'.format(self.spec,self.lang))

class Bird(Animal):
    def speak(self):
        print((self.lang+"! ")*3)

class Queue:
    'represents a queue in First-In First-Out ordering'

    def __init__(self):
        self.q = []

    def __repr__(self):
        return "Queue({})".format(str(self.q))

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        if self.isEmpty:
            raise EmptyQueueError('dequeue from empty queue')
        return self.q.pop(0)

    def isEmpty(self):
        return (len(self.q)==0)

class EmptyQueueError(Exception):
    pass

import random
class MyList(list):
    'subclass of list supporting method choice()'

    def choice(self):
        return random.choice(self)
