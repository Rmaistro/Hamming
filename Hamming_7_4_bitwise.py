from Class_vectors_and_matrices import vector
from Class_vectors_and_matrices import matrix
import numpy as np
import random
import string as rijtje
import copy
import time 
import matplotlib.pyplot as plt
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

def encrypt74(mess):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. It returns the same code with after it the security-bits. 
    In the form of a matrix size 1 x (n+the security-bits).
    """
    if len(mess) !=4:
        return None
    else:
        x=str(int(mess[0])^int(mess[1])^int(mess[3]))
        y=str(int(mess[0])^int(mess[2])^int(mess[3]))
        z=str(int(mess[1])^int(mess[2])^int(mess[3]))
    return mess+x+y+z
def parity(mess):
    """
    This functions takes a piece of binary code, given in the form of a matrix 
    with size 1 x n. At which index the original code should be flipped, if 
    neccesary. 
    """
    x=True
    y=True
    z=True
    if mess[4]!=str(int(mess[0])^int(mess[1])^int(mess[3])):
        x=False
    if mess[5]!=str(int(mess[0])^int(mess[2])^int(mess[3])):
        y=False
    if mess[6]!=str(int(mess[1])^int(mess[2])^int(mess[3])):
        z=False
        
    if x==True and y==True and z==True:
        return "None"
    elif x==True and y==True and z==False:
        return 6
    elif x==True and y==False and z==True:
        return 5  
    elif x==True and y==False and z==False:
        return 2
    elif x==False and y==True and z==True:
        return 4
    elif x==False and y==True and z==False:
        return 1
    elif x==False and y==False and z==True:
        return 0
    elif x==False and y==False and z==False:
        return 3
def correct (a):
    """
    This code correct a 7 bit long code, given as a 7X1-matrix. 
    """
    wrong = parity(a)
    if wrong == "None":
        return a
    else:
        new=list(a)
        new[wrong]=int(new[wrong])^1
    total=''
    for i in range(len(new)):
        total=total+str(new[i])
    return total
def decrypt74(corrected): 
    """
    Takes a nx1-matrix m. After multiplaction of a matrix with m,
    the original output is displayed as een 1 x n- matix
    """
    return corrected[:4]
def total_check(a):
    """
    After giving a 7-bit long code, secured with Hamming (7,4), this code 
    returns the (corrected) original code. The input has to be given as a 
    1x7 matrix/vector. 
    """
    new=correct(a)
    return decrypt74(new)
def ready_to_go(a):
    """
    After given a string input length 7 in binary, this return it's string-
    encryption
    """
    new_code=encrypt74(a)
    return new_code
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
    
def time_loop(n):
    i=1
    total=0
    while i <=500:
        starttime=time.time()   
        random_testing(n)
        eindtijd=time.time()
        verstreken_tijd=eindtijd-starttime
        i+=1
        total+=verstreken_tijd
    return total/100

def complexity_analysis():  
    n_lst = []
    time_lst = []
    for i in range(30,330,10):
        n_lst.append(int(i))
        time_lst.append(time_loop(int(i)))
    n_arr = np.array(n_lst)
    time_arr = np.array(time_lst)
    
    time_arr = 1000*time_arr #omzetten van seconden naar milliseconden
    plt.figure()
    plt.scatter(n_arr, time_arr)
    plt.xlabel('Length teststring')
    plt.ylabel('Time (ms)')
    plt.title('Complexity of the bitwise implementation')
    plt.xlim(0, max(n_arr)+10)
    plt.ylim(0, max(time_arr)+2)
    plt.show()
    
inp = input("Type 'analysis' if you want to perform an complexity analysis, type 'codecheck' if you want to check whether or not the code works, type 'encrypt' if you want to encrypt a message or 'decrypt' if you want to decrypt and if needed correct a message: ")
if inp == 'analysis':
    complexity_analysis()
elif inp == 'encrypt':
    text = input('Give the text you want to encrypt here: ')
    print(text_encryption_displayable(text))
elif inp == 'decrypt':
    message = input('Give your decrypted message here: ')
    message = message[2:-2]
    message_lst = message.split("', '")
    print(text_decryption(message_lst))
elif inp == 'codecheck':
    n=input("How long should the test string be? Give an positive interger as answer: ")
    print(random_testing(int(n)))
