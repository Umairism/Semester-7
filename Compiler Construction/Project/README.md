# LL(1) Parser Implementation

## Overview
This project implements a complete **LL(1) Parser** in Python for parsing arithmetic expressions. The implementation follows the classic top-down parsing methodology with a parsing table and stack-based approach.

## Key Components

### 1. **Grammar Definition** (`grammar.py`)
- **Original Grammar** (with left recursion):
  - E → E + T | T
  - T → T * F | F
  - F → (E) | n

- **Converted Grammar** (left recursion eliminated for LL(1)):
  ```
  E  → T E'
  E' → + T E' | ε
  T  → F T'
  T' → * F T' | ε
  F  → (E) | n
  ```

**Why Conversion?** LL(1) parsers cannot handle left-recursive grammars. The grammar is converted to right-recursive form using **left recursion elimination**.

### 2. **FIRST and FOLLOW Sets** (`ll1_helper.py`)
Computes the FIRST and FOLLOW sets for all non-terminals:
- **FIRST(X)**: Set of terminals that can appear first in a derivation from X
- **FOLLOW(X)**: Set of terminals that can appear immediately after X in some sentential form

**Example:**
```
FIRST(E) = {'(', 'n'}
FIRST(E') = {'+', 'ε'}
FOLLOW(E) = {'$', ')'}
FOLLOW(E') = {'$', ')'}
```

### 3. **LL(1) Parsing Table** (`ll1_table.py`)
Constructs the parsing table M[A, a]:
- **A**: Non-terminal
- **a**: Terminal (lookahead symbol)
- **M[A, a]**: The production to apply when A is on top of stack and a is the current token

**Table Construction Rules:**
1. For each production A → α, add it to M[A, a] for every a ∈ FIRST(α)
2. If ε ∈ FIRST(α), add it to M[A, b] for every b ∈ FOLLOW(A)

### 4. **Tokenizer** (`tokenizer.py`)
Converts input expressions into token arrays:
- Input: `"n + n * n"` (with optional spaces)
- Output: `['n', '+', 'n', '*', 'n', '$']`
- Supports: `n, +, *, (, ), $` (end marker)

### 5. **Stack-Based LL(1) Parser** (`ll1_parser.py`)
Core parsing algorithm:

**Algorithm:**
```
1. stack ← ['$', S]  (where S is start symbol)
2. input_pos ← 0
3. while stack is not empty:
   a. top ← stack.pop()
   b. current_token ← input[input_pos]
   
   if top == '$' and current_token == '$':
       → ACCEPT (success)
   
   if top is terminal:
       if top == current_token:
           → MATCH (pop stack, advance input)
       else:
           → ERROR
   
   if top is non-terminal:
       production ← M[top, current_token]
       if production exists:
           → EXPAND (pop top, push production symbols in reverse)
       else:
           → ERROR
```

## Parsing Process

### Input: `n + n * n`

**Tokens:** `[n, +, n, *, n, $]`

**Parsing Trace:**
```
Step  Stack              Input           Action
──────────────────────────────────────────────────────────
1     $ E                n + n * n $     EXPAND: E → T E'
2     $ E' T             n + n * n $     EXPAND: T → F T'
3     $ E' T' F          n + n * n $     EXPAND: F → n
4     $ E' T' n          n + n * n $     MATCH n
5     $ E' T'            + n * n $       EXPAND: T' → ε
6     $ E'               + n * n $       EXPAND: E' → + T E'
7     $ E' T +           + n * n $       MATCH +
8     $ E' T             n * n $         EXPAND: T → F T'
9     $ E' T' F          n * n $         EXPAND: F → n
10    $ E' T' n          n * n $         MATCH n
11    $ E' T'            * n $           EXPAND: T' → * F T'
12    $ E' T' F *        * n $           MATCH *
13    $ E' T' F          n $             EXPAND: F → n
14    $ E' T' n          n $             MATCH n
15    $ E' T'            $               EXPAND: T' → ε
16    $ E'               $               EXPAND: E' → ε
17    $                  $               ACCEPT ✓
```

## Project Structure

```
Project/
├── grammar.py              # Grammar definition
├── ll1_helper.py          # FIRST/FOLLOW set computation
├── ll1_table.py           # Parsing table construction
├── tokenizer.py           # Input tokenization
├── ll1_parser.py          # Core parser implementation
├── main.py                # Main program with test cases
└── README.md              # This file
```

## Running the Parser

```bash
python main.py
```

### Output Includes:
1. Grammar production rules
2. FIRST and FOLLOW sets for all non-terminals
3. LL(1) Parsing Table
4. Token array representation
5. Detailed parsing trace with step-by-step execution
6. Test cases with multiple expressions

## Test Cases Supported

All the following expressions are successfully parsed:
- ✓ `n`
- ✓ `n + n`
- ✓ `n * n`
- ✓ `n + n * n`
- ✓ `(n)`
- ✓ `(n + n)`
- ✓ `(n + n) * n`
- ✓ `((n))`

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| FIRST Set Computation | O(N²) | O(N) |
| FOLLOW Set Computation | O(N²) | O(N) |
| Parsing Table Construction | O(N) | O(N×M) |
| Parsing | O(n) | O(n) |

Where:
- N = Number of non-terminals
- M = Number of terminals  
- n = Input length

## Key Concepts Implemented

1. **Left Recursion Elimination**: Converted original grammar to avoid left recursion
2. **ε-Productions (Epsilon)**: Handled nullable productions correctly
3. **FIRST/FOLLOW Analysis**: Computed sets using iterative fixed-point algorithm
4. **Predictive Parsing Table**: Generated based on FIRST/FOLLOW sets
5. **Top-Down Parsing**: Stack-based implementation using parse table
6. **Error Detection**: Detects syntax errors and reports position

## Strengths

✓ Complete LL(1) implementation from scratch  
✓ Handles epsilon productions correctly  
✓ Detailed parsing traces  
✓ Multiple test cases  
✓ Clear error messages  
✓ Proper input tokenization  

## Limitations

- Supports only single-character terminals (n, +, *, (, ))
- No semantic actions (can be added for value computation)
- Grammar must be LL(1) compatible (no conflicts in parsing table)
- Limited error recovery

## References

- Compilers: Principles, Techniques, and Tools (Dragon Book)
- Parsing algorithms: LR/LL parser theory
- Grammar transformations for parser generation

---
**Author**: Compiler Construction Project  
**Date**: 2024  
**Language**: Python 3.x
