# LL(1) Parser - Quick Reference Guide

## Grammar Overview

### Original Grammar (Left-Recursive - Not LL(1))
```
E → E + T | T
T → T * F | F
F → (E) | n
```
❌ **Problem**: LL(1) parsers cannot handle left recursion

### Converted Grammar (Right-Recursive - LL(1) Compatible)
```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → (E) | n
```
✓ **Solution**: Left recursion eliminated using grammar transformation

---

## FIRST and FOLLOW Sets

### FIRST Sets (What terminals can start a derivation)
| Non-Terminal | FIRST Set |
|---|---|
| E | {n, (} |
| E' | {+, ε} |
| T | {n, (} |
| T' | {*, ε} |
| F | {n, (} |

### FOLLOW Sets (What terminals can follow a non-terminal)
| Non-Terminal | FOLLOW Set |
|---|---|
| E | {$, )} |
| E' | {$, )} |
| T | {+, ), $} |
| T' | {+, ), $} |
| F | {+, *, ), $} |

---

## Parsing Table (Simplified View)

```
        n  +  *  (  )  $
    E   0  -  -  0  -  -
    E'  -  1  -  -  2  2
    T   3  -  -  3  -  -
    T'  -  5  4  -  5  5
    F   7  -  -  6  -  -
```

**Production Numbers:**
```
0: E → T E'
1: E' → + T E'
2: E' → ε
3: T → F T'
4: T' → * F T'
5: T' → ε
6: F → ( E )
7: F → n
```

---

## Parsing Algorithm (Stack-Based)

### Initialization
```
Stack: [$ E]
Input: n + n * n $
Pos:   0
```

### Parsing Steps

1. **Pop E from stack, lookahead = n**
   - M[E, n] = 0 (E → T E')
   - Push E', T
   - Stack: [$ E' T]

2. **Pop T from stack, lookahead = n**
   - M[T, n] = 3 (T → F T')
   - Push T', F
   - Stack: [$ E' T' F]

3. **Pop F from stack, lookahead = n**
   - M[F, n] = 7 (F → n)
   - Push n
   - Stack: [$ E' T' n]

4. **Pop n from stack, lookahead = n**
   - Match! Advance input
   - Stack: [$ E' T']
   - Input: [+ n * n $]

5. **Pop T' from stack, lookahead = +**
   - M[T', +] = 5 (T' → ε)
   - Push nothing (ε)
   - Stack: [$ E']

6. **Pop E' from stack, lookahead = +**
   - M[E', +] = 1 (E' → + T E')
   - Push E', T, +
   - Stack: [$ E' T +]

... (continue until accept)

---

## Code Usage Examples

### 1. Basic Parsing
```python
from grammar import Grammar
from ll1_table import LL1ParsingTable
from ll1_parser import LL1Parser
from tokenizer import Tokenizer

# Create grammar
grammar = Grammar()

# Build parsing table
parsing_table = LL1ParsingTable(grammar)

# Tokenize input
tokenizer = Tokenizer()
tokens = tokenizer.tokenize("n + n * n")

# Parse
parser = LL1Parser(grammar, parsing_table)
success, message = parser.parse(tokens)

# View trace
parser.print_parse_trace()
```

### 2. Get FIRST/FOLLOW Sets
```python
from ll1_helper import LL1Helper

helper = LL1Helper(grammar)
first_E = helper.get_first_set('E')  # {'n', '('}
follow_E = helper.get_follow_set('E')  # {'$', ')'}
helper.print_sets()  # Print all sets
```

### 3. Custom Input
```python
test_cases = ["n", "n+n", "n*n", "(n)", "(n+n)*n"]

for expr in test_cases:
    tokens = tokenizer.tokenize(expr)
    parser = LL1Parser(grammar, parsing_table)
    success, msg = parser.parse(tokens)
    print(f"{expr}: {'✓' if success else '✗'}")
```

---

## Common Errors & Solutions

### Error: "No production for M[A, a]"
**Cause**: Parsing table has no entry for non-terminal A with lookahead a
**Solution**: Grammar conflict - may not be LL(1)

### Error: "Expected X, got Y"
**Cause**: Terminal mismatch during parsing
**Solution**: Input string has syntax error

### Error: "Max steps exceeded"
**Cause**: Infinite loop in parsing
**Solution**: Check for grammar cycles or infinite derivations

---

## Key Formulas

### FIRST(α) where α = X₁X₂...Xₙ
```
FIRST(α) = FIRST(X₁) - {ε}
         + (FIRST(X₂) - {ε}) if ε ∈ FIRST(X₁)
         + ...
         + {ε} if ε ∈ FIRST(Xᵢ) for all i
```

### FOLLOW(A)
```
If B → α A β:
    FOLLOW(A) ⊇ (FIRST(β) - {ε})
    If ε ∈ FIRST(β):
        FOLLOW(A) ⊇ FOLLOW(B)
```

### Parsing Table Construction
```
For each production A → α:
    For each a ∈ FIRST(α):
        M[A, a] = A → α
    If ε ∈ FIRST(α):
        For each b ∈ FOLLOW(A):
            M[A, b] = A → α
```

---

## Input Format

**Supported Characters:**
- `n` - Number/variable
- `+` - Addition
- `*` - Multiplication
- `(` - Left parenthesis
- `)` - Right parenthesis
- `$` - End of input (added automatically)

**Examples:**
```
n          → Valid
n+n        → Valid
n*n        → Valid
n + n * n  → Valid (spaces ignored)
(n)        → Valid
(n+n)*n    → Valid
n+(n)*n    → Valid
```

---

## Implementation Statistics

| Metric | Value |
|--------|-------|
| Total Lines of Code | ~500 |
| Number of Classes | 6 |
| FIRST Set Iterations | ~3 |
| FOLLOW Set Iterations | ~4 |
| Parsing Table Size | 5 × 6 |
| Max Parsing Steps | ~20 |

---

## Running Tests

```bash
# Run all tests
python main.py

# Expected output:
# ✓ ACCEPTED for: n, n+n, n*n, n+n*n, (n), (n+n), (n+n)*n
```

---

**Last Updated**: 2024  
**Status**: ✓ Production Ready
