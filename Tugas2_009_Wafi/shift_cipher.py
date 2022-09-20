'''
Nama        : Wafi Fahruzzaman
NPM         : 140810200009
Deskirosi   : Tugas 2 - Program Shift Cipher
'''

import enum

class PROCESS(enum.Enum):
    encrypt = 'encrypt'
    decrypt = 'decrypt'

def shift_cipher(method):
    input_text = input("\nInput text\t: ")
    key = int(input("Input key\t: "))
    output = ""
    if method == PROCESS.encrypt :
        for char in input_text:
            if (char.isupper()):
                output += chr((((ord(char)-65)+key)%26)+65)
            elif (char.islower()) :
                output += chr((((ord(char)-97)+key)%26)+97)
            else :
                output += " "
    elif method == PROCESS.decrypt :
        for char in input_text:
            if (char.isupper()):
                output += chr((((ord(char)-65)-key)%26)+65)
            elif (char.islower()) :
                output += chr((((ord(char)-97)-key)%26)+97)
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
        output = shift_cipher(PROCESS.encrypt)
    elif menu == '2':
        output = shift_cipher(PROCESS.decrypt)
    elif menu == '3':
        break
    else :
        print("\nError Input.\n")
    
    print("\nHasil\t: " + output)
    print()