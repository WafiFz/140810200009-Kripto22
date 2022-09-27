'''
Nama        : Wafi Fahruzzaman
NPM         : 140810200009
Deskirosi   : Tugas 3 - Program Hill Cipher
'''

import helper as helper
import numpy as np

def hill_cipher(process, text, key, n):    
    determinan_key = helper.determinan_with_validation(key)
    
    if(len(text) % n != 0) :
        last_char = text[-1]
        text = last_char*(n - len(text) % n)
        
    text_vector = helper.vector(text, n)
    result = np.array([], dtype=int)
    
    if process == helper.PROCESS.decrypt:
        key = helper.inverse(determinan_key, key)

    for i in range(len(text_vector)):
            temp = np.matmul(key, text_vector[i].reshape(n, 1)) % 26
            result = np.append(result, temp)
   
    result = list(map(helper.num_to_char, result))
        
    output = ''.join(result)
    
    return output

def solve_key(plaintext, ciphertext, m):
    p_vector = helper.vector(plaintext, m)
    p_matrix = np.array([], dtype=int)
    
    c_vector = helper.vector(ciphertext, m)
    c_matrix = np.array([], dtype=int)
    
    for i in range(m):
        c_matrix = np.append(c_matrix, c_vector[i])
        p_matrix = np.append(p_matrix, p_vector[i])
        
    c_matrix = np.transpose(c_matrix.reshape(m,m))
    p_matrix = np.transpose(p_matrix.reshape(m,m))
    
    p_det = helper.determinan_with_validation(p_matrix)
    p_inverse = helper.inverse(p_det, p_matrix)
    
    result = np.matmul(c_matrix, p_inverse) % 26
    return result
    

while True :
    print("\n|--- Menu ---|")
    print("1) Enkripsi\n2) Dekripsi\n3) Cari Key\n4) Exit")
    menu = input("\nPilihan\t: ")

    if menu == '1' or menu == '2':
        ukuran_matrix = int(input("\nInput ukuran (n) matrix key [n x n]: "))
        key = helper.input_key(ukuran_matrix)

        text = helper.input_text("text")
        if(len(text) < ukuran_matrix):
            print("terjadi ketidaksesuaian antara ukuran matrix key dan jumlah karakter")
            exit()
                
        if(menu == '1'):
            print("\n== Enkripsi ==")
            print("Plaintext\t: " + text)
            print("Ciphertext\t: " + hill_cipher(helper.PROCESS.encrypt, text, key, ukuran_matrix))
        elif menu == '2':
            print("\n== Dekripsi ==")
            print("Ciphertext\t: " + text)
            print("Plaintext\t: " + hill_cipher(helper.PROCESS.decrypt, text, key, ukuran_matrix))     
            
    elif menu == '3':
        print("\n")
        plaintext = helper.input_text("plaintext")
        ciphertext = helper.input_text("ciphertext")
        m = int(input("\nInput nilai m: "))
        
        print("\nPlaintext: " + plaintext + "\nCiphertext: " + ciphertext)
        key = solve_key(plaintext, ciphertext, m)
        
        print("key:")
        print(key)
        
    elif menu == '4':
        exit()
        
    else :
        print("\nError Input.\n")