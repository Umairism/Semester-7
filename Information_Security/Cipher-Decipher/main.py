from encrypt_decrypt import encrypt, decrypt
from xor_cipher import xor_cipher


if __name__ == "__main__":
    plaintext = input("Enter text to encrypt: ")

    # ROT13 + Substitution Cipher
    encrypted = encrypt(plaintext)
    decrypted = decrypt(encrypted)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    # XOR Cipher demo
    key = input("\nEnter key for XOR cipher: ")
    xor_encrypted = xor_cipher(plaintext, key)
    xor_decrypted = xor_cipher(xor_encrypted, key)

    print(f"\n--- XOR Cipher ---")
    print(f"Original:  {plaintext}")
    print(f"Key:       {key}")
    print(f"Encrypted: {repr(xor_encrypted)}")
    print(f"Decrypted: {xor_decrypted}")
