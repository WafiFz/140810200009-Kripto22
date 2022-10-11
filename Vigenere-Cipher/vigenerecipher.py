'''
Nama        : Wafi Fahruzzaman
NPM         : 140810200009
Deskripsi   : Tugas 5 - Program Vigenere Cipher
'''

import enum

class PROCESS(enum.Enum):
    encrypt = 'encrypt'
    decrypt = 'decrypt'

def vigenere_cipher(method):
    input_text = input("\nInput text\t: ")
    key = input("Input key\t: ")

    key_real = key
    
    while (len(key_real) < len(input_text)):
        key_real += key
    
    if (len(key_real) > len(input_text)):
        n = len(input_text) - len(key_real)
        key_real = key_real[0:n]

    output = ""
    if method == PROCESS.encrypt :
        k=0
        for i in range(len(input_text)):
            if (input_text[i].isupper()):
                output += chr((((ord(input_text[i])-65)+(ord(key_real[k])-65))%26)+65)
                k = k+1
            elif (input_text[i].islower()) :
                output += chr((((ord(input_text[i])-97)+(ord(key_real[k])-97))%26)+97)
                k = k+1
            else :
                output += " "
    elif method == PROCESS.decrypt :
        k=0
        for i in range(len(input_text)):
            if (input_text[i].isupper()):
                output += chr((((ord(input_text[i])-65)-(ord(key_real[k])-65))%26)+65)
                k = k+1
            elif (input_text[i].islower()) :
                output += chr((((ord(input_text[i])-97)-(ord(key_real[k])-97))%26)+97)
                k = k+1
            else :
                output += " "
    else : 
        print("Terjadi kesalahan.")
        return
    
    return output

while True :
    print("\n|--- Menu ---|")
    print("1) Enkripsi\n2) Dekripsi\n3) Exit")
    menu = input("\nPilihan\t: ")

    if menu == '1':
        output = vigenere_cipher(PROCESS.encrypt)
    elif menu == '2':
        output = vigenere_cipher(PROCESS.decrypt)
    elif menu == '3':
        break
    else :
        print("\nError Input.\n")
    
    print("\nHasil\t: " + output)
    print()