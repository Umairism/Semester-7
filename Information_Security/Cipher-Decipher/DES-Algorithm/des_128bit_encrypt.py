"""
DES 128-bit (Triple DES / 3DES) Encryption Program
====================================================
Uses a 128-bit (16-byte) key to perform Triple DES encryption.
Two-key TDEA: C = E_K1( D_K2( E_K1( P ) ) )

Dependencies:
    pip install pycryptodome
"""

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import hashlib
import binascii
import sys


def derive_128bit_key(user_key: str) -> bytes:
    """
    Derive a valid 16-byte (128-bit) Triple DES key from any user-provided string.

    DES/3DES keys require odd-parity bits, so we hash the user input
    and then adjust parity to produce a valid key.
    """
    # Hash the user key to get exactly 16 bytes
    raw = hashlib.md5(user_key.encode("utf-8")).digest()  # 16 bytes

    # Adjust parity bits for each byte (DES requires odd parity on each byte)
    adjusted = bytearray(raw)
    for i in range(len(adjusted)):
        byte = adjusted[i] & 0xFE  # clear the lowest bit
        # count number of 1-bits in the upper 7 bits
        ones = bin(byte).count("1")
        # set lowest bit to make total number of 1-bits odd
        if ones % 2 == 0:
            byte |= 1
        adjusted[i] = byte

    key = bytes(adjusted)

    # Verify it's a valid 3DES key (checks parity and weak-key conditions)
    try:
        DES3.adjust_key_parity(key)
    except ValueError:
        # In the rare case of a weak/semi-weak key, flip one parity bit
        adjusted[0] ^= 0x01
        key = bytes(adjusted)

    return key


def encrypt(plaintext: str, user_key: str) -> dict:
    """
    Encrypt plaintext using Triple DES (128-bit key) in CBC mode.

    Args:
        plaintext: The message to encrypt.
        user_key:  Any string provided by the user as the encryption key.

    Returns:
        A dict with 'iv', 'ciphertext', and 'key' (all hex-encoded).
    """
    key = derive_128bit_key(user_key)

    # Generate a random 8-byte IV for CBC mode
    iv = get_random_bytes(8)

    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)

    # Pad plaintext to a multiple of 8 bytes (DES block size)
    padded = pad(plaintext.encode("utf-8"), DES3.block_size)

    ciphertext = cipher.encrypt(padded)

    return {
        "key_hex": binascii.hexlify(key).decode(),
        "iv_hex": binascii.hexlify(iv).decode(),
        "ciphertext_hex": binascii.hexlify(ciphertext).decode(),
    }


def main():
    print("=" * 60)
    print("   DES 128-bit (Triple DES) Encryption Program")
    print("=" * 60)
    print()

    # --- Get user input ---
    user_key = input("Enter encryption key (any text): ").strip()
    if not user_key:
        print("Error: Key cannot be empty.")
        sys.exit(1)

    plaintext = input("Enter plaintext to encrypt : ").strip()
    if not plaintext:
        print("Error: Plaintext cannot be empty.")
        sys.exit(1)

    # --- Encrypt ---
    result = encrypt(plaintext, user_key)

    # --- Display results ---
    print()
    print("-" * 60)
    print("  ENCRYPTION RESULTS")
    print("-" * 60)
    print(f"  Algorithm    : Triple DES (3DES / DES-EDE2)")
    print(f"  Mode         : CBC")
    print(f"  Key size     : 128 bits (16 bytes)")
    print(f"  Block size   : 64 bits  (8 bytes)")
    print()
    print(f"  Derived Key  : {result['key_hex']}")
    print(f"  IV           : {result['iv_hex']}")
    print(f"  Ciphertext   : {result['ciphertext_hex']}")
    print("-" * 60)


if __name__ == "__main__":
    main()
