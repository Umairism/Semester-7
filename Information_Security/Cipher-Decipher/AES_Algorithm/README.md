# AES-128 Encryption: Complete Implementation & Understanding Guide

## 📁 Files in This Directory

```
.
├── AES_encryption.py          ← Main implementation (this file!)
├── AES_VISUAL_GUIDE.md        ← Detailed visual guide with examples
└── README.md                  ← This file
```

---

## 🚀 Quick Start

### Running the Program

```bash
cd /home/umairism/Desktop/Semester\ 7/Information_Security/Cipher-Decipher

# Show this help
python AES_encryption.py help

# Run default demo (compact visualization)
python AES_encryption.py

# Run specific demonstrations
python AES_encryption.py 1  # Quick demo
python AES_encryption.py 2  # Default compact output
python AES_encryption.py 3  # Key sensitivity (avalanche effect)
python AES_encryption.py 4  # Detailed transformation walkthrough
```

### Example Output

```
Plaintext:  CompactDemo12345
Key:        CompactKey123456
Ciphertext: 58AE98D05E3CF500AADCD7A0F631F0EE
```

---

## 🎓 Educational Purpose

This implementation is designed to **teach** AES encryption, not for production use. It includes:

✅ **Visual representations**: 4×4 state matrices printed at each step  
✅ **Detailed explanations**: Comments explaining every transformation  
✅ **Step-by-step debugging**: See how each round modifies the state  
✅ **Multiple demos**: Different examples showing different aspects  
✅ **No external dependencies**: Pure Python (except standard library)

---

## 📊 What You'll Learn

### The 4 Core AES Transformations

#### 1. **SubBytes** - S-Box Substitution
```python
📌 What: Replace each byte using a 256-entry lookup table
📊 Why: Non-linearity (prevents linear attacks)
⚡ How: state[i][j] = SBOX[state[i][j]]

Visual:
Before: 0x43 0x61 0x65 0x32 ...
After:  0xED ...  ...  ...  ...
        (completely changed)
```

#### 2. **ShiftRows** - Circular Rotation
```python
📌 What: Rotate each row left by row number
📊 Why: Diffusion (spreads changes across columns)
⚡ How: 
  Row 0: No shift
  Row 1: Shift left 1 position
  Row 2: Shift left 2 positions
  Row 3: Shift left 3 positions

Visual:
Before: Col0 Col1 Col2 Col3    After: Col0 Col1 Col2 Col3
        ──────────────────            ──────────────────
Row0 │   a0   b0   c0   d0     Row0 │   a0   b1   c2   d3
Row1 │   a1   b1   c1   d1  →  Row1 │   a1   b2   c3   d0
Row2 │   a2   b2   c2   d2     Row2 │   a2   b3   c0   d1
Row3 │   a3   b3   c3   d3     Row3 │   a3   b0   c1   d2
```

#### 3. **MixColumns** - Galois Field Matrix Multiplication
```python
📌 What: Each column multiplied by transformation matrix in GF(2^8)
📊 Why: Algebraic diffusion (output depends on all 4 input bytes)
⚡ How:
  Matrix = | 0x02  0x03  0x01  0x01 |
           | 0x01  0x02  0x03  0x01 |
           | 0x01  0x01  0x02  0x03 |
           | 0x03  0x01  0x01  0x02 |
  
  r0 = (0x02·s0) ⊕ (0x03·s1) ⊕ s2 ⊕ s3
  r1 = s0 ⊕ (0x02·s1) ⊕ (0x03·s2) ⊕ s3
  r2 = s0 ⊕ s1 ⊕ (0x02·s2) ⊕ (0x03·s3)
  r3 = (0x03·s0) ⊕ s1 ⊕ s2 ⊕ (0x02·s3)
  
  Where · = Galois Field multiplication, ⊕ = XOR
```

#### 4. **AddRoundKey** - XOR with Round Key
```python
📌 What: XOR each state byte with corresponding round key byte
📊 Why: Incorporates key material (only key holder can undo)
⚡ How: state[i][j] ^= round_key[i][j]

Visual:
State:     0101010 (binary)
Round Key: 1010101 (binary)
XOR:       1111111 (result)

Key Property: A ⊕ B ⊕ B = A  (XORing twice reverses it)
```

---

## 🔐 Security Properties

### Confusion & Diffusion

**Confusion** - Making key's effect on ciphertext obscure:
```
✓ S-box provides non-linearity
✓ No mathematical relationship between key and output
✓ Each output byte depends on multiple input bytes
```

**Diffusion** - Spreading input changes across entire output:
```
┌─────────────────────────────────────────┐
│          Avalanche Effect               │
├─────────────────────────────────────────┤
│  Input bit 0 changes:                   │
│  After Round 1: ~12.5% output bits      │
│  After Round 2: ~50% output bits        │
│  After Round 3: ~98% output bits        │
│                                         │
│  This is IDEAL for cryptography!        │
└─────────────────────────────────────────┘
```

### Key Expansion

