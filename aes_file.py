import os
import hashlib
import sys
from Crypto.Cipher import AES
from Crypto.Util import Padding

def encryptFile(password, IV, filename):
    key = hashlib.sha256(password.encode()).digest()

    with open(filename, 'rb') as f:
        file_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded_file_data = Padding.pad(file_data, 16)
    encrypted_data = cipher.encrypt(padded_file_data)

    with open(filename, 'wb') as f:
        f.write(encrypted_data)
    return 'Fichier chiffré avec succès'

def decryptFile(password, IV, filename):
    key = hashlib.sha256(password.encode()).digest()

    with open(filename, 'rb') as ef:
        en_file_data = ef.read()

    cipher = AES.new(key, AES.MODE_CBC, IV)
    decrypted_data = cipher.decrypt(en_file_data)
    original_file_data = Padding.unpad(decrypted_data, 16)

    with open(filename, 'wb') as f:
        f.write(original_file_data)
    return 'Fichier déchiffré avec succès'

if len(sys.argv) < 4:
    print('Utilisation : python script.py [option] [fichier] [mot de passe]')
    sys.exit(1)

if sys.argv[1] == '-e':
    print(encryptFile(sys.argv[3], b'P0123as235a145df', sys.argv[2]))
elif sys.argv[1] == '-d':
    print(decryptFile(sys.argv[3], b'P0123as235a145df', sys.argv[2]))
else:
    print('Mauvais choix! Utilisation : python script.py [option] [fichier] [mot de passe]')
