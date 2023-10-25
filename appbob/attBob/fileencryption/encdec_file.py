"""
title           : encdec_file.py
description     : This programs shows how to generate a symmetric key
                : to encrypt a file. 
                :
source          : https://nitratine.net/blog/post/encryption-
                : and-decryption-in-python/ 
                : 
author          : Carlos Molina-Jimenez,
                : carlos.molina@cl.cam.ac.uk
date            : 10 Sep 2023, Computer Lab, University of Cambridge
version         : __ 
usage           : 
notes           :
compile and run : 
                :
                : bash-3.2$ python enndec_file.py
                : alicebob key has been retrieved from alicebob_key.key
                : ... ...
                :
python_version  : Python 3.7.4(v3.7.4:e09359112e, Jul 8 2019, 14:36:03) 
"""

from cryptography.fernet import Fernet

#key = b'' # Use one of the methods to get a key (it must be the same when decrypting)

# retrieve key from local disk
file = open('alicebob_key.key', 'rb')  # Open the file as wb to read bytes
key= file.read()           # The key will be type bytes
file.close()
print("\nalicebob key has been retrieved from alicebob_key.key\n")

input_file = 'test_file.txt'
output_file = 'test_file.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file
print("\nPlain text from input file has been retreived.\n")

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file
print("\nEncrypted text has been stored in output file.\n")

# Note: You can delete input_file here if you want


print("\n\n\n Decrypting process ...\n")

#from cryptography.fernet import Fernet, InvalidToken
#key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)

# retrieve key from local disk
file = open('alicebob_key.key', 'rb')  # Open the file as wb to read bytes
key= file.read()           # The key will be type bytes
file.close()
print("\nalicebob key has been retrieved from alicebob_key.key\n")

input_file = 'test_file.encrypted'
output_file = 'test_file_decrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the encrypted file
print("\n Encrypted text from encrypted file has been retreived.\n")

fernet = Fernet(key)
try:
   decrypted = fernet.decrypt(data)
   print("\n Text has been decrypted using alicebob_key.\n")

   with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file
   print("\nPlain text: ", decrypted.decode())
   print("\n Plain text has been stored to output file.\n")

   # Note: You can delete input_file here if you want
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")

