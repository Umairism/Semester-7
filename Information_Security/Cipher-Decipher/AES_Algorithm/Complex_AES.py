"""
╔════════════════════════════════════════════════════════════════════════════╗
║                    AES ENCRYPTION - VISUAL IMPLEMENTATION                 ║
║              Advanced Encryption Standard - Step-by-Step                   ║
║                                                                            ║
║  This program demonstrates AES-128 encryption with visual debugging       ║
║  showing each step: SubBytes → ShiftRows → MixColumns → AddRoundKey       ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import numpy as np
from typing import List, Tuple
from Crypto.Cipher import AES as CryptoAES
from Crypto.Random import get_random_bytes
import textwrap


# ═══════════════════════════════════════════════════════════════════════════
#                           AES S-BOX (SUBSTITUTION BOX)
# ═══════════════════════════════════════════════════════════════════════════

SBOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5e, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xd7, 0x4b, 0x55, 0xcf, 0x34, 0xc5, 0x84,
    0xcb, 0xc6, 0x22, 0xbb, 0x20, 0x11, 0xc1, 0x65, 0x57, 0x69, 0x2c, 0x90, 0x13, 0xf0, 0xac, 0xe6,
    0x87, 0x4f, 0x97, 0x75, 0xa7, 0xf2, 0x72, 0xc0, 0xab, 0x81, 0x18, 0xd4, 0x3f, 0xdc, 0x77, 0x13,
    0xfe, 0x5c, 0x97, 0x73, 0x51, 0x4a, 0x49, 0x3e, 0x87, 0x25, 0x36, 0x42, 0x87, 0xe8, 0xb3, 0xea,
]

# Inverse S-Box for decryption
SBOX_INV = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x3f, 0xb9, 0xd1, 0x77, 0x2d, 0x48, 0xd6, 0x4d, 0x7a, 0x0a, 0x61, 0x20, 0xfa, 0x87,
    0xe5, 0xb5, 0x69, 0xfd, 0x36, 0xae, 0x41, 0xc6, 0xc5, 0x05, 0xd8, 0x09, 0x17, 0x51, 0x1b, 0x81,
    0x09, 0xf1, 0xba, 0x4b, 0x3b, 0x24, 0xb4, 0xd5, 0xb5, 0x2e, 0xc0, 0xe0, 0x5e, 0xf1, 0x4f, 0x74,
]

# Round constants (Rcon)
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]


# ═══════════════════════════════════════════════════════════════════════════
#                          UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def print_header(title: str, width: int = 80):
    """Print formatted header"""
    border = "═" * width
    print(f"\n{border}")
    print(f"║ {title.center(width - 4)} ║")
    print(f"{border}\n")


def print_state_matrix(state: List[List[int]], title: str = "State Matrix", decimal: bool = False):
    """Print 4x4 state matrix in a nice format"""
    print(f"\n📊 {title}:")
    print("┌─────────┬─────────┬─────────┬─────────┐")
    for row in state:
        if decimal:
            print(f"│  {row[0]:3d}     │  {row[1]:3d}     │  {row[2]:3d}     │  {row[3]:3d}     │")
        else:
            print(f"│  {row[0]:02x}     │  {row[1]:02x}     │  {row[2]:02x}     │  {row[3]:02x}     │")
        print("├─────────┼─────────┼─────────┼─────────┤")
    print("└─────────┴─────────┴─────────┴─────────┘")


def bytes_to_state(data: bytes) -> List[List[int]]:
    """Convert 16 bytes to 4x4 state matrix (column-major order)"""
    state = [[0] * 4 for _ in range(4)]
    for i in range(16):
        state[i % 4][i // 4] = data[i]
    return state


def state_to_bytes(state: List[List[int]]) -> bytes:
    """Convert 4x4 state matrix back to 16 bytes"""
    data = []
    for col in range(4):
        for row in range(4):
            data.append(state[row][col])
    return bytes(data)


def hex_dump(data: bytes, title: str = "Data") -> str:
    """Create hex dump of bytes"""
    result = f"\n{title}:\n"
    for i in range(0, len(data), 16):
        hex_str = ' '.join(f"{b:02x}" for b in data[i:i+16])
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data[i:i+16])
        result += f"{i:04x}: {hex_str:<48} {ascii_str}\n"
    return result


# ═══════════════════════════════════════════════════════════════════════════
#                      AES CORE TRANSFORMATIONS
# ═══════════════════════════════════════════════════════════════════════════

class AESUnderstander:
    """Educational AES implementation showing each step visually"""
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.round_num = 0
    
    # ─────────────────────────────────────────────────────────────────────
    # STEP 1: SUBSTITUTE BYTES (SubBytes)
    # ─────────────────────────────────────────────────────────────────────
    
    def sub_bytes(self, state: List[List[int]], inverse: bool = False) -> List[List[int]]:
        """
        Substitution transformation using S-box
        
        VISUAL EXPLANATION:
        - S-box is a 16×16 lookup table with non-linear substitution
        - For byte 0xAB: row=0xA(10), col=0xB(11) → SBOX[171] = some value
        - Each byte is replaced independently
        """
        sbox = SBOX_INV if inverse else SBOX
        new_state = [row[:] for row in state]
        
        if self.verbose:
            print(f"\n🔤 STEP 1: SubBytes (Substitute Bytes) - Round {self.round_num}")
            print("─" * 80)
            print("📌 Each byte replaced using S-box lookup table")
            print("   Byte value 0xXY → S-box[256] → New byte value\n")
        
        for i in range(4):
            for j in range(4):
                old_byte = state[i][j]
                new_byte = sbox[old_byte]
                new_state[i][j] = new_byte
                
                if self.verbose and (i < 2 and j < 2):  # Show first few bytes
                    print(f"   [{i},{j}]: 0x{old_byte:02x} → SBOX[{old_byte}] → 0x{new_byte:02x}")
        
        if self.verbose:
            print_state_matrix(state, "Before SubBytes")
            print_state_matrix(new_state, "After SubBytes")
        
        return new_state
    
    # ─────────────────────────────────────────────────────────────────────
    # STEP 2: SHIFT ROWS (ShiftRows)
    # ─────────────────────────────────────────────────────────────────────
    
    def shift_rows(self, state: List[List[int]], inverse: bool = False) -> List[List[int]]:
        """
        Row shifting transformation
        
        VISUAL EXPLANATION:
        Row 0: [a0 a1 a2 a3] → [a0 a1 a2 a3]  (no shift)
        Row 1: [b0 b1 b2 b3] → [b1 b2 b3 b0]  (shift left 1)
        Row 2: [c0 c1 c2 c3] → [c2 c3 c0 c1]  (shift left 2)
        Row 3: [d0 d1 d2 d3] → [d3 d0 d1 d2]  (shift left 3 = right 1)
        
        Inverse: Shift right instead of left
        """
        new_state = [row[:] for row in state]
        
        if self.verbose:
            print(f"\n🔄 STEP 2: ShiftRows (Circular Row Shift) - Round {self.round_num}")
            print("─" * 80)
            print("📌 Each row shifted left by its row number (cyclic)\n")
            print_state_matrix(state, "Before ShiftRows")
        
        if not inverse:
            # Forward: shift left
            new_state[1] = [state[1][1], state[1][2], state[1][3], state[1][0]]
            new_state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
            new_state[3] = [state[3][3], state[3][0], state[3][1], state[3][2]]
        else:
            # Inverse: shift right
            new_state[1] = [state[1][3], state[1][0], state[1][1], state[1][2]]
            new_state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
            new_state[3] = [state[3][1], state[3][2], state[3][3], state[3][0]]
        
        if self.verbose:
            print("\n📍 Shift Operations:")
            print("   Row 0: [a0 a1 a2 a3] → [a0 a1 a2 a3]  (no shift)")
            print("   Row 1: [b0 b1 b2 b3] → [b1 b2 b3 b0]  (shift left 1)")
            print("   Row 2: [c0 c1 c2 c3] → [c2 c3 c0 c1]  (shift left 2)")
            print("   Row 3: [d0 d1 d2 d3] → [d3 d0 d1 d2]  (shift left 3)\n")
            print_state_matrix(new_state, "After ShiftRows")
        
        return new_state
    
    # ─────────────────────────────────────────────────────────────────────
    # STEP 3: MIX COLUMNS (MixColumns)
    # ─────────────────────────────────────────────────────────────────────
    
    def gmul(self, a: int, b: int) -> int:
        """Galois field multiplication (GF(2^8))"""
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xff
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p
    
    def mix_columns(self, state: List[List[int]], inverse: bool = False) -> List[List[int]]:
        """
        Mix columns transformation (matrix multiplication in GF(2^8))
        
        VISUAL EXPLANATION:
        Forward transformation matrix:
        | 2 3 1 1 |
        | 1 2 3 1 |
        | 1 1 2 3 |
        | 3 1 1 2 |
        
        Each column: [s0 s1 s2 s3]^T → multiply by matrix
        """
        new_state = [row[:] for row in state]
        
        if self.verbose:
            print(f"\n🔀 STEP 3: MixColumns (Galois Field Multiplication) - Round {self.round_num}")
            print("─" * 80)
            print("📌 Each column multiplied by transformation matrix in GF(2^8)\n")
            print_state_matrix(state, "Before MixColumns")
        
        if not inverse:
            # Forward mix matrix
            for col in range(4):
                s0, s1, s2, s3 = [state[row][col] for row in range(4)]
                
                new_state[0][col] = self.gmul(0x02, s0) ^ self.gmul(0x03, s1) ^ s2 ^ s3
                new_state[1][col] = s0 ^ self.gmul(0x02, s1) ^ self.gmul(0x03, s2) ^ s3
                new_state[2][col] = s0 ^ s1 ^ self.gmul(0x02, s2) ^ self.gmul(0x03, s3)
                new_state[3][col] = self.gmul(0x03, s0) ^ s1 ^ s2 ^ self.gmul(0x02, s3)
        else:
            # Inverse mix matrix
            for col in range(4):
                s0, s1, s2, s3 = [state[row][col] for row in range(4)]
                
                new_state[0][col] = self.gmul(0x0e, s0) ^ self.gmul(0x0b, s1) ^ self.gmul(0x0d, s2) ^ self.gmul(0x09, s3)
                new_state[1][col] = self.gmul(0x09, s0) ^ self.gmul(0x0e, s1) ^ self.gmul(0x0b, s2) ^ self.gmul(0x0d, s3)
                new_state[2][col] = self.gmul(0x0d, s0) ^ self.gmul(0x09, s1) ^ self.gmul(0x0e, s2) ^ self.gmul(0x0b, s3)
                new_state[3][col] = self.gmul(0x0b, s0) ^ self.gmul(0x0d, s1) ^ self.gmul(0x09, s2) ^ self.gmul(0x0e, s3)
        
        if self.verbose:
            print("\n📍 Matrix Multiplication:")
            print("   Forward:  [2 3 1 1]     Inverse:  [14 11 13 9]")
            print("             [1 2 3 1]               [9  14 11 13]")
            print("             [1 1 2 3]               [13 9  14 11]")
            print("             [3 1 1 2]               [11 13 9  14]\n")
            print_state_matrix(new_state, "After MixColumns")
        
        return new_state
    
    # ─────────────────────────────────────────────────────────────────────
    # STEP 4: ADD ROUND KEY (AddRoundKey)
    # ─────────────────────────────────────────────────────────────────────
    
    def add_round_key(self, state: List[List[int]], round_key: List[List[int]]) -> List[List[int]]:
        """
        Add round key transformation (XOR with round key)
        
        VISUAL EXPLANATION:
        XOR operation: 
        0 ⊕ 0 = 0
        0 ⊕ 1 = 1
        1 ⊕ 0 = 1
        1 ⊕ 1 = 0
        
        Each byte of state XORed with corresponding byte of round key
        """
        new_state = [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]
        
        if self.verbose:
            print(f"\n🔑 STEP 4: AddRoundKey (XOR with Round Key) - Round {self.round_num}")
            print("─" * 80)
            print("📌 State XORed with round key (bitwise XOR each byte)\n")
            print_state_matrix(state, "State Before AddRoundKey")
            print_state_matrix(round_key, "Round Key")
            print("\n📍 XOR Operation for each byte:")
            print("   0 ⊕ 0 = 0 (both 0, result 0)")
            print("   0 ⊕ 1 = 1 (different, result 1)")
            print("   1 ⊕ 0 = 1 (different, result 1)")
            print("   1 ⊕ 1 = 0 (both 1, result 0)\n")
            print_state_matrix(new_state, "State After AddRoundKey (XOR Result)")
        
        return new_state
    
    # ─────────────────────────────────────────────────────────────────────
    # KEY EXPANSION (Key Schedule)
    # ─────────────────────────────────────────────────────────────────────
    
    def rot_word(self, word: List[int]) -> List[int]:
        """Rotate word left by 1 byte"""
        return [word[1], word[2], word[3], word[0]]
    
    def sub_word(self, word: List[int]) -> List[int]:
        """Apply S-box to each byte in word"""
        return [SBOX[b] for b in word]
    
    def expand_key(self, key: bytes) -> List[List[List[int]]]:
        """
        Key expansion for AES-128
        Generates 11 round keys (Round Key 0 through 10)
        """
        if self.verbose:
            print_header("KEY EXPANSION (Key Schedule)")
            print("📌 Generating 11 round keys from 128-bit master key\n")
        
        # Convert key to state matrix
        key_state = bytes_to_state(key)
        if self.verbose:
            print_state_matrix(key_state, "Initial Master Key")
        
        # Expanded key (44 words = 11 round keys × 4 words)
        w = []
        for i in range(4):
            w.append([key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]])
        
        # Generate remaining words
        for i in range(4, 44):
            temp = w[i-1][:]
            
            if i % 4 == 0:
                temp = self.sub_word(self.rot_word(temp))
                temp[0] ^= RCON[(i // 4) - 1]
            
            w.append([w[i-4][j] ^ temp[j] for j in range(4)])
        
        # Group into 11 round keys
        round_keys = []
        for r in range(11):
            round_key = []
            for i in range(4):
                word = w[4*r + i]
                for j in range(4):
                    row = j % 4
                    col = i
                    if round_key.__len__() <= row:
                        round_key.append([])
                    if len(round_key[row]) <= col:
                        round_key[row].append(word[j])
                    else:
                        round_key[row][col] = word[j]
            
            # Construct state matrix for this round key
            rk_state = [[0]*4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    rk_state[i][j] = w[4*r + j][i]
            
            round_keys.append(rk_state)
            
            if self.verbose and r == 0:
                print_state_matrix(rk_state, f"Round Key {r} (Initial)")
        
        if self.verbose:
            print(f"\n✅ Generated {len(round_keys)} round keys for AES-128 (10 rounds + 1 initial)")
        
        return round_keys
    
    # ─────────────────────────────────────────────────────────────────────
    # MAIN ENCRYPTION
    # ─────────────────────────────────────────────────────────────────────
    
    def encrypt_block(self, plaintext: bytes, key: bytes) -> bytes:
        """AES-128 block encryption"""
        print_header("AES-128 ENCRYPTION")
        print(f"🔐 Plaintext:  {plaintext.hex().upper()}")
        print(f"🔑 Key:        {key.hex().upper()}\n")
        
        # Step 1: Expand key schedule
        round_keys = self.expand_key(key)
        
        # Step 2: Convert plaintext to state matrix
        state = bytes_to_state(plaintext)
        
        print_header("INITIAL ROUND")
        print("📌 Before any transformation\n")
        print_state_matrix(state, "Initial Plaintext State")
        
        # Step 3: Initial AddRoundKey
        self.round_num = 0
        state = self.add_round_key(state, round_keys[0])
        
        # Step 4: Main rounds (1-9)
        for round_num in range(1, 10):
            self.round_num = round_num
            
            print_header(f"ROUND {round_num} (Main Transformation)")
            print(f"📌 Applying 4 transformations in sequence\n")
            
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round_keys[round_num])
        
        # Step 5: Final round (no MixColumns)
        self.round_num = 10
        print_header("FINAL ROUND (Round 10)")
        print("📌 Same as other rounds BUT no MixColumns step\n")
        
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, round_keys[10])
        
        # Convert state back to bytes
        ciphertext = state_to_bytes(state)
        
        print_header("ENCRYPTION COMPLETE")
        print(f"🔓 Ciphertext: {ciphertext.hex().upper()}\n")
        
        return ciphertext
    
    def decrypt_block(self, ciphertext: bytes, key: bytes) -> bytes:
        """AES-128 block decryption"""
        print_header("AES-128 DECRYPTION")
        print(f"🔐 Ciphertext: {ciphertext.hex().upper()}")
        print(f"🔑 Key:        {key.hex().upper()}\n")
        
        # Step 1: Expand key schedule
        round_keys = self.expand_key(key)
        
        # Step 2: Convert ciphertext to state matrix
        state = bytes_to_state(ciphertext)
        
        print_header("INITIAL ROUND")
        print("📌 Before any transformation\n")
        print_state_matrix(state, "Initial Ciphertext State")
        
        # Step 3: Initial AddRoundKey (with final round key)
        self.round_num = 10
        state = self.add_round_key(state, round_keys[10])
        
        # Step 4: Main rounds (9-1) - REVERSED
        for round_num in range(9, 0, -1):
            self.round_num = round_num
            
            print_header(f"DECRYPTION ROUND {11 - round_num}")
            print(f"📌 Applying inverse transformations in reverse\n")
            
            state = self.shift_rows(state, inverse=True)
            state = self.sub_bytes(state, inverse=True)
            state = self.add_round_key(state, round_keys[round_num])
            state = self.mix_columns(state, inverse=True)
        
        # Step 5: Final round (no MixColumns)
        self.round_num = 0
        print_header("FINAL DECRYPTION ROUND")
        print("📌 No MixColumns in final round\n")
        
        state = self.shift_rows(state, inverse=True)
        state = self.sub_bytes(state, inverse=True)
        state = self.add_round_key(state, round_keys[0])
        
        # Convert state back to bytes
        plaintext = state_to_bytes(state)
        
        print_header("DECRYPTION COMPLETE")
        print(f"🔓 Plaintext:  {plaintext.hex().upper()}\n")
        
        return plaintext


# ═══════════════════════════════════════════════════════════════════════════
#                          USAGE EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════

def example_1_visual_encryption():
    """Example 1: Encrypt "Hello World!!!!!" with visual explanations"""
    print("\n" + "="*80)
    print("EXAMPLE 1: SIMPLE MESSAGE ENCRYPTION WITH VISUAL STEPS")
    print("="*80)
    
    plaintext = b"Hello World!!!!!"  # 16 bytes
    key = b"MySecretKey12345"        # 16 bytes (128 bits)
    
    understander = AESUnderstander(verbose=True)
    ciphertext = understander.encrypt_block(plaintext, key)
    
    # Verify decryption
    decrypted = understander.decrypt_block(ciphertext, key)
    print(f"\n✅ Verification: Decrypted matches original: {decrypted == plaintext}")


def example_2_different_keys():
    """Example 2: Show how different keys produce different ciphertexts"""
    print("\n" + "="*80)
    print("EXAMPLE 2: SAME PLAINTEXT, DIFFERENT KEYS = DIFFERENT CIPHERTEXTS")
    print("="*80)
    
    plaintext = b"SameMsg12345678"  # Make sure it's 16 bytes
    plaintext = plaintext + b"X"  # Now 16 bytes
    key1 = b"Key1234567890ABC"
    key2 = b"Key1234567890ABD"  # Changed last byte
    
    understander = AESUnderstander(verbose=False)
    
    ciphertext1 = understander.encrypt_block(plaintext, key1)
    print(f"\nKey 1: {key1}")
    print(f"→ Ciphertext: {ciphertext1.hex().upper()}")
    
    ciphertext2 = understander.encrypt_block(plaintext, key2)
    print(f"\nKey 2: {key2}")
    print(f"→ Ciphertext: {ciphertext2.hex().upper()}")
    
    print(f"\n📊 Ciphertexts are completely different despite 1-byte difference!")


def example_3_detailed_single_round():
    """Example 3: Show just one round in detail"""
    print("\n" + "="*80)
    print("EXAMPLE 3: SINGLE ROUND DETAILED BREAKDOWN")
    print("="*80)
    
    plaintext = b"Test1234Test1234"
    key = b"MyKey123MyKey123"
    
    understander = AESUnderstander(verbose=True)
    round_keys = understander.expand_key(key)
    
    state = bytes_to_state(plaintext)
    state = understander.add_round_key(state, round_keys[0])
    
    understander.round_num = 1
    print_header("ROUND 1 - DETAILED")
    state = understander.sub_bytes(state)
    state = understander.shift_rows(state)
    state = understander.mix_columns(state)
    state = understander.add_round_key(state, round_keys[1])


def example_4_cryptolib_comparison():
    """Example 4: Compare with standard crypto library"""
    print("\n" + "="*80)
    print("EXAMPLE 4: COMPARE WITH PYCRYPTODOME LIBRARY")
    print("="*80)
    
    plaintext = b"ComparisonTest!!"
    key = b"CryptoKeyForTest"
    
    # Using our implementation
    understander = AESUnderstander(verbose=False)
    our_ciphertext = understander.encrypt_block(plaintext, key)
    
    # Using pycryptodome
    cipher = CryptoAES.new(key, CryptoAES.MODE_ECB)
    lib_ciphertext = cipher.encrypt(plaintext)
    
    print(f"Our AES-128:      {our_ciphertext.hex().upper()}")
    print(f"PyCryptodome:     {lib_ciphertext.hex().upper()}")
    print(f"✅ Match: {our_ciphertext == lib_ciphertext}")


# ═══════════════════════════════════════════════════════════════════════════
#                              MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n")
    print("╔" + "═"*78 + "╗")
    print("║" + "AES ENCRYPTION - EDUCATIONAL VISUAL IMPLEMENTATION".center(78) + "║")
    print("║" + "Understanding each step of AES-128 encryption".center(78) + "║")
    print("╚" + "═"*78 + "╝")
    
    import sys
    
    if len(sys.argv) > 1:
        example = sys.argv[1]
        if example == "1":
            example_1_visual_encryption()
        elif example == "2":
            example_2_different_keys()
        elif example == "3":
            example_3_detailed_single_round()
        elif example == "4":
            example_4_cryptolib_comparison()
        else:
            print("Usage: python AES_encryption.py [1|2|3|4]")
    else:
        # Run all examples
        example_1_visual_encryption()
        example_2_different_keys()
        example_3_detailed_single_round()
        example_4_cryptolib_comparison()
    
    print("\n" + "="*80)
    print("🎓 LEARNING POINTS:")
    print("="*80)
    print("""
1. SUBBYTES: Non-linear transformation preventing linear attacks
2. SHIFTROWS: Diffusion across columns (spread changes horizontally)
3. MIXCOLUMNS: Galois field math providing algebraic diffusion
4. ADDROUNDKEY: XOR with round key (simple but crucial for security)

5. KEY EXPANSION: 128-bit key expanded to 11 round keys (44 words)
6. 10 ROUNDS: Each with all 4 transformations
7. FINAL ROUND: Skips MixColumns (why? For invertibility of key schedule)

🔐 Security Properties:
- Confusion: S-box makes each output bit depend on all input bits
- Diffusion: ShiftRows + MixColumns spread input bits across output
- Key Expansion: Each round key completely different from master key
- Avalanche Effect: 1-bit change → affects ~50% of output bits
    """)
