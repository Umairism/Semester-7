# Information Security – Course Notes

## Table of Contents

- [What is Information Security?](#what-is-information-security)
- [Critical Characteristics of Information](#critical-characteristics-of-information)
- [Subsets of Information Security](#subsets-of-information-security)
- [CNSS Security Model](#cnss-security-model)
- [Security Attacks](#security-attacks)
- [Security Services & Mechanisms](#security-services--mechanisms)
- [Symmetric Cipher Model](#symmetric-cipher-model)
- [Cryptanalysis & Brute Force Attacks](#cryptanalysis--brute-force-attacks)
- [Types of Ciphers](#types-of-ciphers)

---

## What is Information Security?

### Information

**Information** is data that has been organized into a meaningful and useful form.

### Types of Security

Security is a broad domain encompassing multiple layers:

| Type | Scope |
|:--|:--|
| **Physical Security** | Protection of hardware, buildings, and physical assets |
| **Personal Security** | Protection of individuals and personnel |
| **Operations Security** | Protection of operational procedures and processes |
| **Communication Security** | Protection of communication channels |
| **Network Security** | Protection of network infrastructure |
| **Information Security** | Protection of information across all forms |

### Definition

> **Information Security** is the protection of information — including the systems and hardware that use, store, and transmit it.

---

## Critical Characteristics of Information

For information to be considered secure, it must satisfy these seven properties:

| Characteristic | Description |
|:--|:--|
| **Availability** | Information is accessible when needed by authorized users |
| **Accuracy** | Information is free from errors and is reliable |
| **Authenticity** | Information is genuine and verifiable as to its origin |
| **Confidentiality** | Information is accessible only to those authorized to view it |
| **Integrity** | Information is complete and has not been tampered with |
| **Utility** | Information is useful and serves a purpose |
| **Possession** | Information is owned or controlled by the rightful entity |

---

## Subsets of Information Security

Information Security is a broad umbrella that includes several specialized domains:

```
            ┌─────────────────────────┐
            │  Information Security   │
            └───────────┬─────────────┘
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
  Cyber Security  Computer Security  Network Security
                                         │
                                         ▼
                                  Internet Security
```

| Subset | Focus |
|:--|:--|
| **Cyber Security** | Protection in the cyberspace domain |
| **Computer Security** | Protection of individual computer systems |
| **Network Security** | Protection of network infrastructure and data in transit |
| **Internet Security** | Protection specific to internet-facing systems and communications |

---

## CNSS Security Model

The **CNSS Model** (Committee on National Security Systems) provides a **three-dimensional** framework for understanding information security:

### The Three Dimensions

| Dimension | Components |
|:--|:--|
| **CIA Triad** | **C**onfidentiality, **I**ntegrity, **A**vailability |
| **Information States (TSP)** | **T**ransmission, **S**torage, **P**rocessing |
| **Countermeasures (TATP)** | **T**echnology, Policies **A**nd Practices, **P**eople |

> The CNSS model is visualized as a **cube** — every combination of the three dimensions represents a specific security concern that must be addressed.

### CIA Triad Explained

| Property | Meaning |
|:--|:--|
| **Confidentiality** | Only authorized parties can access the information |
| **Integrity** | Information has not been altered by unauthorized parties |
| **Availability** | Information is accessible to authorized users when needed |

---

## Security Attacks

Security attacks are classified into two main categories:

### Passive Attacks

Passive attacks involve **monitoring and eavesdropping** without modifying data. The attacker observes but does not interfere.

| Type | Description |
|:--|:--|
| **Spyware / Malware** | Software that secretly monitors user activity |
| **Traffic Analysis** | Observing patterns in communication (who talks to whom, when, how often) |

> Passive attacks are **difficult to detect** because they don't alter the data.

### Active Attacks

Active attacks involve **modification or disruption** of data and communication. The attacker interferes directly.

| Type | Description |
|:--|:--|
| **Replay Attack** | Capturing and retransmitting valid data to trick the receiver |
| **Data Modification** | Altering the contents of a message in transit |
| **Masquerade** | Impersonating an authorized entity to gain access |
| **Denial of Service (DoS)** | Overwhelming a system to make it unavailable to legitimate users |

---

## Security Services & Mechanisms

### Security Services

Services provide the **"what"** — the security goals to achieve:

| Service | Description |
|:--|:--|
| **Authentication** | Verifying the identity of a user or system |
| **Access Control** | Restricting access to resources based on permissions |

### Security Mechanisms

Mechanisms provide the **"how"** — the tools and techniques to achieve security:

| Mechanism | Description |
|:--|:--|
| **Cryptography** | Encrypting data to protect confidentiality |
| **Data Integrity** | Techniques to detect unauthorized data modification (e.g., checksums, hashes) |
| **Digital Signature** | Verifying the authenticity and integrity of a message using asymmetric cryptography |
| **Authentication** | Protocols and methods to verify identity (passwords, tokens, biometrics) |
| **Traffic Padding** | Adding dummy data to communication to prevent traffic analysis |

---

## Symmetric Cipher Model

In **symmetric encryption**, the same secret key is used for both encryption and decryption.

### How It Works

```
Plaintext → [ Encryption Algorithm + Secret Key ] → Ciphertext → [ Decryption Algorithm + Secret Key ] → Plaintext
```

| Component | Description |
|:--|:--|
| **Plaintext** | The original readable message |
| **Secret Key** | A shared key used by both sender and receiver (e.g., used with the AES algorithm) |
| **Ciphertext** | The encrypted, unreadable output |
| **Decryption Algorithm** | Reverses the encryption using the same secret key |

> **Example:** The AES (Advanced Encryption Standard) algorithm is a widely used symmetric cipher.

---

## Cryptanalysis & Brute Force Attacks

### Cryptanalysis

**Cryptanalysis** is the study of breaking encryption by exploiting weaknesses in the algorithm itself. The attacker relies on knowledge of the algorithm's structure.

### Brute Force Attack

A **brute force attack** tries **every possible key** on the ciphertext until the correct one is found.

| Method | Approach | Feasibility |
|:--|:--|:--|
| **Cryptanalysis** | Exploit algorithm weaknesses | Depends on algorithm strength |
| **Brute Force** | Try all possible keys | Depends on key length ($2^n$ possibilities for an $n$-bit key) |

> Longer keys make brute force exponentially harder. A 128-bit key has $2^{128}$ possible combinations — practically unbreakable by brute force with current technology.

---

## Types of Ciphers

### Substitution Ciphers

In substitution ciphers, each element of the plaintext is **replaced** by another element.

| Cipher | How It Works |
|:--|:--|
| **ROT13** | Each letter is shifted 13 positions in the alphabet. Applying ROT13 twice returns the original text. |
| **XOR Cipher** | Each byte of plaintext is XOR'd with a key byte. Applying XOR with the same key decrypts the message. |

> ROT13 and XOR are **symmetric** — the same operation encrypts and decrypts.

### Transposition Ciphers

In transposition ciphers, the **positions** of plaintext elements are rearranged according to a specific pattern, but the elements themselves remain unchanged.

| Cipher Type | Approach |
|:--|:--|
| **Substitution** | Replaces characters with different characters |
| **Transposition** | Rearranges the order of characters |

### Example from the Notes

> **Plaintext:** "This is my secret text"
>
> This can be encrypted using either **XOR Cipher** or **ROT13** substitution as demonstrated in the course's Cipher-Decipher program.

---

*These notes cover Information Security topics from Semester 7 — core concepts, the CNSS model, attack types (passive/active), security services and mechanisms, symmetric encryption, cryptanalysis, and cipher types (substitution & transposition).*
