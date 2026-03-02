from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

def decrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        iv_from_file = f.read(16)
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv_from_file)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
