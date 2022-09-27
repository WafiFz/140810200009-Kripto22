import enum
import numpy as np

# helper general #

class PROCESS(enum.Enum):
    encrypt = 'encrypt'
    decrypt = 'decrypt'

def char_to_num(x):
    x = ord(x)-65
    return x

def num_to_char(x):
    x = chr(x+65)
    return x

def mod_inverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def input_text(string):
    text = input("Input " + string + ": ")
    text = text.replace(' ', '').upper()
    
    return text

# helper hill cipher #
def input_key(n):
    key = list(map(int, input("Masukkan nilai key matrix (dipisahkan koma): ").split(",")))
    key = np.array(key).reshape(n, n) % 26
    
    print("Matrix Key: ")
    print(key)
    
    return key

def vector(text, m):
    text_in_number = list(map(char_to_num, list(text)))
    return np.array(text_in_number).reshape(int(len(text)/m), m)

def determinan_with_validation(matrix):
    determinan = int(np.linalg.det(matrix))
    if determinan % 2 == 0 or determinan == 13 :
        print("Determinan key harus ganjil dan selain 13!")
        exit()
    
    return determinan

def inverse(determinan, matrix):
    return (mod_inverse(determinan % 26, 26) * np.round(determinan * np.linalg.inv(matrix)).astype(int) % 26)