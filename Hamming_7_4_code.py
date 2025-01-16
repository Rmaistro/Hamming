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
    if message_4.shape()[1] == generator_matrix.shape()[0]:
        return matrix.XOR(generator_matrix, message_4)
    else:
        return "This is undefined.."


def parity74(message_7, parity_check):
    if parity_check.shape()[1] == message_7.shape()[0]:
        syndrome = matrix.XOR(parity_check, message_7)
        
        Checking_library = {
            matrix([[0], [0], [0]]): None,  
            
            matrix([[1], [0], [0]]): 5,  # Error in bit 5=x
            matrix([[0], [1], [0]]): 6,  # Error in bit 6=y
            matrix([[0], [0], [1]]): 7,  # Error in bit 7=z
            
            matrix([[1], [1], [0]]): 1,  # Error in bit 1=a
            matrix([[1], [0], [1]]): 2,  # Error in bit 2=b
            matrix([[0], [1], [1]]): 3,  # Error in bit 3=c
            matrix([[1], [1], [1]]): 4,  # Error in bit 4=d
}

        # Determine where the error is.
        error_position = Checking_library[syndrome] 
        
        # Correcting the code by flipping one bit.
        if error_position:
            message_list = message_7.get_matrix()  
            message_list[error_position - 1][0] ^= 1
            corrected_message = matrix(message_list)
            return corrected_message
        else:
            return message_7 

# Make it into a 4-bit code again.
def decrypt74(message_7): 
    message_list = message_7.get_matrix()
    binary_string = []
    for i in range(4):
        binary_string.append(message_list[i][0])
    return binary_string

# All blocks of 8 bits go back to text.
def decode(binary_string):
    bytes_string = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    byte_number = [int(byte, 2) for byte in bytes_string]
    text = bytes(byte_number).decode('utf-8')
    return text