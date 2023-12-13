import sys

def xor_encrypt(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encrypted_data = bytearray(data[i] ^ password[i % len(password)] for i in range(len(data)))

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def xor_decrypt(input_file, output_file, password):
    xor_encrypt(input_file, output_file, password)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("Encrypt: $ python xor.py message.txt password")
        print("Decrypt: $ python xor.py message.txt.xor password")
        sys.exit(1)

    input_file = sys.argv[1]
    password = sys.argv[3]

    if sys.argv[1].endswith(".xor"):
        # Decrypt
        output_file = sys.argv[1][:-4]  # Remove the ".xor" extension
        xor_decrypt(input_file, output_file, password)
        print(f"Decryption successful. Output written to {output_file}")
    else:
        # Encrypt
        output_file = f"{input_file}.xor"
        xor_encrypt(input_file, output_file, password)
        print(f"Encryption successful. Output written to {output_file}")
