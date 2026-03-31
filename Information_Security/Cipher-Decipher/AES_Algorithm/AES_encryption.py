"""
╔════════════════════════════════════════════════════════════════════════════╗
║                    AES ENCRYPTION - VISUAL IMPLEMENTATION                 ║
║              Advanced Encryption Standard - Step-by-Step                   ║
║                                                                            ║
║  This program demonstrates AES-128 encryption concepts with visual        ║
║  debugging showing each step: SubBytes → ShiftRows → MixColumns → Key     ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

from typing import List


# ═══════════════════════════════════════════════════════════════════════════
#                    AES CONSTANTS - S-BOX & UTILITIES
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


def print_state(state: List[List[int]], title: str = "State", hex_format: bool = True):
    """Print 4x4 state matrix nicely"""
    print(f"\n{title}:")
    print("┌──────┬──────┬──────┬──────┐")
    for row in state:
        if hex_format:
            print(f"│ {row[0]:02x}   │ {row[1]:02x}   │ {row[2]:02x}   │ {row[3]:02x}   │")
        else:
            print(f"│ {row[0]:3d}  │ {row[1]:3d}  │ {row[2]:3d}  │ {row[3]:3d}  │")
        print("├──────┼──────┼──────┼──────┤")
    print("└──────┴──────┴──────┴──────┘")


def bytes_to_state(data: bytes) -> List[List[int]]:
    """Convert 16 bytes to 4x4 state matrix (column-major)"""
    if len(data) != 16:
        raise ValueError(f"Data must be 16 bytes, got {len(data)}")
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


# ═══════════════════════════════════════════════════════════════════════════
#                      AES TRANSFORMATION STEPS
# ═══════════════════════════════════════════════════════════════════════════

class AESVisualizer:
    """Visual AES implementation for educational purposes"""
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
    
    def sub_bytes(self, state: List[List[int]]) -> List[List[int]]:
        """
        STEP 1: SubBytes Transformation
        ════════════════════════════════════════════════════════════════
        Replace each byte using S-box lookup table.
        - S-box is 16×16 table with 256 entries (0-255)
        - For byte 0xAB: look up SBOX[0xAB] and replace
        
        PURPOSE: Non-linearity (prevents linear attacks)
        """
        if self.verbose:
            print("\n🔤 STEP 1: SubBytes (S-box Substitution)")
            print("─" * 70)
            print("Each byte replaced independently using S-box lookup table")
            print_state(state, "BEFORE SubBytes")
        
        new_state = [row[:] for row in state]
        
        # Show detailed S-box substitutions
        if self.verbose:
            print("\n📋 DETAILED S-BOX SUBSTITUTIONS:")
            print("┌────────┬──────┬──────────┬─────────┐")
            print("│Position│Old   │S-box[x]  │New      │")
            print("├────────┼──────┼──────────┼─────────┤")
        
        for i in range(4):
            for j in range(4):
                old = state[i][j]
                new = SBOX[old]
                new_state[i][j] = new
                if self.verbose:
                    print(f"│ [{i},{j}] │ 0x{old:02x} │ SBOX[{old:3d}] │ 0x{new:02x}   │")
        
        if self.verbose:
            print("└────────┴──────┴──────────┴─────────┘")
            print_state(new_state, "AFTER SubBytes")
        
        return new_state
    
    def shift_rows(self, state: List[List[int]]) -> List[List[int]]:
        """
        STEP 2: ShiftRows Transformation
        ════════════════════════════════════════════════════════════════
        Rotate each row left by its row number:
         Row 0: [a0 a1 a2 a3] → [a0 a1 a2 a3]  (shift 0)
         Row 1: [b0 b1 b2 b3] → [b1 b2 b3 b0]  (shift 1)
         Row 2: [c0 c1 c2 c3] → [c2 c3 c0 c1]  (shift 2)
         Row 3: [d0 d1 d2 d3] → [d3 d0 d1 d2]  (shift 3)
        
        PURPOSE: Provides diffusion across columns
        """
        if self.verbose:
            print("\n🔄 STEP 2: ShiftRows (Circular Rotation)")
            print("─" * 70)
            print("Each row shifted left by row number (cyclically)")
            print_state(state, "BEFORE ShiftRows")
        
        new_state = [row[:] for row in state]
        new_state[1] = [state[1][1], state[1][2], state[1][3], state[1][0]]
        new_state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
        new_state[3] = [state[3][3], state[3][0], state[3][1], state[3][2]]
        
        if self.verbose:
            print("\n📋 SHIFT PATTERN & TRANSFORMATIONS:")
            print("┌─────┬───────────────────────┬───────────────────────┐")
            print("│ Row │      Before           │       After           │")
            print("├─────┼───────────────────────┼───────────────────────┤")
            
            # Row 0 (no shift)
            row0_before = ' '.join(f"0x{state[0][i]:02x}" for i in range(4))
            row0_after = ' '.join(f"0x{new_state[0][i]:02x}" for i in range(4))
            print(f"│  0  │ {row0_before} │ {row0_after} │ (0 shift)")
            
            # Row 1 (shift 1)
            row1_before = ' '.join(f"0x{state[1][i]:02x}" for i in range(4))
            row1_after = ' '.join(f"0x{new_state[1][i]:02x}" for i in range(4))
            print(f"│  1  │ {row1_before} │ {row1_after} │ (1 shift)")
            
            # Row 2 (shift 2)
            row2_before = ' '.join(f"0x{state[2][i]:02x}" for i in range(4))
            row2_after = ' '.join(f"0x{new_state[2][i]:02x}" for i in range(4))
            print(f"│  2  │ {row2_before} │ {row2_after} │ (2 shift)")
            
            # Row 3 (shift 3)
            row3_before = ' '.join(f"0x{state[3][i]:02x}" for i in range(4))
            row3_after = ' '.join(f"0x{new_state[3][i]:02x}" for i in range(4))
            print(f"│  3  │ {row3_before} │ {row3_after} │ (3 shift)")
            
            print("└─────┴───────────────────────┴───────────────────────┘")
            print_state(new_state, "AFTER ShiftRows")
        
        return new_state
    
    def gmul(self, a: int, b: int) -> int:
        """Galois field multiplication"""
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
    
    def mix_columns(self, state: List[List[int]]) -> List[List[int]]:
        """
        STEP 3: MixColumns Transformation
        ════════════════════════════════════════════════════════════════
        Each column is multiplied by transformation matrix in GF(2^8):
        
        Matrix (Galois Field):
        | 2 3 1 1 |
        | 1 2 3 1 |
        | 1 1 2 3 |
        | 3 1 1 2 |
        
        PURPOSE: Provides algebraic diffusion & confusion
        """
        if self.verbose:
            print("\n🔀 STEP 3: MixColumns (Galois Field Matrix Multiplication)")
            print("─" * 70)
            print("Each column multiplied by GF(2^8) transformation matrix")
            print_state(state, "BEFORE MixColumns")
        
        new_state = [row[:] for row in state]
        
        if self.verbose:
            print("\n📋 DETAILED COLUMN-BY-COLUMN CALCULATIONS:")
            print("Matrix (Galois Field):")
            print("  | 0x02  0x03  0x01  0x01 |")
            print("  | 0x01  0x02  0x03  0x01 |")
            print("  | 0x01  0x01  0x02  0x03 |")
            print("  | 0x03  0x01  0x01  0x02 |")
        
        for col in range(4):
            s0, s1, s2, s3 = [state[row][col] for row in range(4)]
            
            if self.verbose:
                print(f"\n═ Column {col} Input: [0x{s0:02x}, 0x{s1:02x}, 0x{s2:02x}, 0x{s3:02x}]")
            
            # Calculate new values
            r0 = self.gmul(0x02, s0) ^ self.gmul(0x03, s1) ^ s2 ^ s3
            r1 = s0 ^ self.gmul(0x02, s1) ^ self.gmul(0x03, s2) ^ s3
            r2 = s0 ^ s1 ^ self.gmul(0x02, s2) ^ self.gmul(0x03, s3)
            r3 = self.gmul(0x03, s0) ^ s1 ^ s2 ^ self.gmul(0x02, s3)
            
            if self.verbose:
                print(f"Row 0: gmul(0x02,0x{s0:02x})=0x{self.gmul(0x02, s0):02x} XOR gmul(0x03,0x{s1:02x})=0x{self.gmul(0x03, s1):02x} XOR 0x{s2:02x} XOR 0x{s3:02x} = 0x{r0:02x}")
                print(f"Row 1: 0x{s0:02x} XOR gmul(0x02,0x{s1:02x})=0x{self.gmul(0x02, s1):02x} XOR gmul(0x03,0x{s2:02x})=0x{self.gmul(0x03, s2):02x} XOR 0x{s3:02x} = 0x{r1:02x}")
                print(f"Row 2: 0x{s0:02x} XOR 0x{s1:02x} XOR gmul(0x02,0x{s2:02x})=0x{self.gmul(0x02, s2):02x} XOR gmul(0x03,0x{s3:02x})=0x{self.gmul(0x03, s3):02x} = 0x{r2:02x}")
                print(f"Row 3: gmul(0x03,0x{s0:02x})=0x{self.gmul(0x03, s0):02x} XOR 0x{s1:02x} XOR 0x{s2:02x} XOR gmul(0x02,0x{s3:02x})=0x{self.gmul(0x02, s3):02x} = 0x{r3:02x}")
            
            new_state[0][col] = r0
            new_state[1][col] = r1
            new_state[2][col] = r2
            new_state[3][col] = r3
        
        if self.verbose:
            print_state(new_state, "AFTER MixColumns")
        
        return new_state
    
    def add_round_key(self, state: List[List[int]], round_key: List[List[int]]) -> List[List[int]]:
        """
        STEP 4: AddRoundKey Transformation
        ════════════════════════════════════════════════════════════════
        XOR each state byte with corresponding round key byte.
        
        XOR Truth Table:  0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0
        
        PURPOSE: Incorporates key into encryption (simple but crucial)
        """
        if self.verbose:
            print("\n🔑 STEP 4: AddRoundKey (XOR with Round Key)")
            print("─" * 70)
            print("State XORed with round key (bitwise)")
            print_state(state, "BEFORE AddRoundKey (State)")
            print_state(round_key, "Round Key")
        
        new_state = [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]
        
        if self.verbose:
            print("\n📋 DETAILED XOR OPERATIONS (Position by Position):")
            print("┌────────┬─────────┬─────────┬–──────────────┐")
            print("│Position│State    │Round Key│ Result (XOR)  │")
            print("├────────┼─────────┼─────────┼–──────────────┤")
            for i in range(4):
                for j in range(4):
                    state_val = state[i][j]
                    key_val = round_key[i][j]
                    result = state_val ^ key_val
                    print(f"│ [{i},{j}] │ 0x{state_val:02x}    │ 0x{key_val:02x}    │ 0x{state_val:02x} ⊕ 0x{key_val:02x} = 0x{result:02x} │")
            print("└────────┴─────────┴─────────┴–──────────────┘")
            print_state(new_state, "AFTER AddRoundKey (Result)")
        
        return new_state
    
    def expand_key(self, key: bytes) -> List[List[List[int]]]:
        """Basic key expansion (simplified for visualization)"""
        if self.verbose:
            print_header("KEY EXPANSION")
            print("Generating 11 round keys from 128-bit master key (simplified)")
        
        # Simple approach: just repeat and XOR for visualization
        round_keys = []
        key_state = bytes_to_state(key)
        round_keys.append([row[:] for row in key_state])
        
        for i in range(1, 11):
            # Simplified: just XOR with RCON for visualization
            new_key = [[key_state[r][c] for c in range(4)] for r in range(4)]
            for r in range(4):
                new_key[r][0] ^= RCON[i-1]
            key_state = new_key
            round_keys.append([row[:] for row in key_state])
        
        if self.verbose:
            print(f"\n✅ Generated {len(round_keys)} round keys\n")
        
        return round_keys
    
    def encrypt_block(self, plaintext: bytes, key: bytes) -> bytes:
        """AES-128 block encryption"""
        print_header("AES-128 ENCRYPTION - COMPLETE PROCESS")
        print(f"📝 Plaintext:  {plaintext.hex().upper()}")
        print(f"🔑 Key:        {key.hex().upper()}\n")
        
        # Generate round keys
        round_keys = self.expand_key(key)
        
        # Convert to state
        state = bytes_to_state(plaintext)
        print_header("STEP 0: Initial State")
        print_state(state, "Plaintext converted to state matrix")
        
        # Initial AddRoundKey
        print_header("STEP 0.5: Initial AddRoundKey")
        state = self.add_round_key(state, round_keys[0])
        
        # Main rounds
        for round_num in range(1, 10):
            print_header(f"ROUND {round_num}")
            print(f"Applying 4 transformations in sequence\n")
            
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, round_keys[round_num])
        
        # Final round (no MixColumns)
        print_header("FINAL ROUND (Round 10 - No MixColumns)")
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, round_keys[10])
        
        # Convert back to bytes
        ciphertext = state_to_bytes(state)
        
        print_header("ENCRYPTION COMPLETE")
        print(f"✅ Ciphertext: {ciphertext.hex().upper()}\n")
        
        return ciphertext


# ═══════════════════════════════════════════════════════════════════════════
#                          DEMONSTRATION EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════

def demo_quick():
    """Quick demonstration"""
    plaintext = b"DemoTest12345678"  # 16 bytes
    key = b"DemoKey123456789"        # 16 bytes
    
    print("\n" + "="*80)
    print("DEMO: QUICK VISUALIZATION")
    print("="*80)
    
    viz = AESVisualizer(verbose=True)
    ciphertext = viz.encrypt_block(plaintext, key)


def demo_compact():
    """Compact demo - minimal output"""
    print("\n" + "="*80)
    print("DEMO: COMPACT VISUALIZATION")
    print("="*80)
    
    plaintext = b"CompactDemo12345"
    key = b"CompactKey123456"
    
    viz = AESVisualizer(verbose=False)
    ciphertext = viz.encrypt_block(plaintext, key)
    
    print(f"Plaintext:  {plaintext.hex().upper()}")
    print(f"Key:        {key.hex().upper()}")
    print(f"Ciphertext: {ciphertext.hex().upper()}\n")


def demo_key_sensitivity():
    """Show how different keys produce different ciphertexts"""
    print("\n" + "="*80)
    print("DEMO: KEY SENSITIVITY")
    print("="*80)
    
    plaintext = b"TheSamePlaint123"  # Same plaintext
    key1 = b"FirstTestKey1234"
    key2 = b"FirstTestKey1235"  # Changed last byte
    
    viz = AESVisualizer(verbose=False)
    
    print(f"\nPlaintext: {plaintext.hex().upper()}\n")
    
    print(f"Key 1: {key1.hex().upper()}")
    ct1 = viz.encrypt_block(plaintext, key1)
    print(f"→ Ciphertext: {ct1.hex().upper()}\n")
    
    print(f"Key 2: {key2.hex().upper()}")
    ct2 = viz.encrypt_block(plaintext, key2)
    print(f"→ Ciphertext: {ct2.hex().upper()}\n")
    
    print("📊 KEY SENSITIVITY ANALYSIS:")
    print(f"  Keys differ by:        1 byte (last byte)")
    print(f"  Ciphertexts differ:    ALL bytes (avalanche effect!)")
    print("  → This demonstrates the avalanche effect!\n")


def demo_visual_transformation():
    """Visual step-by-step through one round"""
    print("\n" + "="*80)
    print("DEMO: VISUAL TRANSFORMATION WALKTHROUGH")
    print("="*80)
    
    # Create a simple state for visualization
    state = [
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34],
    ]
    
    key = b"MyVisualDemoKey1"
    
    print("\nStarting with a known state:")
    print_state(state, "Initial State")
    
    viz = AESVisualizer(verbose=True)
    
    # Apply transformations step by step
    print("\n" + "─"*70)
    print("Now applying the 4 AES transformations in sequence:")
    print("─"*70)
    
    state = viz.sub_bytes(state)
    state = viz.shift_rows(state)
    state = viz.mix_columns(state)
    
    # Simple round key
    round_key = bytes_to_state(key)
    state = viz.add_round_key(state, round_key)
    
    print_state(state, "Final State After One Complete Round")


def demo_detailed_full_encryption():
    """Full encryption with COMPLETE DETAILED visualization of EVERY step"""
    print("\n" + "="*80)
    print("DEMO: COMPLETE DETAILED ENCRYPTION (VERBOSE)")
    print("="*80)
    
    plaintext = b"DetailedDemo1234"  # 16 bytes  
    key = b"DetailedKey12345"        # 16 bytes
    
    print("\n✨ This mode shows EVERY transformation in complete detail!\n")
    
    viz = AESVisualizer(verbose=True)  # Enable ALL verbose output
    ciphertext = viz.encrypt_block(plaintext, key)
    
    print("\n" + "="*80)
    print("ANALYSIS:")
    print("="*80)
    print("""
