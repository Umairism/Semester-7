from rot13 import rot13
from substitution_cipher import substitution_cipher


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
