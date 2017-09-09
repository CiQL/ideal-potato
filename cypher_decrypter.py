#!/usr/bin/python3
import string
def cipher(file, is_decipher):
    '''Encrypts and decrypts a string with its backwards alphabet'''
    f = file_prep(file)
    if is_decipher:
        alpha       = string.ascii_lowercase
        shift_alpha = alpha[::-1]
    else:
        shift_alpha = string.ascii_lowercase
        alpha       = shift_alpha[::-1]
    table = str.maketrans(alpha, shift_alpha)
    print(f.translate(table))

def file_len(file):
    '''Counts the number of lines in file'''
    with open(file, "r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def file_prep(file):
    '''Prepares file for encryption/decryption'''
    f = ""
    #q = file_len(file)
    with open(file, "r") as fc:
        for i, l in enumerate(fc):
            f += l
    f.splitlines()
    return f

if __name__ == "__main__":
    i = True
    while i:
        q = input("Encipher or decipher? (E/D): ")
        if (q.lower() == 'e'):
            ftype = False
            i = False
        elif (q.lower() == 'd'):
            ftype = True
            i = False
        else:
            print("Error: proper inputs are E or D")
    f = input("Enter file name: ")
    cipher(f, ftype)
