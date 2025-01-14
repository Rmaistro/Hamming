import numpy as np
from functools import reduce

def testset(n):
    #creating a random string of 16 bits
    return np.random.randint(0,2,n)
    
def checking(bits):
    #in case of a one-error, returns the index for the error   
    bits_numbered=list(enumerate(bits)) #adding indeces from 0-n
    #performing x-or's on the indeces with value 1
    answer=reduce(lambda x,y: x^y, [x for x, bit in enumerate(bits) if bit])
    return answer

def correcting (bits):
    wrong=checking(bits)
    bits[wrong]=(bits[wrong]+1)%2
    return bits
