# Information Security - Final Term Study Notes

## Final Term Topics

- Hashing and salting
- Access control
- Buffer overflow
- Risk management
- Link-to-link encryption
- Key management
- Types of firewall

## Hashing and Salting

Hashing converts data, especially passwords, into a fixed-length hash value. A hash is one-way, which means the original input cannot be recovered from the output.

### Why hashing is useful

- It hides the original password.
- It is useful for password storage.
- It supports integrity checking.

### Salting

Salting means adding a random value before hashing.

### Why salting matters

- It makes each password hash unique.
- It protects against rainbow table attacks.
- It makes dictionary attacks harder.

### Common hash algorithms

- MD5
- SHA-256
- SHA-512
- bcrypt

If two users have the same password, salting ensures that their stored hashes are different.

## Access Control

Access control decides who is allowed to do what in a system.

### Main parts

- Identification: Who are you?
- Authentication: Can you prove it?
- Authorization: What are you allowed to do?

### Example

A student may log in to a portal, but only an admin can change user roles.

### Common access control models

- DAC: Discretionary Access Control
- MAC: Mandatory Access Control
- RBAC: Role-Based Access Control
- ABAC: Attribute-Based Access Control

### Short explanation

- DAC gives the owner control over resources.
- RBAC assigns permissions by role.
- MAC is strict and based on security labels.

## Buffer Overflow

A buffer overflow happens when a program writes more data into a buffer than it can hold.

### Why it is dangerous

- It can crash the program.
- It can corrupt memory.
- It may allow an attacker to run malicious code.

### Simple example

If a 10-character buffer receives 50 characters, extra data may overwrite nearby memory.

### Prevention ideas

- Input validation
- Safe library functions
- Bounds checking
- Memory-safe programming practices

## Risk Management

Risk management means identifying, analyzing, and reducing security risks.

### Steps in risk management

- Identify assets
- Identify threats
- Identify vulnerabilities
- Estimate impact
- Estimate likelihood
- Choose controls

### Categories of business risks

- Strategic risk
- Operational risk
- Financial risk
- Compliance risk
- Reputational risk

### Simple numerical example

If the chance of a loss is 20% and the expected loss is 50,000, then expected risk can be estimated as:

- Risk = 0.20 x 50,000 = 10,000

This helps the organization understand whether the control cost is worth it.

## Link-to-Link Encryption

Link-to-link encryption protects communication on each network link or hop.

### Main idea

- Data is encrypted from one node to the next.
- It is decrypted and encrypted again at each intermediate point.

### Advantage

- Each link gets protection.

### Limitation

- Intermediate devices can see the data after decryption on each hop.

### Compare with end-to-end encryption

- Link-to-link encryption protects each segment.
- End-to-end encryption protects data only from sender to receiver.

## Key Management

Key management is the process of handling encryption keys safely.

### Main tasks

- Key generation
- Key distribution
- Key storage
- Key rotation
- Key revocation
- Key destruction

### Why it matters

If key management is weak, even strong encryption can fail.

### Key exchange idea

- Diffie-Hellman is used to create a shared secret over an insecure network.
- It helps two parties agree on a secret without sending the secret directly.

## Types of Firewall

A firewall controls incoming and outgoing traffic based on security rules.

### Main purpose

- Protect a trusted network from untrusted traffic.

### Common types

- Packet filtering firewall
- Application-level gateway
- Proxy firewall
- Stateful inspection firewall

### Packet filtering firewall

- Checks source IP, destination IP, port, and protocol.
- Makes decisions quickly.

### Application-level gateway

- Works at the application layer.
- Can inspect application data more deeply.

### Firewall limitations

- It cannot stop attacks that bypass it.
- It may not fully protect against insider threats.

## Exam Revision Summary

- Hashing hides passwords; salting makes hashes unique.
- Access control decides who can do what.
- Buffer overflow is a memory safety problem.
- Risk management reduces business losses.
- Link-to-link encryption protects each communication hop.
- Key management keeps encryption keys safe.
- Firewalls filter traffic and protect the network boundary.
