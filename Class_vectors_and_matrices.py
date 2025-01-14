"""
Created on Tue Jan  7 12:16:17 2025

@author: jogde
"""

import math as m 
import numpy as np      

"""
Below we have defined a class of vectors. 

A vector can be created by assigning vector(list) to a variable. 
Between the brackests you must put a list of floats which represent the elements of the vector.
The first element of the list represents the upper most element of the vector.
All basic vector operations and comparisons except a cross product can be performed. 
We have also defined the operation mod(other) which takes the mod(other) of each element of the vector separately.
"""

class vector:
    def __init__(self, lst):
        self.lst = lst
        self.arr = np.array(lst)
    def __str__(self):
        return str(self.lst)
    def __add__(self,other):
        if type(other) == vector and len(self.lst) == len(other.lst):
            return vector(list(self.arr + other.arr))
        else:
            print('This is undefined')
    def __sub__(self,other):
        if type(other) == vector and len(self.lst) == len(other.lst):
            return vector(list(self.arr + other.arr))
        else:
            print('This is undefined')
    def __mul__(self,other): #This is the definition of scalar multiplication and a dot product depending on the type of other.
        if type(other) == float or type(other) == int:
            return vector(list(self.arr * other))
        elif type(other) == vector:
            if len(self.lst) == len(other.lst):
                var = 0
                for i in range(len(self.lst)):
                    var += self.lst[i] * other.lst[i]
                return var
            else:
                print('This is undefined')
        else:
            print('This is undefined')
    def __rmul__(self,other): 
        return self.__mul__(other)
    def __neg__(self):
        return vector(list(self.arr * -1))
    def __pos__(self):
        return self
    def length(self):
        squares = 0
        for i in self.lst:
            squares += i**2
        return m.sqrt(squares)
    def unit(self):
        return self.__mul__(1/self.length())
    def mod(self,other): #takes a vector and takes the modulo other of all elements
        if type(other) == int:
            newlst = [i%other for i in self.lst]
            return vector(newlst)
        else:
            print('This is undefined')
    def dim(self):
        return len(self.lst)
    def __eq__(self,other):
        if self.lst == other.lst:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.lst != other.lst:
            return True
        else:
            return False
    def isparallel(self, other):
        if type(other) == vector:
            if self.unit() == other.unit():
                return True
            else: 
                return False
        else:
            print('This is undefined')

"""
Below we have defined a class of matrices. 

A matrix can be created by assigning matrix(list) to a variable. 
Between the brackests you must put a nested list of floats which represent the elements of the matrix.
The first list of the nested list represents the upper most row of the matrix.
The basic matrix operations addition, substraction and multiplication are defined as usual.
Matrices can be compared using __eq__ and __ne__.
Matrix.shape gives a the following tupple (m,n) for a m by n matrix.
We have also defined the operation mod(other) which takes the mod(other) of each element of the vector separately.
We have also defined the XOR function which multiplies two matrices and takes all element mod(2).
"""    

class matrix:
    def __init__(self, lst):
        self.lst = lst
        self.arr = np.array(lst)
    def __str__(self):
        return str(self.lst)
    def shape(self):
        return self.arr.shape
    def __add__(self,other):
        if type(other) == matrix and self.shape() == other.shape():
            arrsum = self.arr + other.arr
            return matrix(arrsum.tolist())
        else:
            print('This is undefined')
    def __sub__(self,other):
        if type(other) == matrix and self.shape() == other.shape():
            arrdif = self.arr - other.arr
            return matrix(arrdif.tolist())
        else:
            print('This is undefined')
    def __mul__(self,other): #This is the definition of scalar multiplication and matrix multplication depending on the type of other.
        if type(other) == float or type(other) == int:
            arrprod = self.arr * other
            return matrix(arrprod.tolist())
        elif type(other) == matrix:
            if self.shape()[1] == other.shape()[0]:
                lijst = []
                for i in range(0,self.shape()[0]):
                    rijlijst = []
                    for j in range(0,other.shape()[1]):
                        var = 0
                        for k in range(0,self.shape()[1]):
                            var += self.lst[i][k] * other.lst[k][j]
                        rijlijst.append(var)
                    lijst.append(rijlijst)
                return matrix(lijst)
            else:
                print('This is undefined')
        else:
            print('This is undefined')
    def __rmul__(self,other): 
        if type(other) == float or type(other) == int:
            arrprod = self.arr * other
            return matrix(arrprod.tolist())
        else:
            print('This is undefined')
    def __neg__(self):
        return self.__mul__(-1)
    def __pos__(self):
        return self
    def mod(self,other): #takes a matrix and takes the modulo other of all elements
        if type(other) == int:
            newarr = self.arr % other
            newlst = newarr.tolist()
            return matrix(newlst)
        else:
            print('This is undefined')
    def XOR(self, other):
        mprod = self.__mul__(other)
        return mprod.mod(2)
    def __eq__(self,other):
        if self.lst == other.lst:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.lst != other.lst:
            return True
        else:
            return False
