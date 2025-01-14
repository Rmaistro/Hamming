from Class_vectors_and_matrices import vector
from Class_vectors_and_matrices import matrix
#secures message and adds 4 extra bits:
Generator_matrix=matrix([[1,0,0,0,1,1,0],[0,1,0,0,1,0,1],[0,0,1,0,0,1,1],[0,0,0,1,1,1,1]]) 
#checks whether or not a message was corrupted
Parity_check=matrix([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])
test1=matrix([[1],[1],[0],[1],[1],[0],[0]])
test2=matrix([[1,1,0,1]])

def encrypt74(self,Generator_matrix):
    if self.shape()[1] == Generator_matrix.shape()[0]:
        return matrix.XOR(self,Generator_matrix)
    else:
        return "This is undefined.."
def parity74 (self,Parity_check):
    if Parity_check.shape()[1]==self.shape()[0]:
        answer=matrix.XOR(Parity_check,self)
        Checking_library={
            matrix([[0],[0],[0],[0]]) : None
            }
    else:
        return "This is undefined.."
print(parity74(test1, Generator_matrix))
