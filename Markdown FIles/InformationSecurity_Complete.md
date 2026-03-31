# Information Security – Comprehensive Course Notes

## Table of Contents

1. [Introduction to Information Security](#introduction-to-information-security)
2. [Fundamental Concepts](#fundamental-concepts)
3. [Critical Characteristics of Information](#critical-characteristics-of-information)
4. [Subsets of Information Security](#subsets-of-information-security)
5. [CNSS Security Model](#cnss-security-model)
6. [Security Attacks](#security-attacks)
7. [Security Services & Mechanisms](#security-services--mechanisms)
8. [Cryptography Fundamentals](#cryptography-fundamentals)
9. [Symmetric Cipher Model](#symmetric-cipher-model)
10. [Types of Ciphers](#types-of-ciphers)
11. [Cryptanalysis & Attack Methods](#cryptanalysis--attack-methods)
12. [Modular Arithmetic in Cryptography](#modular-arithmetic-in-cryptography)
13. [One-Time Pad (OTP)](#one-time-pad-otp)
14. [AES—Advanced Encryption Standard](#aesadvanced-encryption-standard)
15. [DES & 3DES](#des--3des)
16. [Block Cipher Modes of Operation](#block-cipher-modes-of-operation)
17. [Hash Functions & Digital Signatures](#hash-functions--digital-signatures)
18. [RSA — Asymmetric Encryption](#rsa--asymmetric-encryption)
19. [Common Cryptographic Attacks](#common-cryptographic-attacks)
20. [SSL/TLS Protocol](#ssltls-protocol)
21. [Password Security & Key Derivation](#password-security--key-derivation)
22. [Key Distribution & Management](#key-distribution--management)
23. [Frequency Analysis & Cipher Security](#frequency-analysis--cipher-security)
24. [Quick Reference—Formulas & Key Facts](#quick-referenceformulas--key-facts)

---

## Introduction to Information Security

### What is Information Security?

**Information Security** is the practice of protecting information and information systems from unauthorized access, use, disclosure, disruption, modification, or destruction.

### Key Definitions

| Term | Definition |
|:--|:--|
| **Information** | Data that has been organized, refined, and given context to become meaningful |
| **Security** | The state of being free from danger, risk, or loss of control |

### Scope of Protection

Information security protects:
- **Content:** The actual data and information
- **Systems:** Hardware and software that stores, processes, and transmits data
- **Infrastructure:** Networks, storage, and communication channels

---

## Fundamental Concepts

### Types of Security

Security operates at multiple levels within an organization:

| Type | Scope | Focus |
|:--|:--|:--|
| **Physical Security** | Hardware and facilities | Buildings, servers, access control |
| **Personal Security** | Individual protection | Employee awareness, credential management |
| **Operations Security (OPSEC)** | Procedures and processes | Standard operating procedures, incident response |
| **Communication Security** | Data in transit | Encryption, secure channels |
| **Network Security** | Network infrastructure | Firewalls, intrusion detection, access controls |
| **Information Security** | Holistic data protection | All data forms (storage, transit, processing) |

---

## Critical Characteristics of Information

For information to be considered secure, it must satisfy **seven critical characteristics**:

### The Seven Pillars of Information Security

| Characteristic | Definition | Importance |
|:--|:--|:--|
| **Availability** | Information is accessible to authorized users when needed | Ensures business continuity; prevents denial of service impact |
| **Accuracy** | Information is complete, correct, and free from errors | Enables good decision-making; prevents costly mistakes |
| **Authenticity** | Information is genuine and verifiable as to its origin | Prevents fraud; builds trust in sources |
| **Confidentiality** | Information is accessible only to those authorized to view it | Prevents unauthorized disclosure; protects privacy |
| **Integrity** | Information is complete and unchanged; has not been tampered with | Ensures data reliability; detects unauthorized modifications |
| **Utility** | Information is useful and serves a practical purpose | Ensures efficiency; prevents waste |
| **Possession** | Information is owned or controlled by the rightful entity | Establishes ownership; enables proper governance |

### The CIA Triad (Three Pillars)

While seven characteristics exist, three form the core:

```
        ┌───────────────┐
        │Confidentiality│
        └───────┬───────┘
               / \
              /   \
             /     \
            /       \
    ┌──────────────┐  ┌──────────────┐
    │ Integrity    │  │ Availability │
    └──────────────┘  └──────────────┘
```

---

## Subsets of Information Security

Information Security is a broad umbrella encompassing several specialized domains:

```
        ┌──────────────────────────┐
        │ Information Security     │
        │  (Broadest Scope)        │
        └───────────┬──────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
Cyber Security Computer Security Network Security
    │                               │
    │                               ▼
    │                       Internet Security
    │                    (Internet-specific)
    │
    └─→ Focuses on cyberspace attacks
```

### Detailed Breakdown

| Subset | Scope | Example Concerns |
|:--|:--|:--|
| **Cyber Security** | Protection in cyberspace domain | Malware, ransomware, cyber attacks |
| **Computer Security** | Individual computer systems | System hardening, access control |
| **Network Security** | Network infrastructure | Firewalls, intrusion detection, VPNs |
| **Internet Security** | Internet-facing systems | Web security, cloud security, DDoS protection |

---

## CNSS Security Model

### Three-Dimensional Framework

The **CNSS Model** (Committee on National Security Systems) is a **three-dimensional** security framework visualized as a **3D cube**:

```
        ┌─────────────────────────────┐
       /│        INFORMATION STATES   /│
      / │ (Transmission, Storage,    / │
     /  │  Processing)              /  │
    ┌───┼─────────────────────────────┐│
    │   │   CIA TRIAD               │ │
    │   │   (Threats to counteract) │ │
    │  /│                           │ │
    │ / │    COUNTERMEASURES        │ │
    │/  │  (Technology, Policies,   │ /
    └───│────────────────────────────┘
        │
        └─ People & Awareness
```

### Three Dimensions Explained

#### Dimension 1: CIA Triad (Security Services)

The fundamental security objectives:

| Service | Definition | Goal |
|:--|:--|:--|
| **Confidentiality (C)** | Keep information secret | Only authorized access |
| **Integrity (I)** | Ensure data accuracy and completeness | No unauthorized modifications |
| **Availability (A)** | Ensure accessibility when needed | Prevent denial of service |

#### Dimension 2: Information States (TSP)

The different conditions where information needs protection:

| State | Definition | Example |
|:--|:--|:--|
| **Transmission** | Data moving across networks | Network communications |
| **Storage** | Data at rest in databases/files | Hard drives, cloud storage |
| **Processing** | Data being used/transformed | CPU operations, memory |

#### Dimension 3: Countermeasures (TATP)

The mechanisms used to implement security:

| Countermeasure | Description | Examples |
|:--|:--|:--|
| **Technology (T)** | Tools and systems | Encryption, firewalls, IDS |
| **Policies & Practices (A)** | Rules and procedures | Access control policies, audit procedures |
| **People (P)** | Human element | Training, awareness, authentication |

### Comprehensive Security Matrix

| CIA \ State | Transmission | Storage | Processing |
|:--|:--|:--|:--|
| **Confidentiality** | Encrypted channels | Encrypted storage | Memory protection |
| **Integrity** | Digital signatures | Hash verification | Error detection |
| **Availability** | Redundant networks | Backup systems | Load balancing |

---

## Security Attacks

### Types of Attacks

#### Passive Attacks

**Definition:** Unauthorized reading or theft of information without modification

**Characteristics:**
- Attacker monitors but doesn't alter data
- Hard to detect
- Focus: Confidentiality violation

**Examples:**
- **Spy Programs/Malware:** Silent monitoring software
- **Traffic Analysis:** Intercepting and analyzing network patterns
- **Eavesdropping:** Listening to communications

#### Active Attacks

**Definition:** Unauthorized modification, creation, or destruction of information

**Characteristics:**
- Attacker changes or disrupts data/systems
- Easier to detect than passive attacks
- Focus: Integrity violation

**Categories:**

| Type | Description | Impact |
|:--|:--|:--|
| **Masquerade** | Impersonating authorized user | Unauthorized access |
| **Replay Attack** | Reusing captured valid data | Duplicate transactions |
| **Data Modification** | Altering messages in transit | Integrity compromise |
| **Denial of Service (DoS)** | Blocking legitimate access | Availability compromise |

### Real-World Examples

- **Phishing Attack:** Creating identical replicas of legitimate websites to steal credentials
- **Man-in-the-Middle (MITM):** Intercepting and modifying communications between two parties
- **Hijacking:** Taking control of ongoing connections

---

## Security Services & Mechanisms

### Security Services

Services that enhance the security of data processing systems and information transfers:

| Service | Definition | Addresses |
|:--|:--|:--|
| **Authentication** | Verifying the identity of users/systems | Who you are |
| **Authorization & Access Control** | Granting/denying specific permissions | What you can access |
| **Availability** | Ensuring information access when needed | Uptime and performance |
| **Confidentiality** | Protecting information from disclosure | Who can see data |
| **Integrity** | Ensuring data hasn't been altered | Data trustworthiness |

### Security Mechanisms

Specific techniques and technologies implementing security services:

**Specific Mechanisms** (tailored to particular services):
- Cryptographic algorithms
- Data signatures
- Authentication protocols

**Pervasive Mechanisms** (apply across all services):
- Traffic padding (add dummy data to hide patterns)
- Access control (restrict system access)
- Audit logging (record all activities)

---

## Cryptography Fundamentals

### Principles

**Cryptography** is the science of secret writing—transforming plaintext into ciphertext to ensure confidentiality.

### Types of Cryptography

| Type | Keys Used | Applications | Complexity |
|:--|:--|:--|:--|
| **Symmetric** | One shared key | Speed critical, bulk encryption | Simpler |
| **Asymmetric** | Public/private key pair | Key distribution, digital signatures | Complex |

---

## Symmetric Cipher Model

### Overview

Symmetric cryptography uses a **single shared secret key** for both encryption and decryption.

### Components

```
┌──────────────┐
│  Plaintext   │ (Original message)
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│  Encryption Algorithm    │◄─────┐
│      (e.g., AES)         │      │
└──────┬───────────────────┘      │
       │                      Secret Key
       ▼                      (Shared)
┌──────────────┐                  │
│  Ciphertext  │                  │
└──────┬───────┘                  │
       │                          │
       ▼                          │
    (Transmitted)                 │
       │                          │
       ▼                          │
┌──────────────────────────┐      │
│  Decryption Algorithm    │◄─────┘
│      (e.g., AES)         │
└──────┬───────────────────┘
       │
       ▼
┌──────────────┐
│  Plaintext   │ (Recovered message)
└──────────────┘
```

### Ingredients

| Component | Description |
|:--|:--|
| **Plaintext** | Original readable message; input to encryption |
| **Secret Key** | Shared cryptographic key; determines encryption behavior |
| **Encryption Algorithm** | Computational process transforming plaintext to ciphertext |
| **Ciphertext** | Encrypted, unreadable message; transmitted over insecure channels |
| **Decryption Algorithm** | Reverses encryption using the same key |
| **Recipient** | Authorized party possessing the secret key |

---

## Types of Ciphers

### Transposition Ciphers

**Mechanism:** Rearrange characters while keeping them unchanged

**Operation:** Change position of elements; preserve identity

**Example Pattern:**
```
Original: HELLO
Rearranged: LLEHO
```

**Strength:** Simple; vulnerable to frequency analysis

### Substitution Ciphers

**Mechanism:** Replace each character with another character/value

#### ROT13 (Rotation 13)

**Definition:** Replace each letter with the letter 13 positions away

**Mapping:**
```
A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z
```

**Example:**
- Original: `this is my secret message`
- ROT13: `guvf vf zl frperg zrffntr`

**Note:** Applying ROT13 twice returns original text

#### XOR Cipher

**Mechanism:** Perform XOR operation on ASCII values of plaintext and key

**Process:**
1. Convert text to ASCII values
2. Convert key to ASCII values
3. Perform bitwise XOR for each character
4. Result is ciphertext

**Example:**

```
Plaintext: SECURITY
ASCII:     83 69 67 85 82 73 84 89
           01010011 01000101 01000011 01010101 01010010 01001001 01010100 01011001

Key: KEYKEYKE (repeated)
ASCII:     75 69 89 75 69 89 75 69
           01001011 01000101 01011001 01001011 01000101 01011001 01001011 01000101

XOR Result:
           00011000 00000000 00011010 00011110 00010111 00010000 00011111 00011100
Decimal:   24   00   26    30    23    16    31    28
           $         ▲ ▼ (hex values)
```

**Characteristics:**
- Simple yet effective for basic encryption
- Symmetric: Same operation for encryption and decryption
- Vulnerable to known-plaintext attacks

### Numerical Cipher

**Operation:** Convert text to numbers using ASCII or other encoding schemes

---

## Cryptanalysis & Attack Methods

### Cryptanalysis

**Definition:** The study of attack methods against ciphers

**Approach:**
- Analyzes cipher nature and characteristics
- Exploits algorithm weaknesses
- Uses frequency analysis and patterns

**Information Used:**
- General knowledge of plaintext characteristics
- Patterns (language structure, typing style, etc.)
- Statistical properties

### Brute Force Attack

**Definition:** Exhaustively try every possible key against ciphertext

**Process:**
1. Generate all possible keys
2. Decrypt ciphertext with each key
3. Check if result is readable plaintext
4. Found! When decryption produces valid text

**Effectiveness:** Directly proportional to hash/key space size

| Key Size | Total Possibilities | Time to Brute Force* |
|:--|:--|:--|
| 56-bit | $2^{56}$ ≈ 7 × 10¹⁶ | ~3 months |
| 128-bit | $2^{128}$ ≈ 3 × 10³⁸ | Years with current tech |
| 256-bit | $2^{256}$ ≈ 1 × 10⁷⁷ | Mathematically infeasible |

*Assumes 1 billion computations per second

### Defense Strategies

| Strategy | Description |
|:--|:--|
| **Key Size** | Increase key length to exponentially increase work |
| **Algorithm Strength** | Use mathematically secure algorithms (AES, RSA) |
| **Key Management** | Properly secure and rotate keys |
| **Rate Limiting** | Limit failed authentication attempts |

---

## Practical Examples

### ROT13 Example

```
Original: "This is my secret message."
ROT13:    "Guvf vf zl frperg zrffntr."
Reapply:  "This is my secret message." (returns to original)
```

### XOR Cipher Example

Given ciphertext "estd td xj dpncpe xpddlrp" encrypted with ROT13:

1. Identify the key (or use brute force)
2. Apply XOR with each byte
3. If plaintext appears, the correct key was used

---

## Summary & Key Takeaways

### Essential Principles

1. **Defense in Depth:** Use multiple security layers (technology, policies, people)
2. **CIA Triad:** Balance confidentiality, integrity, and availability
3. **Threat Awareness:** Understand both passive and active attack vectors
4. **Cryptographic Strength:** Key size and algorithm matter
5. **Human Element:** Policy and people are as important as technology

### Recommended Study Path

1. Understand CIA fundamentals
2. Learn about threats (passive vs active)
3. Study cipher types and their weaknesses
4. Explore cryptographic best practices
5. Apply knowledge to real-world scenarios

### Modern Considerations

- Symmetric encryption is fast but requires secure key distribution
- Use established algorithms (AES) instead of custom ciphers
- Consider asymmetric encryption for key exchange
- Implement comprehensive security policies
- Regular training and awareness programs are critical

---

## Modular Arithmetic in Cryptography

### What is Modular Arithmetic?

Called "clock arithmetic"—numbers wrap around after reaching a certain value (the modulus). It is the backbone of most encryption algorithms.

$$a \bmod n = \text{remainder when } a \text{ is divided by } n$$

### Caesar Cipher (Substitution)

The Roman emperor Julius Caesar substituted each letter with the letter 3 positions further in the alphabet.

**Encryption:** $C = (P + K) \bmod 26$

**Decryption:** $P = (C - K) \bmod 26$

Where:
- $P$ = Plaintext value (A=0, B=1,...Z=25)
- $K$ = Key/shift value
- $C$ = Ciphertext value

**Example: Encrypt "HOTEL" with K=7**

| Letter | Value (P) | P + 7 | (P+7) mod 26 | Ciphertext Letter |
|:--|:--|:--|:--|:--|
| H | 7 | 14 | 14 | O |
| O | 14 | 21 | 21 | V |
| T | 19 | 26 | 0 (wraps to 0) | A |
| E | 4 | 11 | 11 | L |
| L | 11 | 18 | 18 | S |

**Note:** HOTEL → OVALS with K=7. When the result = 26, it wraps back to 0 (like a clock).

**Original Caesar (K=3)**
- Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- Ciphertext: DEFGHIJKLMNOPQRSTUVWXYZABC
- Example: ET TU BRUTUS → HW WX EUXWXV

### Affine Cipher (Substitution)

A mono-alphabetic substitution cipher. Uses TWO keys (a and b) and a multiplication step — more secure than Caesar.

**Encryption:** $C = (a \times P + b) \bmod 26$

**Decryption:** $P = a^{-1} \times (C - b) \bmod 26$

**Important Note:** 'a' and 26 must be COPRIME — they share no common factors other than 1. Valid values of a: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.

**Example: Encrypt "HI" with a=5, b=8**

| Letter | P value | Calculation | Result | Ciphertext |
|:--|:--|:--|:--|:--|
| H | 7 | (5×7 + 8) mod 26 = 43 mod 26 | 17 | R |
| I | 8 | (5×8 + 8) mod 26 = 48 mod 26 | 22 | W |

Result: "HI" → "RW"

**How to Calculate mod 26:**
1. Divide the number by 26
2. Drop the whole number part (before decimal)
3. Multiply the decimal part × 26 → this is your remainder
4. Example: 210 mod 26 → 210 ÷ 26 = 8.076... → 0.076 × 26 = 2 ∴ result = 2

**Affine Decryption — Finding Modular Inverse**

For Affine cipher with a=5, b=8, find $5^{-1} \bmod 26$:

- Need a number such that: $5 \times a^{-1} \equiv 1 \pmod{26}$
- Testing: $5 \times 21 = 105$; $105 \bmod 26 = 1$ ✓
- So: $5^{-1} = 21 \pmod{26}$
- Decryption formula becomes: $D(y) = 21(y - 8) \bmod 26$

### Modular Exponentiation

Computing large powers modulo a number efficiently. Used in RSA, Diffie-Hellman.

**Method:** Square-and-reduce. Keep numbers small by reducing mod n at each step.

**Example: Compute $18^{13} \bmod 39$**

1. $18^2 \bmod 39 = 324 \bmod 39 = 12$
2. $18^4 \bmod 39 = 12^2 \bmod 39 = 144 \bmod 39 = 27$
3. $18^8 \bmod 39 = 27^2 \bmod 39 = 729 \bmod 39 = 27$
4. Break exponent: $13 = 8 + 4 + 1$ → $18^{13} = 18^8 \times 18^4 \times 18^1 \bmod 39$
5. $= 27 \times 27 \times 18 \bmod 39 = 729 \bmod 39 \times 18 = 27 \times 18 = 486 \bmod 39 = 18$

$$18^{13} \bmod 39 = 18$$

**Example: Compute $5^{12} \bmod 13$**

1. $5^2 \bmod 13 = 25 \bmod 13 = 12$
2. $5^4 \bmod 13 = 12^2 \bmod 13 = 144 \bmod 13 = 1$
3. $5^{12} = (5^4)^3 = 1^3 = 1$

$$5^{12} \bmod 13 = 1$$

---

## One-Time Pad (OTP)

### Definition

OTP combines plaintext with a completely random key (the pad) using XOR. It is the ONLY theoretically unbreakable encryption — but only under strict conditions.

### Four Required Conditions

OTP is secure **only if ALL four** are met:

1. **Random Key** — The pad must be completely random.
2. **Same Length** — Key must be exactly the same length as the message.
3. **Used Once** — The key must NEVER be reused. Reusing even once destroys security.
4. **Shared Secret** — Both sender and receiver must have the exact same key.

**Note:** If the key is wrong even by ONE bit, the decrypted output becomes completely incorrect.

### OTP Encryption Example: Plaintext = "HELLO", Key = "XMCKL"

**Step 1: Convert to Binary (ASCII)**

| Letter | ASCII | Binary |
|:--|:--|:--|
| H | 72 | 01001000 |
| E | 69 | 01000101 |
| L | 76 | 01001100 |
| L | 76 | 01001100 |
| O | 79 | 01001111 |

| Key Letter | ASCII | Binary |
|:--|:--|:--|
| X | 88 | 01011000 |
| M | 77 | 01001101 |
| C | 67 | 01000011 |
| K | 75 | 01001011 |
| L | 76 | 01001100 |

**Step 2: Apply XOR**

| Plain | Binary | Key | Binary | XOR Result | Decimal |
|:--|:--|:--|:--|:--|:--|
| H | 01001000 | X | 01011000 | 00010000 | 16 |
| E | 01000101 | M | 01001101 | 00001000 | 8 |
| L | 01001100 | C | 01000011 | 00001111 | 15 |
| L | 01001100 | K | 01001011 | 00000111 | 7 |
| O | 01001111 | L | 01001100 | 00000011 | 3 |

**Step 3: Ciphertext**

The resulting decimal values (16, 8, 15, 7, 3) map to non-printable ASCII control characters. This is normal — OTP output is raw binary data.

### OTP Decryption

$$\text{Plaintext} \oplus \text{Key} = \text{Ciphertext}$$

$$\text{Ciphertext} \oplus \text{Key} = \text{Plaintext}$$

(XOR with same key reverses the operation)

Apply XOR again with SAME key XMCKL to recover HELLO:

| Cipher Binary | Key (Binary) | XOR Result | Letter |
|:--|:--|:--|:--|
| 00010000 | X: 01011000 | 01001000 | H |
| 00001000 | M: 01001101 | 01000101 | E |
| 00001111 | C: 01000011 | 01001100 | L |
| 00000111 | K: 01001011 | 01001100 | L |
| 00000011 | L: 01001100 | 01001111 | O |

### Why OTP is Secure / Why OTP is Impractical

| Secure Because | Impractical Because |
|:--|:--|
| Each letter encrypted with truly random key | Key must be as long as the message |
| No pattern to analyze | Key must be shared securely beforehand |
| Cannot be broken even with unlimited computing power | Key must NEVER be reused |

---

## AES—Advanced Encryption Standard

### Introduction

- **AES** = Advanced Encryption Standard. Made in 2001 by NIST (USA), replacing the old DES algorithm.
- **Type:** Symmetric block cipher (same key for encryption and decryption).
- **Algorithm:** Rijndael algorithm.
- **Block size:** 128 bits (16 bytes = 4×4 state matrix).
- **Key sizes:** 128, 192, or 256 bits.

| Key Length | AES Name | Number of Rounds |
|:--|:--|:--|
| 128 bits | AES-128 | 10 |
| 192 bits | AES-192 | 12 |
| 256 bits | AES-256 | 14 |

### Why AES is Strong

- AES-128 requires trying $2^{128}$ combinations — practically impossible to brute-force.
- Resistant to known attacks: Brute-Force, Statistical, Differential, and Linear Attacks.
- Works very fast on both software and hardware.
- Used in: banks, Wi-Fi security (WPA2), VPNs, WhatsApp, and almost every secure app.

### AES Structure — Input/State Array

AES operates on a 4×4 matrix of bytes called the State Array.

- 1 word = 4 bytes = 32 bits
- Block size = 128 bits = 16 bytes = 4 words = 4×4 matrix

### Four AES Transformation Functions (applied each round)

| Step | Transformation | Description |
|:--|:--|:--|
| 1 | Substitute Bytes (SubBytes) | Replace each byte using a 16×16 S-box table. Byte {95} → look at row 9, col 5 → value {2A}. |
| 2 | Shift Rows (ShiftRows) | Circular byte shift of each row. Row 1 unchanged. Row 2: 1-byte shift left. Row 3: 2-byte shift left. Row 4: 3-byte shift left. |
| 3 | Mix Columns (MixColumns) | Each column processed separately. Each byte replaced by a value dependent on all 4 bytes in its column. (Matrix multiplication in GF(2⁸)) |
| 4 | Add Round Key (AddRoundKey) | XOR the state with 128-bit round key. Simplest step — designed to be as simple as possible. |

### AES Round Structure

**Before rounds begin:** Initial AddRoundKey (XOR plaintext with Key 0).

**Then each round applies:** SubBytes → ShiftRows → MixColumns → AddRoundKey.

**Final round:** SubBytes → ShiftRows → AddRoundKey (no MixColumns in last round).

### AES-128 Detailed Example

**Plaintext (Hex):** 32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34

**Key 0 (Hex):** 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c

**Step 0: Initial AddRoundKey (XOR each byte)**

| Byte # | Plaintext | Key 0 | Result (XOR) |
|:--|:--|:--|:--|
| 1 | 32 | 2b | 19 |
| 2 | 43 | 7e | 3d |
| 3 | f6 | 15 | e3 |
| 4 | a8 | 16 | be |
| 5 | 88 | 28 | a0 |
| 6 | 5a | ae | f4 |
| 7 | 30 | d2 | e2 |
| 8 | 8d | a6 | 2b |

**Key Schedule (Round Key Generation)**

For AES-128, the key expansion generates 11 round keys (Round Key 0 through Round Key 10).

The G function is applied on the last word (W3) of previous key:
1. Left-shift W3 by 1 byte
2. Apply S-box substitution
3. XOR with round constant (Rcon)

Then: $W_4 = W_0 \oplus G(W_3)$, $W_5 = W_1 \oplus W_4$, $W_6 = W_2 \oplus W_5$, $W_7 = W_3 \oplus W_6$

---

## Key Distribution & Management

### Overview

Encryption is only as strong as the keys that power it. Key management involves: Generation → Distribution → Storage → Rotation → Revocation.

### Placement of Encryption

| Type | Description | Used In |
|:--|:--|:--|
| **Link-to-Link Encryption** | Encrypts data between two specific points. Data is decrypted and re-encrypted at each intermediate node. Like a relay race of couriers. | HTTPS, WPA2/WPA3, VPNs |
| **End-to-End Encryption (E2EE)** | Encrypts from sender to receiver — no intermediate node can read it. Like a locked box only sender & receiver can open. | WhatsApp, Signal, iMessage, ProtonMail |

**Note:** Link encryption weakness: If the intermediate server/node is compromised, data can be exposed after decryption at that node.

### Key Distribution for Link Encryption (Symmetric)

Uses symmetric keys. The key distribution problem: how to securely share the same key?

- **Diffie-Hellman Key Exchange** — Used when browsers connect via HTTPS. Agrees on a temporary symmetric key WITHOUT transmitting the key over the network.
- **Session Keys** — Temporary keys discarded after the session ends. Past sessions remain safe even if later compromised.

### Key Distribution for E2EE (Asymmetric + Symmetric)

- **Public Key** = like a mailbox slot — anyone can insert (encrypt). Only owner has private key to open (decrypt).
- **Asymmetric + Symmetric Hybrid:** Use public key to encrypt a temporary symmetric key → then use that symmetric key to communicate.
- **PGP/GPG** = Pretty Good Privacy / GNU Privacy Guard. Uses public-key cryptography to exchange symmetric keys for email encryption.

### Key Management Steps

1. **Key Generation** — Use secure algorithms (AES for symmetric, RSA for asymmetric).
2. **Key Distribution** — Share keys securely (e.g., banks distribute ATM keys via dedicated secure channels).
3. **Key Storage** — Use Hardware Security Modules (HSM) or encrypted databases.
4. **Key Rotation** — Periodically replace old keys (e.g., every 24 hours). Like regularly changing your door lock.
5. **Key Revocation** — Remove/invalidate compromised or expired keys.

### Diffie-Hellman Key Exchange

Introduced by Whitfield Diffie and Martin Hellman in 1976. Allows two parties to establish a shared secret key over an insecure channel without meeting in person.

**Step-by-Step Example**

| Step | Action | Values (example) |
|:--|:--|:--|
| 1 | Agree on public parameters (shared openly — even if attacker knows these, it's safe) | n = 5, g = 7 (n and g are large prime numbers) |
| 2 | Each party picks a private number (NEVER shared) | Mr. A: x = 3, Mr. B: y = 13 |
| 3 | Each computes a public value using: $A = g^x \bmod n$ and $B = g^y \bmod n$ | $A = 7^3 \bmod 5 = 343 \bmod 5 = 3$ \| $B = 7^{13} \bmod 5 = 2$ |
| 4 | Exchange A and B publicly (attacker can see these but cannot reverse them) | Mr. A gets B=2, Mr. B gets A=3 |
| 5 | Each computes the shared key: $K = B^x \bmod n$ or $K = A^y \bmod n$ | Mr. A: $K = 2^3 \bmod 5 = 8 \bmod 5 = 3$ \| Mr. B: $K = 3^{13} \bmod 5 = 3$ |

Both get $K = 3$ → This is the shared secret key used for symmetric encryption!

**Note:** Even if an attacker knows n, g, A, and B, they cannot calculate x or y (Discrete Logarithm Problem). This is what makes Diffie-Hellman secure.

---

## DES & 3DES

### Data Encryption Standard (DES)

**DES (Data Encryption Standard)** was the primary symmetric encryption algorithm from 1977 to 2001, replaced by AES.

#### DES Specifications

| Property | Details |
|:--|:--|
| **Block Size** | 64 bits (8 bytes) |
| **Key Size** | 56 bits (effective); 64 bits with parity bits |
| **Rounds** | 16 rounds |
| **Algorithm** | Feistel network structure |
| **S-boxes** | 8 substitution boxes (non-linear transformation) |
| **P-boxes** | Permutation boxes (linear transformation) |

#### DES Structure

1. **Initial Permutation (IP)** — Rearrange input bits
2. **16 Rounds of Feistel Function**
   - Split into left (L) and right (R) halves
   - Round function: $R_{i+1} = L_i \oplus F(R_i, K_i)$
   - $L_{i+1} = R_i$
3. **Final Permutation (FP)** — Inverse of initial permutation

#### Why DES is Obsolete

- **56-bit key is too small:** $2^{56} \approx 7.2 \times 10^{16}$ (breakable in hours with modern computers)
- **64-bit blocks are small:** Prone to birthday attacks with large volumes of data
- **Triple DES is slow:** Takes 3× time to encrypt single block
- **AES is superior:** Larger key sizes (128/192/256), faster, more secure

### Triple DES (3DES)

**3DES** applied DES encryption three times to extend key lifetime while DES was being phased out.

#### 3DES Variants

| Variant | Description | Key Size | Effective Key Size |
|:--|:--|:--|:--|
| **3DES-EDE** | Encrypt-Decrypt-Encrypt | 168 bits (3 × 56) | 112 bits |
| **3DES-EEE** | Encrypt-Encrypt-Encrypt | 168 bits | 112 bits |

#### 3DES Encryption Process

```
Plaintext → [DES Encrypt with K1] → [DES Decrypt with K2] → [DES Encrypt with K3] → Ciphertext
```

#### Why E-D-E (Not E-E-E)?

- **EDE allows compatibility:** If K1 = K2 = K3, then 3DES reduces to single DES
- **Better than EEE** for backward compatibility with DES systems

#### Current Status

- ⚠️ **Deprecated:** NIST deprecated 3DES in 2017
- ❌ **Disallowed:** TLS 1.3 prohibits 3DES
- ✅ **Use:** Only for legacy system support
- ✅ **New Systems:** Use AES-128 or stronger

---

## Block Cipher Modes of Operation

Block ciphers like AES encrypt fixed-size blocks. **Modes of operation** are techniques to encrypt data longer than block size while adding security properties.

### 1. ECB (Electronic Codebook) — ❌ NOT SECURE

**Definition:** Each plaintext block encrypted independently with same key.

```
C[i] = E(K, P[i])
```

**Disadvantages:**
- ❌ **Identical plaintext blocks produce identical ciphertext blocks** → Pattern leakage
- ❌ Vulnerable to statistical analysis
- ❌ Example: ECB mode encrypts identical images into identical ciphertext patterns

**Status:** Never use for production. Only for single-block encryption.

### 2. CBC (Cipher Block Chaining) — ✅ COMMONLY USED

**Definition:** Each plaintext block XORed with previous ciphertext block before encryption.

#### Encryption:
```
C[0] = E(K, P[0] ⊕ IV)
C[i] = E(K, P[i] ⊕ C[i-1]) for i > 0
```

#### Decryption:
```
P[0] = D(K, C[0]) ⊕ IV
P[i] = D(K, C[i]) ⊕ C[i-1] for i > 0
```

**Components:**
- **IV (Initialization Vector):** Random value, must be unpredictable and unique per message
- **Chaining:** Previous ciphertext depends on all previous plaintext

**Advantages:**
- ✅ **Identical plaintext blocks → different ciphertext blocks** (due to chaining)
- ✅ Semantic security achieved
- ✅ Widely supported

**Disadvantages:**
- ❌ **Sequential:** Cannot parallelize encryption
- ❌ **Decryption parallelizable** but encryption must be sequential
- ❌ **Error propagation:** 1-bit error in ciphertext affects all subsequent blocks
- ❌ **Padding required** for non-aligned messages

**Padding Scheme (PKCS#7):**
```
If message block needs N padding bytes, append N bytes each with value N.

Example (16-byte block, 10 bytes data):
Data:        6F 6B 6B 6B 6B 6B 6B 6B 6B 6B
Padding:     06 06 06 06 06 06
Padded:      6F 6B 6B 6B 6B 6B 6B 6B 6B 6B 06 06 06 06 06 06
```

### 3. CTR (Counter Mode) — ✅ MODERN, PARALLELIZABLE

**Definition:** Block cipher operates as stream cipher using counter.

#### Encryption:
```
Keystream[i] = E(K, Counter + i)
C[i] = P[i] ⊕ Keystream[i]
```

**Components:**
- **Nonce:** Initial counter value, often = timestamp + random
- **Counter:** Increments for each block

**Advantages:**
- ✅ **Fully parallelizable:** All blocks can encrypt simultaneously
- ✅ **Random access:** Can decrypt any block independently
- ✅ **No padding required:** Encrypts to exact message length
- ✅ **Turns block cipher into stream cipher**

**Disadvantages:**
- ❌ **Nonce reuse is catastrophic:** Same nonce + key = identical keystream → XOR attack vulnerability
- ⚠️ Must never repeat (Nonce, Key) pair

### 4. GCM (Galois/Counter Mode) — ✅ AUTHENTICATED ENCRYPTION

**Definition:** CTR mode + authentication tag for data integrity.

#### Structure:
```
1. Encrypt plaintext using CTR mode
2. Generate authentication tag using GHASH function
3. Send: (IV, Ciphertext, AuthenticationTag)
```

**Advantages:**
- ✅ **Authenticated encryption:** Ensures both confidentiality AND integrity
- ✅ **Parallelizable:** Can process multiple blocks simultaneously
- ✅ **NIST approved:** Used in TLS 1.3, IPSec
- ✅ **Associated Data (AD):** Can authenticate metadata without encrypting it

**How Verification Works:**
```
Receiver computes: ReceivedTag = GHASH(K, IV, Ciphertext, AD)
Compare with transmitted tag (timing-safe comparison)
If match → Accept. If mismatch → Reject (possible tampering).
```

### 5. Other Modes (Briefly)

| Mode | Use | Pros | Cons |
|:--|:--|:--|:--|
| **OFB** (Output Feedback) | Stream cipher mode | Synchronous | Error propagation |
| **CFB** (Cipher Feedback) | Stream cipher mode | Works with any block size | Slower than CTR |
| **EAX** | Authenticated encryption | Flexible | More complex |

### Mode Selection Criteria

**Choose based on:**

1. **Do you need authentication?**
   - YES → GCM, EAX, OCB
   - NO → CBC, CTR

2. **Parallelization needed?**
   - YES → GCM, CTR, ECB (but ECB is insecure!)
   - NO → CBC, OFB, CFB

3. **Streaming requirement?**
   - YES → CTR, CFB, OFB
   - NO → CBC, GCM

4. **Random access decryption?**
   - YES → CTR, ECB
   - NO → CBC, OFB

---

## Hash Functions & Digital Signatures

### Hash Function Properties

A **cryptographic hash function** maps arbitrary-length input to fixed-length output with specific security properties.

#### Hash Function Characteristics

| Property | Definition | Security Impact |
|:--|:--|:--|
| **Deterministic** | Same input always produces same hash | Reproducible |
| **Quick Computation** | Efficiently computable in polynomial time | Practical |
| **Fixed Output Size** | Always produces n-bit hash regardless of input size | Standardized |
| **Avalanche Effect** | Tiny input change drastically changes hash | Diffusion |
| **One-Way (Preimage Resistance)** | Infeasible to find input from hash | Information hiding |
| **Weak Collision Resistance** | Infeasible to find different input with same hash | Signature security |
| **Strong Collision Resistance** | Infeasible to find ANY two inputs with same hash | Overall integrity |

#### Collision Resistance Levels

```
Preimage Resistance (1st preimage):    Find x given H(x)          → ~2^n difficulty
Weak Collision (2nd preimage):        Find y ≠ x such that H(x)=H(y) → ~2^n difficulty 
Strong Collision:                     Find any x,y where H(x)=H(y) → ~2^(n/2) difficulty (Birthday Attack)
```

### Common Hash Algorithms

| Algorithm | Output Size | Block Size | Status | Usage |
|:--|:--|:--|:--|:--|
| **MD5** | 128 bits | 512 bits | ❌ Broken | Legacy only (NOT secure) |
| **SHA-1** | 160 bits | 512 bits | ⚠️ Deprecated | Legacy systems |
| **SHA-256** (SHA-2) | 256 bits | 512 bits | ✅ Secure | Most common |
| **SHA-512** (SHA-2) | 512 bits | 1024 bits | ✅ Secure | High-security apps |
| **SHA-3** | Variable | Variable | ✅ Secure | Modern standard |
| **BLAKE2** | Variable | Variable | ✅ Fast | Performance-critical |

### Hash Function Applications

1. **Data Integrity:** Verify files, messages unchanged
2. **Password Storage:** Hash passwords instead of storing plaintext
3. **Digital Signatures:** Sign hash instead of entire message
4. **Blockchain:** Chain blocks using hash values
5. **Message Authentication:** HMAC combines hash with secret key

### Digital Signatures

**Digital Signature** proves:
- ✅ **Authentication:** Signer identity confirmed (only private key holder could create)
- ✅ **Integrity:** Message not modified (any change breaks signature)
- ✅ **Non-repudiation:** Signer cannot deny creating signature

#### RSA Digital Signature Process

**Signing (Private Key Operation):**
```
1. Hash message:        H = SHA-256(Message)
2. Sign hash:           Signature = H^d mod n
   (Only private key holder knows d)
```

**Verification (Public Key Operation):**
```
1. Received signature:   Signature
2. Unsign:             H' = Signature^e mod n
3. Hash message:        H = SHA-256(Message)
4. Verify:             Accept if H == H'
```

#### Why Sign the Hash?

- **Efficiency:** Hash is smaller than message
- **Speed:** Sign 256 bits instead of multi-MB file
- **Universality:** Any hash function + any cipher combination

#### Message Authentication Codes (MAC)

**MAC** provides authentication using a **shared secret key** (symmetric).

**HMAC (Hash-based MAC):**
```
HMAC = H((K ⊕ opad) || H((K ⊕ ipad) || Message))

Where:
- K = shared secret key
- opad = outer padding constant
- ipad = inner padding constant
- H = hash function (SHA-256, etc.)
```

**HMAC Verification:**
```
1. Sender: HMAC = HMAC-SHA256(SharedKey, Message)
2. Sender sends: (Message, HMAC)
3. Receiver computes: HMAC' = HMAC-SHA256(SharedKey, Message)
4. Verify: Accept if HMAC == HMAC'
```

**HMAC vs. Digital Signature:**

| Aspect | HMAC | Digital Signature |
|:--|:--|:--|
| **Key** | Symmetric (shared secret) | Asymmetric (public/private) |
| **Non-repudiation** | ❌ No (both have same key) | ✅ Yes (only private key) |
| **Speed** | ✅ Faster | ❌ Slower |
| **Use Case** | Internal authentication, APIs | Legal contracts, software signing |

---

## RSA — Asymmetric Encryption

### RSA Overview

**RSA (Rivest–Shamir–Adleman)** is the most widely used asymmetric encryption algorithm. Security depends on difficulty of factoring large numbers.

#### RSA Parameters

| Parameter | Role |
|:--|:--|
| **p, q** | Large prime numbers (1024-2048 bits each) |
| **n = p × q** | RSA modulus (2048-4096 bits) |
| **φ(n) = (p-1)(q-1)** | Euler's totient function |
| **e** | Public exponent (typically 65537) |
| **d** | Private exponent: $e \times d \equiv 1 \pmod{φ(n)}$ |
| **Public Key** | (e, n) - shared with everyone |
| **Private Key** | (d, n) - kept secret |

### Key Generation

**Step 1:** Choose two large random prime numbers p and q
```
p = 61, q = 53 (small example; real: 1024+ bits)
```

**Step 2:** Calculate n and φ(n)
```
n = p × q = 61 × 53 = 3233
φ(n) = (p-1)(q-1) = 60 × 52 = 3120
```

**Step 3:** Choose e (public exponent)
```
Requirements:
- 1 < e < φ(n)
- gcd(e, φ(n)) = 1 (e and φ(n) coprime)

Typically e = 65537 = 0x10001
(common choice: small, fast to compute, prime)
```

**Step 4:** Calculate d (private exponent)
```
Find d such that: e × d ≡ 1 (mod φ(n))

Example: 17 × d ≡ 1 (mod 3120)
Using Extended Euclidean Algorithm: d = 2753
```

**Step 5:** Publish public key, keep private key secret
```
Public Key:  (e=17, n=3233)
Private Key: (d=2753, n=3233)
```

### RSA Encryption & Decryption

**Encryption (anyone with public key):**
```
Ciphertext = Plaintext^e mod n
C = P^17 mod 3233
```

**Decryption (only private key holder):**
```
Plaintext = Ciphertext^d mod n
P = C^2753 mod 3233
```

#### Worked Example: Encrypt "65"

```
1. Plaintext: P = 65
2. Public Key: (e=17, n=3233)
3. Encrypt: C = 65^17 mod 3233
   = 232630513987207 mod 3233
   = 2790

4. Ciphertext: C = 2790

5. Decrypt with Private Key (d=2753, n=3233):
   P = 2790^2753 mod 3233
   = 65 ✓ (successfully recovered!)
```

### Why RSA Works Mathematically

**Euler's Theorem:** If gcd(P, n) = 1, then:
```
P^φ(n) ≡ 1 (mod n)
```

**RSA Decryption Proof:**
```
C^d ≡ (P^e)^d (mod n)
    ≡ P^(e×d) (mod n)
    ≡ P^(1 + k×φ(n)) (mod n)    [since e×d ≡ 1 (mod φ(n))]
    ≡ P × (P^φ(n))^k (mod n)
    ≡ P × 1^k (mod n)             [by Euler's Theorem]
    ≡ P (mod n)
```

### RSA Practical Considerations

#### Key Sizes

| Key Size | Status | Year Deprecated |
|:--|:--|:--|
| 512 bits | ❌ Broken | 1999 |
| 768 bits | ❌ Broken | 2009 |
| 1024 bits | ⚠️ Weak | Before 2010 (not recommended) |
| 2048 bits | ✅ Secure | Current minimum |
| 4096 bits | ✅ Very Secure | Long-term security |

#### RSA vs. Symmetric Encryption

| Aspect | RSA | AES |
|:--|:--|:--|
| **Speed** | ❌ 1000× slower | ✅ Very fast |
| **Key Size** | 2048 bits for 112-bit security | 128 bits for 128-bit security |
| **Use** | Key distribution, signatures | Bulk encryption |
| **Hybrid** | Use RSA to encrypt AES key | Combines both advantages |

#### Practical RSA in HTTPS

```
1. Browser connects to HTTPS server
2. Server sends RSA public key (in certificate)
3. Browser generates random 256-bit AES key (Session Key)
4. Browser encrypts Session Key with server's RSA public key
5. Server decrypts with private RSA key to get Session Key
6. Both now use AES with Session Key for fast encryption
→ Secure key exchange without meeting in advance!
```

---

## Common Cryptographic Attacks

### 1. Birthday Attack — $O(2^{n/2})$

**Principle:** Birthday paradox applied to cryptographic hashes.

**Setup:**
```
Hash output: n bits → 2^n possible values
If we hash 2^(n/2) random messages:
Probability of collision ≈ 50%
```

**Example: SHA-256**
```
Output: 256 bits
Need to hash ~2^128 ≈ 3.4×10^38 messages for collision
With 1 billion hashes/second: 10^30 seconds (older than universe!)
→ SHA-256 resistant to birthday attack
```

**Why MD5 is broken:**
```
MD5 output: 128 bits
Collision found with ~2^64 hashes ≈ realistic in 2000s
❌ Never use MD5 for cryptographic purposes
```

**Mitigation:**
- Use hash with ≥256-bit output (SHA-256, SHA-3)
- For collision resistance: need at least 256-bit hash

### 2. Meet-in-the-Middle Attack

**Target:** Used against block ciphers, symmetric encryption with repeated keys.

**Attack Concept:**
```
Instead of trying all keys sequentially:
1. Try encrypting with first half of keys (2^(n/2) operations)
2. Try decrypting known ciphertext with second half of keys (2^(n/2) operations)
3. Look for matches in the middle
→ Total: ~2 × 2^(n/2) = 2^(n/2 + 1) operations (much better than 2^n)
```

**Example: DES with 2 keys (intended 112-bit security):**
```
Naive: Try all 2^112 combinations → 2^112 DES operations
Meet-in-Middle:
  1. Encrypt with first 56 bits → store 2^56 values
  2. Decrypt with second 56 bits → look for match
  → Total: 2^57 operations (2^55 times faster!)
```

**Why 3DES avoided this:**
- Uses 3 keys (when all different) → no meet-in-middle advantage
- Maintains ~112-bit effective security

### 3. Rainbow Tables — Precomputed Hash Inversion

**Attack:** Precompute hashes of common passwords, then lookup.

**Setup:**
```
1. Compute hashes of all 1-8 character passwords
2. Store in table (reduction function identifies chains)
3. When you find a password hash, trace through chains to find password
```

**Examples of Vulnerable Passwords (Rainbow Table Hits):**
- "password" → SHA256 = 5e884898da280
- "123456" → SHA256 = 8d969eef6ecad
- All common dictionary words

**Mitigation: Salt**
```
Without salt:     Hash(password) → same every time → Rainbow table works
With salt:        Hash(password || random_salt) → different for each user

Example (bcrypt with salt):
Password: "mypassword"
Salt: "$2b$12$abcdefghijklmnopqrst" (16 bytes, random)
Hash: bcrypt("mypassword" || salt) → unique result
```

**Salt Properties:**
- ✅ Random (≥16 bytes)
- ✅ Unique per password (different for each user)
- ✅ Stored with hash (makes rainbow tables impractical)

### 4. Brute-Force Attack

**Direct approach:** Try every possible key/password.

**Time Complexity:** $2^{\text{key size} / 2}$ average (50% after half of keyspace)

**Examples:**
```
DES (56-bit): 2^55 attempts average → 1 second (modern)
AES-128: 2^127 attempts → 10^36 years (impossible)
Password (8 chars, 26 letters): 26^8 ≈ 2×10^11 → 6 hours
```

**Mitigation:**
- Large key size (≥128 bits)
- Rate limiting (max attempts per time period)
- Account lockout (after N failed attempts)
- Slow hashing (bcrypt, Argon2 intentionally slow)

### 5. Dictionary Attack — Targeted Brute-Force

**Attack:** Try common passwords/words instead of all combinations.

**Common Passwords (top 1000):**
```
"password", "123456", "qwerty", "abc123", ...
→ 90% of user passwords from top 1000 words
```

**Mitigation:**
- Strong password policy (length ≥12, mixed case, symbols)
- Slow hashing (Argon2 makes 1000 attempts take minutes)
- Multi-factor authentication (SMS, app-based codes)

### 6. Timing Attacks — Side Channel

**Attack:** Measure encryption/comparison time to leak information.

**Example - String Comparison:**
```
Vulnerable Code:
if password_hash == user_input_hash:
    Process for each character, stop on mismatch
    → Takes longer if correct chars match longer
    → Attacker measures time, deduces correct chars

Correct (Timing-Safe) Code:
verify_hmac(expected_hash, user_input_hash)
    Compare all bytes (constant time)
    → Always same time regardless of match position
```

**Mitigation:**
- Constant-time comparison functions
- Add random delays
- Use dedicated cryptographic libraries

### 7. Padding Oracle Attack

**Target:** CBC mode encryption with predictable padding validation.

**Attack:**
```
1. Attacker sends modified ciphertext
2. Server decrypts and checks PKCS#7 padding
3. Return errors like "invalid padding" vs "invalid MAC"
4. Attacker uses error messages to deduce plaintext byte by byte
```

**Mitigation:**
- Use authenticated encryption (GCM mode)
- Don't reveal padding validation errors
- Use TLS 1.2+ with authenticated encryption

---

## SSL/TLS Protocol

### SSL/TLS Overview

**TLS (Transport Layer Security)** is the cryptographic protocol securing internet communications (HTTPS, email, VPNs).

#### TLS Versions

| Version | Year | Status |
|:--|:--|:--|
| SSL 2.0 | 1995 | ❌ Broken |
| SSL 3.0 | 1996 | ❌ Deprecated |
| TLS 1.0 | 1999 | ⚠️ Deprecated |
| TLS 1.1 | 2006 | ⚠️ Deprecated |
| TLS 1.2 | 2008 | ✅ Secure (current standard) |
| TLS 1.3 | 2018 | ✅ Latest, recommended |

### TLS 1.2 Handshake (4-Way)

#### Step 1: ClientHello
```
Client → Server:
- Supported TLS versions
- Supported cipher suites (RSA+AES-GCM, ECDHE+ChaCha20, etc.)
- Random nonce
- Requested hostname (SNI)
```

#### Step 2: ServerHello + Certificate
```
Server → Client:
- Selected TLS version (typically 1.2)
- Selected cipher suite
- Server's random nonce
- Server's X.509 certificate (public key + identity)
- Digital signature proving certificate ownership
```

#### Step 3: Key Exchange
```
Client → Server (encrypted with server's public key):
- Pre-master secret (random bytes)

Both derive session keys:
Session Key = PRF(Pre-master Secret || Client Nonce || Server Nonce)
```

#### Step 4: Finished
```
Client → Server: MAC("client finished" || handshake messages)
Server → Client: MAC("server finished" || handshake messages)

Verify to ensure no tampering during handshake
```

#### Data Transfer Phase
```
All subsequent traffic encrypted with Session Key
Typically: AES-128-GCM (confidentiality + integrity)
```

### TLS 1.3 Improvements

**TLS 1.3 is faster and more secure:**

| Aspect | TLS 1.2 | TLS 1.3 |
|:--|:--|:--|
| **Handshake Rounds** | 4 RTT | 1 RTT (0-RTT resumption) |
| **Setup Time** | ~100ms | ~25ms |
| **Ciphers** | 100+ deprecation-laden | 5 modern recommended |
| **Forward Secrecy** | Optional | Mandatory (ECDHE by default) |
| **Resumption** | Session IDs/tickets | Pre-shared keys |
| **DES/MD5/RC4** | Allowed (but bad) | ❌ Removed |

### Perfect Forward Secrecy (PFS)

**Concept:** Compromise of long-term keys doesn't decrypt past sessions.

**Without PFS (RSA key exchange):**
```
1. Attacker passively records HTTPS traffic
2. Years later, attacker steals server's RSA private key
3. Attacker can decrypt all past communications
→ Entire past exposure!
```

**With PFS (ECDHE key exchange):**
```
1. Each session uses ephemeral (session-specific) ECDHE key pair
2. Session key discarded after session ends
3. Years later, attacker steals server's RSA private key
4. Attacker CANNOT decrypt past sessions (ephemeral keys lost)
→ Only current session at risk
```

**Implementation:** ECDHE-RSA cipher suites
```
- ECDHE (Elliptic Curve Diffie-Hellman) generates session-specific shared secret
- RSA signs ECDHE public values for authentication
- Result: Forward secrecy + authentication
```

### Cipher Suite Components

**Example: `ECDHE-RSA-AES128-GCM-SHA256`**

| Component | Role |
|:--|:--|
| **ECDHE** | Session key agreement (forward secrecy) |
| **RSA** | Authenticate server certificate |
| **AES128** | Symmetric encryption (128-bit key) |
| **GCM** | Authenticated encryption mode |
| **SHA256** | Hash function for PRF |

### Certificate Validation Chain

```
1. Browser receives server certificate
2. Browser checks:
   - Is certificate signed by trusted CA?
   - Is hostname in certificate SAN/CN?
   - Is certificate not expired?
   - Is certificate not revoked? (CRL check)
3. If all pass → Display 🔒 (HTTPS)
4. If any fail → Display ⚠️ (Warning) or 🚫 (Block)
```

---

## Password Security & Key Derivation

### Why Passwords Need Special Handling

**Problems with passwords:**
- Users choose weak passwords (dictionary words)
- Passwords are static (can be reused across services)
- Passwords vulnerable to rainbow tables if hashed simply

**Solution:** Slow, salted hash functions make cracking impractical.

### Password Hashing Functions

#### 1. PBKDF2 (Password-Based Key Derivation Function 2)

**Algorithm:**
```
Hash_output = PBKDF2(Password, Salt, Iterations, Hash_Function)

Repeats hashing operation N times (iterations)
Example: PBKDF2("mypass", salt, 100,000, SHA256)
```

**Specifications:**
- **Iterations:** Minimum 100,000 (slow down attackers)
- **Salt:** ≥16 bytes random
- **Output:** Typically 256 bits

**Practical Use:**
```python
Password: "SecurePass123"
Salt: random_16_bytes
Hash = PBKDF2(Password, Salt, 100000, SHA256)
→ Takes ~100ms per guess (1 million guesses = 100,000 seconds ≈ 1 day)
```

#### 2. bcrypt — Adaptive Hashing

**Algorithm:**
```
Hash = bcrypt(Password, Salt with Cost Factor)

Cost factor (work factor):
- 2^Cost iterations
- Can increase over time as computers get faster
```

**Features:**
- ✅ **Adaptive:** Can increase cost factor without rehashing
- ✅ **Slow by design:** Intentionally slow (100ms+)
- ✅ **Salt included:** Automatically generates and stores salt

**Output Format:**
```
$2b$12$R9h/cIPz0gi.URNNGEWV2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUW
  │  │  │  │
  │  │  │  └─ Hash (54 characters)
  │  │  └────── Salt + cost factor
  │  └───────── Cost factor (12 = 2^12 iterations)
  └──────────── Algorithm identifier (bcrypt)
```

**Time per guess:** 100ms-1000ms (depends on cost factor)

#### 3. Argon2 — Modern Memory-Hard Function

**Algorithm:**
```
Hash = Argon2(Password, Salt, Time_Cost, Memory_Cost, Parallelism, Output_Size)
```

**Features:**
- ✅ **Memory-hard:** Uses significant RAM (not just CPU)
- ✅ **GPU-resistant:** Parallel memory access prevents GPU acceleration
- ✅ **ASIC-resistant:** Can't be optimized for custom hardware
- ✅ **Recommended:** OWASP recommends for new systems

**Parameters:**
```
Time Cost (t):       3-4 (number of passes)
Memory Cost (m):     64MB-1GB (RAM usage)
Parallelism (p):     1-4 (threads)

Argon2("password", salt, 3, 65540, 4, 32)
→ 3 passes, 64MB RAM, 4 threads, 32-byte output
→ ~50-100ms on modern CPU
```

### Comparison: Password Hashing Functions

| Function | Speed | Memory-Hard | Adaptive | Recommended |
|:--|:--|:--|:--|:--|
| **SHA-256** | ⚡ Very fast | ❌ No | ❌ No | ❌ Never |
| **PBKDF2** | 🐢 Slow | ❌ No | ⚠️ Partially | ⚠️ Legacy systems |
| **bcrypt** | 🐢 Slow | ❌ No | ✅ Yes | ✅ Current standard |
| **Argon2** | 🐢 Slow | ✅ Yes | ✅ Yes | ✅ Best practice |

### Key Derivation Functions (KDF)

Different from password hashing — used to derive multiple keys from single secret.

#### HKDF (HMAC-based KDF)

**Two phases:**

**Phase 1 - Extract (normalize entropy):**
```
PRK = HMAC-Hash(Salt, InputKeyMaterial)
```

**Phase 2 - Expand (stretch to needed length):**
```
OKM = "" 
for i = 1 to N:
    T = T || HMAC-Hash(PRK, T || Info || i)
OKM = first L bytes of T
```

**Use Case (TLS 1.3):**
```
Deriving multiple keys from single pre-shared secret:
- Client write key
- Server write key  
- Client IV
- Server IV
- MAC key

All from single source using HKDF
```

#### PBKDF2 for Key Derivation

```
Same as password hashing, but:
- Input: Key material (from key exchange like DH)
- Output: Multiple session keys
- Purpose: Convert shared secret into usable keys
```

### Salt Best Practices

**Requirements:**
```
1. Random:     Use cryptographically secure RNG
2. Unique:     Different salt per password
3. Size:       ≥16 bytes (128 bits)
4. Stored:     Include with hash (no secret)
```

**Example (bcrypt):**
```
Password: "mypassword"
Generated/Stored: $2b$12$UR9.kPS3rIIVTtNmGY0h..salt..|hash
                        └─── Salt (pre-computed, included)
```

### Practical Implementation Checklist

```
✅ New password storage:
   [ ] Use Argon2 with 65MB memory, 3 iterations
   [ ] Generate 16+ byte random salt
   [ ] Store: (salt, hash, algorithm, parameters)

✅ Legacy password upgrade:
   [ ] Accept bcrypt or PBKDF2 (100k+ iterations)
   [ ] Re-hash with Argon2 on next login
   [ ] Never store plaintext passwords

✅ Key derivation (TLS, encryption):
   [ ] Use HKDF for key extraction/expansion
   [ ] Use PBKDF2 only if HKDF unavailable
   [ ] Never store derived keys (regenerate from master)

✅ Never:
   ❌ Use MD5, SHA-1 for passwords
   ❌ Use unsalted hash
   ❌ Use same salt for multiple passwords
   ❌ Store master secret (only derived keys)
```

---

## Frequency Analysis & Cipher Security

### Frequency Analysis

The statistical distribution of letter frequencies in any message tends toward the known frequency distribution of that language. This is true especially for long messages.

- Simple substitution ciphers preserve letter frequencies → can be broken by frequency analysis.
- In English: E, T, A, O, I, N are the most frequent letters.
- Discovered by Arab scientist Abu Yusuf Yaqub ibn Ishaq al-Kindi (~850 CE).
- Simple substitution cipher has $26! \approx 4 \times 10^{26}$ possible keys — exhaustive search is not practical, but frequency analysis can crack it.

### Summary: Cipher Security Comparison

| Cipher | Security Level | Key Space | Attack Vulnerability |
|:--|:--|:--|:--|
| Caesar | Very Weak | Only 26 keys | Brute force (trivial) |
| Simple Substitution | Weak | $26! \approx 4 \times 10^{26}$ | Frequency analysis |
| ROT-13 | Very Weak | 1 key (fixed) | Trivial |
| Affine | Weak-Medium | Limited by coprime 'a' | Frequency analysis |
| OTP | Unbreakable | Key = message length | Theoretically unbreakable if used correctly |
| AES-128 | Very Strong | $2^{128}$ | No practical attack known |

---

## Quick Reference—Formulas & Key Facts

### Cipher Formulas

| Topic | Formula / Key Fact |
|:--|:--|
| Caesar Encrypt | $C = (P + K) \bmod 26$ |
| Caesar Decrypt | $P = (C - K) \bmod 26$ |
| Affine Encrypt | $C = (a \times P + b) \bmod 26$ |
| Affine Decrypt | $P = a^{-1} \times (C - b) \bmod 26$ (a and 26 must be coprime) |
| OTP Encrypt | $\text{Ciphertext} = \text{Plaintext} \oplus \text{Key}$ |
| OTP Decrypt | $\text{Plaintext} = \text{Ciphertext} \oplus \text{Key}$ (XOR property: $A \oplus B \oplus B = A$) |

### AES & Cryptography

| Topic | Fact |
|:--|:--|
| AES Block Size | 128 bits = 16 bytes = 4×4 matrix |
| AES Keys | 128 / 192 / 256 bits → 10 / 12 / 14 rounds |
| AES Transformations | SubBytes → ShiftRows → MixColumns → AddRoundKey (each round) |
| Diffie-Hellman Public Values | $A = g^x \bmod n$ (Mr. A) \| $B = g^y \bmod n$ (Mr. B) |
| Diffie-Hellman Shared Key | $K = B^x \bmod n = A^y \bmod n$ |
| Modular Exponentiation | Square-and-reduce method: compute powers of 2, then combine |

### Security Concepts

| Topic | Definition |
|:--|:--|
| CIA Triad | Confidentiality, Integrity, Availability |
| CNSS Dimensions | Goals (CIA) × States (Transmission/Storage/Processing) × Measures (People/Tech/Policy) |
| Brute Force | Try every possible key; complexity = $2^{\text{key size}}$ |
| Unconditionally Secure | Ciphertext doesn't contain enough info to determine plaintext — no matter how much time the attacker has. (OTP is the only known scheme.) |
| Computationally Secure | The cost/time to break exceeds the value of the information, or the time to break exceeds the useful lifetime of the info. |

---

## Information Security — Study Summary

**Congratulations!** You now have comprehensive knowledge of information security, cryptography, and ciphers. Remember these key principles:

1. **Defense in Depth:** Use multiple security layers (technology, policies, people)
2. **CIA Triad:** Balance confidentiality, integrity, and availability
3. **Threat Awareness:** Understand both passive and active attack vectors
4. **Cryptographic Strength:** Key size and algorithm matter critically
5. **Human Element:** Policy and people are as important as technology
6. **Key Management:** Secure key distribution and rotation are essential
7. **Algorithm Choice:** Use established algorithms (AES) instead of custom ciphers
