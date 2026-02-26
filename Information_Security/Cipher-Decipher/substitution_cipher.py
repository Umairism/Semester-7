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