```
128-bit Master Key (16 bytes)
        ↓
Key Schedule (Expansion Algorithm)
        ↓
11 Round Keys (44 words = 176 bytes)
  - Round Key 0:  First 16 bytes of master key
  - Round Key 1:  Derived using S-box + Rcon
  - Round Key 2:  Derived from Round Key 1
  - ...
  - Round Key 10: Final round key

Each completely unpredictable and independent!
```

---

## 🔢 Implementation Details

### State Matrix Structure

```
AES works on 16 bytes as a 4×4 matrix (column-major order):

Bytes:  [00 04 08 12]
        [01 05 09 13]
        [02 06 10 14]
        [03 07 11 15]

Layout: [a0 b0 c0 d0]
        [a1 b1 c1 d1]
        [a2 b2 c2 d2]
        [a3 b3 c3 d3]
```

### Round Structure

```
┌────────────────────────────────────────┐
│     AES-128 Encryption (10 + 1 rounds) │
├────────────────────────────────────────┤
│                                        │
│  Plaintext (16 bytes)                  │
│         ↓                              │
│  Initial AddRoundKey (XOR with Key 0)  │
│         ↓                              │
│  ┌──────────────────────────┐          │
│  │ For Round 1 to 9:        │          │
│  │  1. SubBytes             │          │
│  │  2. ShiftRows            │          │
│  │  3. MixColumns           │          │
│  │  4. AddRoundKey          │          │
│  └──────────────────────────┘          │
│         ↓ (repeat 9 times)             │
│  ┌──────────────────────────┐          │
│  │ Final Round (10):        │          │
│  │  1. SubBytes             │          │
│  │  2. ShiftRows            │          │
│  │  3. ❌ NO MixColumns     │          │
│  │  4. AddRoundKey          │          │
│  └──────────────────────────┘          │
│         ↓                              │
│  Ciphertext (16 bytes)                 │
│                                        │
└────────────────────────────────────────┘
```

---

## 📈 Complexity Analysis

### Time Complexity

```
For AES-128:
  • One round: O(1) - fixed 16 bytes
  • All rounds: O(1) - exactly 10 rounds
  • Total: O(1) - constant time operation!

Practical: ~1-2 GB/sec (software), ~10+ GB/sec (hardware)
```

### Space Complexity

```
State matrix:           16 bytes
Round keys (11):        176 bytes (derived, not stored)
S-box lookup:           256 bytes (read-only constant)
Other variables:        ~50 bytes
──────────────────────────────
Total: Approximately 500 bytes
```

---

## 🧪 Testing the Implementation

### Demo 1: Quick Visualization
```bash
python AES_encryption.py 1
Shows: One complete encryption with visual state at each step
```

### Demo 2: Compact Output
```bash
python AES_encryption.py 2
Shows: Quick encryption summary without transformation details
Result: Plaintext → Ciphertext
```

### Demo 3: Key Sensitivity (Avalanche Effect)
```bash
python AES_encryption.py 3
Shows: Same plaintext encrypted with 2 slightly different keys
Result: Completely different ciphertexts (demonstrates avalanche)
```

### Demo 4: Detailed Transformation
```bash
python AES_encryption.py 4
Shows: Step-by-step transformation with hex values
Result: Full visibility into all 4 operations
```

---

## 🔍 Understanding the Code

### Main Class: `AESVisualizer`

```python
class AESVisualizer:
    def __init__(self, verbose: bool = True):
        # verbose=True shows all transformation details
        # verbose=False shows only final ciphertext
    
    def sub_bytes(self, state):
        # S-box substitution
    
    def shift_rows(self, state):
        # Circular rotation
    
    def mix_columns(self, state):
        # Galois field matrix multiplication
    
    def add_round_key(self, state, round_key):
        # XOR with round key
    
    def encrypt_block(self, plaintext, key):
        # Complete AES-128 encryption
```

### Key Functions

```python
def bytes_to_state(data: bytes) → List[List[int]]:
    """Convert 16 bytes to 4×4 state matrix (column-major)"""

def state_to_bytes(state: List[List[int]]) → bytes:
    """Convert 4×4 state matrix back to 16 bytes"""

def gmul(a: int, b: int) → int:
    """Galois field multiplication in GF(2^8)"""
```

---

## 📚 Related Concepts

### Other Block Ciphers

| Cipher | Key | Block | Rounds | Status |
|--------|-----|-------|--------|--------|
| DES | 56 | 64 | 16 | ❌ Broken |
| 3DES | 168 | 64 | 48 | ⚠️ Deprecated |
| AES-128 | 128 | 128 | 10 | ✅ Secure |
| AES-192 | 192 | 128 | 12 | ✅ Very Secure |
| AES-256 | 256 | 128 | 14 | ✅ Maximum |

### Cipher Modes of Operation

To encrypt more than 16 bytes, use:

```
ECB - Electronic Codebook     (❌ Not secure)
CBC - Cipher Block Chaining   (✅ Common)
CTR - Counter Mode            (✅ Fast, parallelizable)
GCM - Galois Counter Mode     (✅ Authenticated encryption)
```

### Related Concepts