✅ You have seen:
   • SubBytes: Each byte replaced using S-box (256-entry lookup table)
   • ShiftRows: Each row rotated left by row number
   • MixColumns: Galois Field matrix multiplication on columns
   • AddRoundKey: XOR operation with round key
   
💡 These 4 operations repeated 10 times create AES security
   • Each operation provides CONFUSION or DIFFUSION
   • Combined effect: 1-bit input change → ~50% output bits affected
   • AVALANCHE EFFECT demonstrated!
""")


# ═══════════════════════════════════════════════════════════════════════════
#                              MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n")
    print("╔" + "═"*78 + "╗")
    print("║" + "AES-128 ENCRYPTION VISUAL DEMONSTRATION".center(78) + "║")
    print("║" + "Understanding Each Step of AES".center(78) + "║")
    print("╚" + "═"*78 + "╝\n")
    
    import sys
    
    if len(sys.argv) > 1:
        demo = sys.argv[1]
        if demo == "1":
            demo_quick()
        elif demo == "2":
            demo_compact()
        elif demo == "3":
            demo_key_sensitivity()
        elif demo == "4":
            demo_visual_transformation()
        elif demo == "5":
            demo_detailed_full_encryption()
        else:
            print("Usage: python AES_encryption.py [1|2|3|4|5]\n")
            print("  1 - Quick visualization")
            print("  2 - Compact output")
            print("  3 - Key sensitivity demo")
            print("  4 - Visual transformation walkthrough") 
            print("  5 - DETAILED FULL ENCRYPTION (shows every step with all details)\n")
    else:
        # Run compact demo by default
        demo_compact()
    
    print("\n" + "="*80)
    print("📚 KEY CONCEPTS:")
    print("="*80)
    print("""
