from Class_vectors_and_matrices import vector 
from Class_vectors_and_matrices import matrix 
#DEFINING TERMS#
#secures message and adds 4 extra bits:
Generator_matrix=matrix([[1,0,0,0,1,1,0],[0,1,0,0,1,0,1],[0,0,1,0,0,1,1],
                         [0,0,0,1,1,1,1]]) 
#checks whether or not a message was corrupted
Parity_check=matrix([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])
test1=matrix([[1],[0],[0],[1],[1],[0],[0]])
test2=matrix([[1,1,0,1]])

#Some helpful functions
def encrypt74(self,Generator_matrix):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. It returns the same code with after it the security-bits. 
    In the form of a matrix size 1 x (n+the security-bits).
    """
    if self.shape()[1] == Generator_matrix.shape()[0]:
        return matrix.XOR(self,Generator_matrix)
    else:
        return "This is undefined.."
    
def parity(check,Parity_check):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. At which index the original code should be flipped, if 
    neccesary. 
    """
    if Parity_check.shape()[1]==check.shape()[0]:
        answer=matrix.XOR(Parity_check,check)
    else:
        return "This is undefined.."
    if answer == matrix([[0], [0], [0]]):
        return None
    elif answer== matrix([[1],[1],[0]]):
        return 0
    elif answer== matrix([[1],[0],[1]]):
        return 1
    elif answer== matrix([[0],[1],[1]]):
        return 2
    elif answer== matrix([[1],[1],[1]]):
        return 3
    elif answer== matrix([[1],[0],[0]]):
        return 4
    elif answer== matrix([[0],[1],[0]]):
        return 5
    elif answer== matrix([[0],[0],[1]]):
        return 6
def reperation(check,Parity_check):
    """
    Repares a gives vector. Question het to solve: how do we adapt an element 
    in a matrix.
    """
    repare=parity(check,Parity_check)
    return repare
x=encrypt74(matrix([[1,1,0,0]]), Generator_matrix)
print(matrix([1,1,0,0]))
print(x)