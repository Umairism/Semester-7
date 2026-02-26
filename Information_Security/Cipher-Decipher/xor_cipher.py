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