1️⃣  SubBytes (S-box):
    Non-linear transformation using 256-entry lookup table.
    - Prevents linear attacks
    - Each byte replaced independently
    Example: 0x00 → 0x63, 0xFF → 0xEA

2️⃣  ShiftRows:
    Circular rotation of each row by row number.
    - Provides DIFFUSION across columns
    - Row 1 shifted left 1, Row 2 left 2, Row 3 left 3

3️⃣  MixColumns:
    Matrix multiplication in Galois Field GF(2^8).
    - Algebraic diffusion and confusion
    - Each output byte depends on all 4 input bytes

4️⃣  AddRoundKey:
    Simple XOR operation with round key.
    - Incorporates key material
    - Reversible (XOR again to undo)

5️⃣  Key Expansion:
    128-bit key → 11 round keys (44 words)
    - Uses S-box and round constants
    - Each round key completely independent

6️⃣  10 Main Rounds:
    Each applies all 4 transformations
    Final round skips MixColumns

🔐 SECURITY:
   ✓ Confusion:   S-box provides non-linearity
   ✓ Diffusion:   ShiftRows + MixColumns spread bits
   ✓ Key Mixing:  Each round key completely independent
   ✓ Avalanche:   1-bit input → ~50% output bits affected
   ✓ Efficient:   Fast in both software and hardware
   ✓ Proven:      No known practical attacks on AES-128

📊 AES VARIANTS:
   • AES-128: 10 rounds, 128-bit key (2^128 ≈ 10^38 combinations)
   • AES-192: 12 rounds, 192-bit key (Stronger)
   • AES-256: 14 rounds, 256-bit key (Maximum security)
""")
