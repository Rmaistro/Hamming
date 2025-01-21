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

# Transforms a 7 string "correctly encrypted" code, back to the original nibble.
Return_matrix = matrix([
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
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
    
def correct (a,Parity_chek):
    wrong = parity(a,Parity_check)
    if wrong == "None":
        return a
    else:
        new=a.get_element((wrong,0))^1
        return a.change_element((wrong,0),new)

# Make it into a 4-bit code again.
def decrypt74(corrected, Return): 
    """
    Takes a nx1-matrix m. After multiplaction of a matrix with m,
    the original output is displayed as een 1 x n- matix
    """
    return Return*corrected
def decode(binary_string):
    """
    Takes a 8 bit string and returns is to 'normal' text.
    """
    bytes_string = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    byte_number = [int(byte, 2) for byte in bytes_string]
    text = bytes(byte_number).decode('utf-8')
    return text
def total_check(a):
    new=correct(a,Parity_check)
    original =decrypt74(new,Return_matrix)
    original_string = list(original).join()
    return original_string
x = matrix([[1],[1],[1],[1],[0],[0],[1]])
print(total_check(x))
