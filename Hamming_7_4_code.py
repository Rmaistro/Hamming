from Class_vectors_and_matrices import vector
from Class_vectors_and_matrices import matrix
import numpy as np
import random
import string as rijtje
import copy
def text_to_binary(text):
    """
    Transforms every message into a string of binary-code.
    """
    byte_number = text.encode('utf-8')
    binary_str = ''
    for byte in byte_number:
        binary_str += format(byte, '08b')          
    return binary_str
def text_to_nibbles(a):
    """
    Lets all messages be written in binairy blcks of 4 bits (nibble). Since 
    every caracter gets transformed into a byte, we can defenitly devide into 
    nibble (half a byte). Returns a list with string-nibbles as elements.
    """
    text=text_to_binary(a)
    code=[]
    for i in range(0,len(text),4):
        code.append(text[i:i+4])
    return code
def binary_to_text(binary_string):
    """
    Takes a string of binary and returns it to normal code.
    """
    bytes_string = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    byte_number = [int(byte, 2) for byte in bytes_string]
    text = bytes(byte_number).decode('utf-8')
    return text
def nibble_to_text(a):
    """
    Takes the code as produced in text_to_nibbles and transforms it back 
    to text.
    """
    text=''
    for i in range(len(a)):
        text+=a[i]
    return binary_to_text(text)
#==================Matrix-defenition-area below================================
# Secures message by adding 3 extra bits.
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
#==================Matrix-defenition-area above================================
def encrypt74(message_4, generator_matrix):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. It returns the same code with after it the security-bits. 
    In the form of a matrix size 1 x (n+the security-bits).
    """
    if message_4.shape()[1] == generator_matrix.shape()[0]:
        return message_4.XOR(generator_matrix)
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
def correct (a,Parity_check):
    """
    This code correct a 7 bit long code, given as a 7X1-matrix. 
    """
    wrong = parity(a,Parity_check)
    if wrong == "None":
        return a
    else:
        new=a.get_element((wrong,0))^1
        return a.change_element((wrong,0),new)
def decrypt74(corrected, Return): 
    """
    Takes a nx1-matrix m. After multiplaction of a matrix with m,
    the original output is displayed as een 1 x n- matix
    """
    return Return*corrected
def string_to_vmatrix(a):
    "Transforms a string to vertical matix with width 1"
    lst=[]
    for i in range(len(a)):
        lst.append([int(a[i])])
    return matrix(lst)
def string_to_hmatrix(a):
    "Transforms a string to horizontal matix with height 1"
    lst=[[]]
    for i in range(len(a)):
        lst[0].append(int(a[i]))
    return matrix(lst)
def total_check(a):
    """
    After giving a 7-bit long code, secured with Hamming (7,4), this code 
    returns the (corrected) original code. The input has to be given as a 
    1x7 matrix/vector. 
    """
    new=correct(a,Parity_check)
    original =decrypt74(new,Return_matrix)
    return original.to_string()
def ready_to_go(a):
    """
    After given a string input lengt 7 in binary, this return it's string-
    encryption
    """
    code=string_to_hmatrix(a)
    new_code=encrypt74(code,Generator_matrix)
    return new_code.to_string()
def text_encryption_displayable(a):
    """
    This code takes a piece of string and secures it using the Hamming(7,4),
    method.It returns a list full of 7-bit long strings.
    """
    code=text_to_nibbles(a)
    for i in range(len(code)):
        code[i]=ready_to_go(code[i])
    return code
def text_decryption(a):
    """
    This code takes a list, as could be produces by "text_encryption_displayable"
    and returns te message in normal caracters.
    """
    for i in range(len(a)):
        a[i]=string_to_vmatrix(a[i])
        a[i]=total_check(a[i])
    return nibble_to_text(a)
def random_flipping(a):
    """
    Takes the total number n of 7-bit long pieces in a. Then flips a random bit!
    The deepcopy is neccesary because otherwise this function wil keep referring
    to the input, so the original will be changed...
    """
    b=copy.deepcopy(a)
    random_number=random.randint(0, len(b)-1)
    random_position=random.randint(0,6)
    new=list(b[random_number])
    new[random_position]=int(new[random_position])^1
    back=''
    for i in range(len(new)):
        back=back+str(new[i])
    b[random_number]=back
    return b
def random_testing(n):
    """
    Generates a n caracter long string. After that is tests wether the code 
    works based on error-correction! Somewhere in the string a bit wil get 
    flipped!
    """
    random_text = ''.join(random.choices(rijtje.ascii_letters + rijtje.digits, k=n))
    lijst=text_encryption_displayable(random_text)
    #time to change one bit in every 7-bit string!
    flipped=random_flipping(lijst)
    retrieve=text_decryption(flipped)
    if random_text==retrieve:
        return"It all seems to work alright: '%s' was correctly transferred!" %(random_text)
    else:
        return "That's not correct, something went wrong..."
