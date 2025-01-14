<<<<<<< HEAD
import numpy as np
from functools import reduce

def encrypting(lst):
    #is able to encrypt an eleven bit long code
    if len(lst) !=11:
        return "Something has gone wrong, please check your input"
    else:
        a=lst[4]^lst[5]^lst[6]^lst[7]^lst[8]^lst[9]^lst[10]
        b=lst[1]^lst[2]^lst[3]^lst[7]^lst[8]^lst[9]^lst[10]
        c=lst[1]^lst[4]^lst[8]^lst[0]^lst[3]^lst[6]^lst[10]
        d=lst[2]^lst[5]^lst[8]^lst[0]^lst[3]^lst[6]^lst[10]
        e=lst[0]^lst[1]^lst[2]^lst[3]^lst[4]^lst[5]^lst[6]^lst[7]^lst[8]^lst[9]^lst[10]
    encryption=(a,b,c,d,e)
    return encryption

def testset(n):
    #creating a random string of 16 bits
    return np.random.randint(0,2,n)
    
def checking(bits):
    #in case of a one-error, returns the index for the error   
    #performing x-or's on the indeces with value 1
    answer=reduce(lambda x,y: x^y, [x for x, bit in enumerate(bits) if bit])
    return answer

def correcting (bits):
    wrong=checking(bits)
    bits[wrong]=(bits[wrong]+1)%2
    return bits
x=testset(11)
print(x)
print(encrypting(x))

      
=======
import numpy as np
from functools import reduce

def encrypting(lst):
    #is able to encrypt an eleven bit long code
    if len(lst) !=11:
        return "Something has gone wrong, please check your input"
    else:
        a=lst[4]^lst[5]^lst[6]^lst[7]^lst[8]^lst[9]^lst[10]
        b=lst[1]^lst[2]^lst[3]^lst[7]^lst[8]^lst[9]^lst[10]
        c=lst[1]^lst[4]^lst[8]^lst[0]^lst[3]^lst[6]^lst[10]
        d=lst[2]^lst[5]^lst[8]^lst[0]^lst[3]^lst[6]^lst[10]
        e=lst[0]^lst[1]^lst[2]^lst[3]^lst[4]^lst[5]^lst[6]^lst[7]^lst[8]^lst[9]^lst[10]
    encryption=(a,b,c,d,e)
    return encryption

def testset(n):
    #creating a random string of 16 bits
    return np.random.randint(0,2,n)
    
def checking(bits):
    #in case of a one-error, returns the index for the error   
    #performing x-or's on the indeces with value 1
    answer=reduce(lambda x,y: x^y, [x for x, bit in enumerate(bits) if bit])
    return answer

def correcting (bits):
    wrong=checking(bits)
    bits[wrong]=(bits[wrong]+1)%2
    return bits
x=testset(11)
print(x)
print(encrypting(x))

      
>>>>>>> 1214ae21ba77adec0b925419fd783a27b66c31ab
