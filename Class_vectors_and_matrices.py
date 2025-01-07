import math as ma 
import numpy as np
class vector2d:
    def __init__(self,upper=0,lower=0):
        self.a=upper
        self.b=lower
    def __str__(self):
        return str([self.a, self.b])
    def __add__(self,other):
        return vector2d(self.a+other.a,self.b+other.b)
    def __mul__(self,other): #This is the definition of scalar multiplication, not an dot product or a cross product
        if isinstance(other,int):
            return vector2d(other*self.a, other*self.b)
        elif isinstance(other,vector2d):
            return ("This is undefined")
    def __rmul__(self,other): #This is the definition of scalar multiplication, not an dot product or a cross product
        if isinstance(other,int):
            return vector2d(other*self.a, other*self.b)
        elif isinstance(other,vector2d):
            return ("This is undefined")
    def __sub__(self,other):
        return vector2d(self.a-other.a,self.b-other.b)
    def __neg__(self):
        return vector2d(-1*self.a, -1*self.b)
    def pos__(self):
        return vector2d(self.a, self.b)
    def __eq__(self,other):
        if self.a==other.a and self.b==other.b:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.a!=other.a and self.b!=other.b:
            return True
        else:
            return False
    def length (self):
        return ma.sqrt(self.a**2+self.b**2)
    def mod (self,other):
        if isinstance (other, int):
            return vector2d(self.a%other, self.b%other)
        #takes a vector and takes the modulo other of all elements
class vector3d:
    def __init__(self,upper=0,middle=0, lower=0):
        self.a=upper
        self.b=middle
        self.c=lower
    def __str__(self):
        return str([self.a, self.b, self.c])
    def __add__(self,other):
        return vector2d(self.a+other.a,self.b+other.b, other.c+other.c)
    def __mul__(self,other): #This is the definition of scalar multiplication, not an dot product or a cross product
        if isinstance(other,int):
            return vector2d(other*self.a, other*self.b, other.c)
        elif isinstance(other,vector2d):
            return ("This is undefined")
    def __rmul__(self,other): #This is the definition of scalar multiplication, not an dot product or a cross product
        if isinstance(other,int):
            return vector2d(other*self.a, other*self.b, other*self.c)
        elif isinstance(other,vector2d):
            return ("This is undefined")
    def __sub__(self,other):
        return vector2d(self.a-other.a,self.b-other.b, self.c-self.c)
    def __neg__(self):
        return vector2d(-1*self.a, -1*self.b,-1*self.c)
    def __pos__(self):
        return vector2d(self.a, self.b, self.c)
    def __eq__(self,other):
        if self.a==other.a and self.b==other.b and self.c==other.c:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.a!=other.a and self.b!=other.b and self.c!=other.c:
            return True
        else:
            return False
    def length (self):
        return ma.sqrt(self.a**2+self.b**2+self.c**2)
    def mod (self,other):
        if isinstance (other, int):
            return vector2d(self.a%other, self.b%other, self.c%other)
        #takes a vector and takes the modulo other of all elements


        
