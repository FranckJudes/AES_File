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
    return 'Opération effectuée'

def decryptFile(password, IV, filename):
    key = hashlib.sha256(password.encode()).digest()

    with open(filename, 'rb') as ef:
        en_file_data = ef.read()

    cipher = AES.new(key, AES.MODE_CBC, IV)
    decrypted_data = cipher.decrypt(en_file_data)
    original_file_data = Padding.unpad(decrypted_data, 16)

    with open(filename, 'wb') as f:
        f.write(original_file_data)
    return 'Opération effectuée'

def encrypt_folder(foldername, password):
    b = ''  # Initialisez la variable b avec une chaîne vide
    for subdir, _, files in os.walk(foldername):
        for file in files:
            filepath = os.path.join(subdir, file)
            b += encryptFile(password, b'P0123as235a145df', filepath)  # Ajoutez le résultat à b
    print(b)

def decrypt_folder(foldername, password):
    b = ''  # Initialisez la variable b avec une chaîne vide
    for subdir, _, files in os.walk(foldername):
        for file in files:
            filepath = os.path.join(subdir, file)
            b += decryptFile(password, b'P0123as235a145df', filepath)  # Ajoutez le résultat à b
    print(b)

if len(sys.argv) < 4:
    print('Utilisation : python script.py [option] [dossier] [mot de passe]')
    sys.exit(1)

if sys.argv[1] == '-eF':
    encrypt_folder(sys.argv[2], sys.argv[3])
elif sys.argv[1] == '-dF':
    decrypt_folder(sys.argv[2], sys.argv[3])
else:
    print('Mauvais choix!')

