import secrets
import random

def xor_bytes(byte_str1, byte_str2):
    result = bytes(x ^ y for x, y in zip(byte_str1, byte_str2))
    return result

def encryption(msg):
    size = len(msg)
    k = secrets.randbits(256)
    k_once = k
    key = b''
    
    while len(key) < size:
        random.seed(k_once)
        key += random.randbytes(1246)
        k_once += 1
    key = key[:size]

    return xor_bytes(key,msg),k

def decryption(ct,k):
    size = len(ct)
    k_once = k
    key = b''
    while len(key) < size:
        random.seed(k_once)
        key += random.randbytes(1246)
        k_once += 1
    key = key[:size]
        
    return xor_bytes(key,ct)

if __name__ == '__main__':
    print('Bienvenue dans cet algorithme de chiffrement symétrique.')
    choice = input('Entrez 1 pour chiffrer, 2 pour déchiffrer : ')
    if choice == '1':
        f = input('Entrez le nom de fichier à chiffrer : ')
        ext=f.split('.')[-1]

        with open(f,'rb') as file:
            msg = file.read()
        ct,k = encryption(msg)
        with open('encrypted.'+ext,'w') as encrypted:
            encrypted.write(ct.hex())
        
        print('Votre clé est :',k)
    
    elif choice == '2':
        f = input('Entrez le nom de fichier à déchiffrer : ')
        ext=f.split('.')[-1]
        key = int(input('Entrez votre clé : '))
        f = open(f,'r')
        ct = ''
        for l in f:
            ct += l
        ct = bytes.fromhex(ct)
        msg = decryption(ct,key)
        
        with open('retrieved.'+ext,'wb') as decrypted:
            decrypted.write(msg)
