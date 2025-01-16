from Class_vectors_and_matrices import vector
from Class_vectors_and_matrices import matrix

# Let all messages will be written in binairy blcks of 8 bits (a byte).
def encode(text):
    byte_number = text.encode('utf-8')
    binary_str = ''
    for byte in byte_number:
        binary_str += format(byte, '08b')          
    return binary_str

# Secures message and adds 4 extra bits:
Generator_matrix = matrix([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
])

# Checks whether or not a message was corrupted
Parity_check = matrix([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
])


def encrypt74(message_4, generator_matrix):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. It returns the same code with after it the security-bits. 
    In the form of a matrix size 1 x (n+the security-bits).
    """
    if message_4.shape()[1] == generator_matrix.shape()[0]:
        return matrix.XOR(generator_matrix, message_4)
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
        return "None"
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
    
def correct (a):
    wrong = parity(a,Parity_check)
    if wrong == "None":
        return a
    else:
        return a.change_element((0,wrong),1)

# Make it into a 4-bit code again.
def decrypt74(message_7): 
    return None
# All blocks of 8 bits go back to text.
def decode(binary_string):
    bytes_string = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    byte_number = [int(byte, 2) for byte in bytes_string]
    text = bytes(byte_number).decode('utf-8')
    return text
test=correct(matrix([[1,1],0,1,0,0,0]))
print(correct(test))