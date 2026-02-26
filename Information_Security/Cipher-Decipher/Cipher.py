def rot13(text):
    """Apply ROT13 transposition cipher"""
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)


def substitution_cipher(text, shift):
    """Apply substitution cipher with modular shift"""
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)


def xor_cipher(text, key):
    """Encrypt/Decrypt using XOR cipher with a repeating key.
    
    XOR is symmetric — the same function is used for both
    encryption and decryption with the same key.
    """
    result = []
    for i, char in enumerate(text):
        xored = ord(char) ^ ord(key[i % len(key)])
        result.append(chr(xored))
    return ''.join(result)


def encrypt(plaintext, shift=3):
    """Encrypt using ROT13 then substitution"""
    step1 = rot13(plaintext)
    step2 = substitution_cipher(step1, shift)
    return step2


def decrypt(ciphertext, shift=3):
    """Decrypt using reverse substitution then ROT13"""
    step1 = substitution_cipher(ciphertext, -shift)
    step2 = rot13(step1)
    return step2


# Example usage
if __name__ == "__main__":
    plaintext = input("Enter text to encrypt: ")
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