```
• Symmetric Encryption: Same key for encryption & decryption
• Asymmetric Encryption: Different keys (RSA, ECC)
• Block Cipher: Fixed-size input (16 bytes for AES)
• Stream Cipher: Variable-size input (operates on bit/byte streams)
• Cipher Modes: Methods to encrypt large data with block cipher
```

---

## 🚨 Important Notes

### ⚠️ NOT For Production

This implementation is **educational only**:

```
❌ Missing:
  - Constant-time implementation (vulnerable to timing attacks)
  - Side-channel attack resistance (vulnerable to power analysis)
  - Padding mode support (PKCS#7, etc.)
  - Multiple block modes (ECB, CBC, CTR, GCM)
  - Error handling (buffer overflows, etc.)

✅ For production use:
  - PyCryptodome (Python crypto library)
  - OpenSSL (C library, used by Python)
  - libsodium (Modern cryptography library)
```

### 📌 Key Requirements

- **Python 3.6+**
- **No external dependencies** (pure Python)
- **16-byte plaintext** (exactly 16 bytes, no padding)
- **16-byte key** (128-bit key for AES-128)

---

## 📖 Learning Path

1. **Start Here**: Read `AES_VISUAL_GUIDE.md` for concepts
2. **Run Demos**: `python AES_encryption.py 1-4` to see in action
3. **Study Code**: Read `AES_encryption.py` line-by-line
4. **Experiment**: Modify the byte values and observe changes
5. **Deep Dive**: Study key expansion and Galois field math
6. **Apply**: Use PyCryptodome for real-world applications

---

## 🔗 External Resources

### Official Documentation
- [NIST AES Specification (FIPS 197)](https://csrc.nist.gov/publications/detail/fips/197/final)
- [The Design of Rijndael](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

### Online Visualizers
- [AES Visualization Tool](https://www.aljacom.com/showcase/aes/)
- [CryptoJS AES Encryption](https://cryptojs.gitbook.io/docs/)

### Related Tutorials
- [Understanding AES](https://www.youtube.com/watch?v=O4xNJsjtN6E)
- [Cryptography Course (Khan Academy)](https://www.khanacademy.org/computing/computer-science/cryptography)

---

## 📝 Example Usage in Code

```python
from AES_encryption import AESVisualizer, bytes_to_state, state_to_bytes

# Create visualizer
aes = AESVisualizer(verbose=True)

# Encrypt 16-byte message
plaintext = b"MySecret123456!!"  # Must be 16 bytes
key = b"MyKey1234567890X"       # Must be 16 bytes

ciphertext = aes.encrypt_block(plaintext, key)
print(f"Ciphertext: {ciphertext.hex().upper()}")

# Without verbose output
aes_quiet = AESVisualizer(verbose=False)
ct = aes_quiet.encrypt_block(plaintext, key)
```

---

## 🎯 Key Takeaways

### Why AES is Excellent

```
✓ Secure: No practical attacks on AES-128, 192, or 256
✓ Fast: Efficient in both software and hardware
✓ Simple: Easy to understand and implement
✓ Standardized: Widely accepted and verified
✓ Proven: 20+ years of cryptanalysis (still unbroken)
✓ Flexible: Available in 3 key sizes (128/192/256 bits)
```

### How AES Achieves Security

```
1. Confusion (S-box):
   Non-linear transformation makes key effect obscure

2. Diffusion (ShiftRows + MixColumns):
   Single-bit input change affects ~50% of output

3. Key Mixing (Key Expansion + AddRoundKey):
   Each round uses completely different key material

4. Iteration (10 Rounds):
   Compounding security properties render attacks infeasible
```

### Security Strength

```
AES-128:  2^128 possible keys ≈ 3.4 × 10^38 (infeasible to brute-force)
AES-192:  2^192 possible keys ≈ 6.2 × 10^57 (extremely secure)
AES-256:  2^256 possible keys ≈ 1.2 × 10^77 (maximum standard security)

For perspective:
  - Trying 1 trillion keys/second
  - AES-128 would take: 10^19 years (age of universe ≈ 10^10 years)
  - AES-256 would take: 10^60 years (incomprehensibl larger)
```

---

## 💡 Commonly Asked Questions

**Q: Why can't AES-128 be broken?**  
A: 2^128 possible keys is computationally infeasible to search. No algorithm is known that's faster than brute force.

**Q: Should I use AES-128, 192, or 256?**  
A: AES-128 is enough for most purposes. Use AES-256 for long-term security (30+ years).

**Q: Is this code secure for production?**  
A: NO. Use PyCryptodome or OpenSSL for production. This is for learning only.

**Q: How do I encrypt messages longer than 16 bytes?**  
A: Use a cipher mode like CBC, CTR, or GCM that chains multiple AES blocks.

---

## 📞 Support

For questions or clarifications, refer to:
- The code comments in `AES_encryption.py`
- The detailed guide in `AES_VISUAL_GUIDE.md`
- Official NIST documentation for absolute specifications

---

**Happy Learning! 🎓**

This implementation is designed to make AES encryption concepts crystal clear. Use it to deepen your understanding of modern cryptography!

