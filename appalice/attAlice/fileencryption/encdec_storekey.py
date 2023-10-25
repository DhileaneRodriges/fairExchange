"""
title           : encdec_storekey.py
description     : This programs shows how to generate a symmetric key
                : to encrypt a message, store the key on disk,
                : retrieve it from disk and use it to decrypt
                : the message. 
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
                : bash-3.2$ python enndec_storekey.py
                : decrypted_msg with AB_key_fromdisk:  my deep dark secret
                : decrypted_msg with AB_key:  my deep dark secret
                :
python_version  : Python 3.7.4(v3.7.4:e09359112e, Jul 8 2019, 14:36:03) 
"""

from cryptography.fernet import Fernet

AB_key = Fernet.generate_key()


# encrypt
message = "my deep dark secret".encode()
f = Fernet(AB_key)
encrypted_msg = f.encrypt(message)  
       # Encrypt the bytes. The returning object is of type bytes

# store key on local disk
file = open('alicebob_key.key', 'wb')  # Open the file as wb to write bytes
file.write(AB_key)                     # The key is type bytes still
file.close()

# retrieve key from local disk
file = open('alicebob_key.key', 'rb')  # Open the file as wb to read bytes
AB_key_fromdisk= file.read()           # The key will be type bytes
file.close()

ff = Fernet(AB_key_fromdisk)

# Use key retrieved from disk to decrypt
decrypted_msg = ff.decrypt(encrypted_msg)  
            # Decrypt the bytes. The returning object is of type bytes

print("decrypted_msg with AB_key_fromdisk: ", decrypted_msg.decode())

# To verify decryp the same msg using original AB_key 
decrypted_msg = f.decrypt(encrypted_msg)  
            # Decrypt the bytes. The returning object is of type bytes

print("decrypted_msg with AB_key: ", decrypted_msg.decode())




