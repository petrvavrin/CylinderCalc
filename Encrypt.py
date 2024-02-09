# Version 1

import os
import shutil
from cryptography.fernet import Fernet

path_to_dir = './files'

# key generation
key = Fernet.generate_key()
 
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

encrypt_request = input('Archieve and encrypt all files? ')

if encrypt_request.lower() == 'y':
    print('Making zip')
    shutil.make_archive('encrypted files', 'zip', path_to_dir)

    # opening the key
    print('Opening key')
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open('encrypted files.zip', 'rb') as file:
        original = file.read()

    # encrypting the file
    print('Encrypting file')
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open('encrypted files.zip', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print('Encryption complete')

    delete_request = input('Delete old files? ')
    if delete_request.lower() == 'y':
        if os.path.exists("files"):
            shutil.rmtree("files")
            print('Deleted')
        else:
            print("The folder does not exist")
    else:
        exit(0)



else:
   exit(0)