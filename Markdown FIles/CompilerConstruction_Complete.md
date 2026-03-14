# Compiler Construction – Comprehensive Course Notes

## Table of Contents

1. [Overview: From Source to Machine Code](#overview-from-source-to-machine-code)
2. [Compiler Architecture](#compiler-architecture)
3. [Lexical Analysis (Phase 1)](#lexical-analysis-phase-1)
4. [Tokens and Categories](#tokens-and-categories)
5. [Regular Expressions (RE)](#regular-expressions-re)
6. [Deterministic vs Non-Deterministic Automata](#deterministic-vs-non-deterministic-automata)
7. [Converting to Deterministic Finite Automata (DFA)](#converting-to-deterministic-finite-automata-dfa)
8. [Syntax Analysis (Phase 2)](#syntax-analysis-phase-2)
9. [Context-Free Grammars (CFG)](#context-free-grammars-cfg)
10. [Parse Trees](#parse-trees)
11. [Advanced Topics](#advanced-topics)

---

## Overview: From Source to Machine Code

### The Compilation Process

A compiler transforms source code written by humans into machine code executedby computers. This involves multiple transformations to ensure correctness and efficiency.

#### Complete Compilation Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│                      SOURCE CODE                             │
│              (Human-written program in language)             │
└────────────────────────┬─────────────────────────────────────┘
                         │
         ╔═══════════════════════════════════╗
         ║   FRONTEND: Source Understanding  ║
         ╚═══════════════════════════════════╝
                         │
        ┌────────────────┴────────────────┐
        │ **Lexical Analysis**            │
        │ Words/Tokens                    │
        └────────────────┬────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │ **Syntax Analysis**             │
        │ Sentence/Structure              │
        └────────────────┬────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │ **Semantic Analysis**           │
        │ Meaning/Type Checking           │
        └────────────────┬────────────────┘
                         │
         ╔═══════════════════════════════════╗
         ║   MIDDLE-END: Transformation      ║
         ╚═══════════════════════════════════╝
                         │
        ┌────────────────┴────────────────┐
        │ **Intermediate Code Gen**       │
        │ Memory Representation           │
        └────────────────┬────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │ **Code Optimization**           │
        │ Improve Efficiency              │
        └────────────────┬────────────────┘
                         │
         ╔═══════════════════════════════════╗
         ║   BACKEND: Target Generation      ║
         ╚═══════════════════════════════════╝
                         │
        ┌────────────────┴────────────────┐
        │ **Target Code Generation**      │
        │ Platform-Specific Code          │
        └────────────────┬────────────────┘
                         │
└────────────────────────┴─────────────────────────────────────┘
         Machine-Readable Code (Executable)
```

### Goal

**Goal:** Transform source code into efficient, correct machine code that preserves the program's semantics (meaning).

---

## Compiler Architecture

### Three-Part Structure

The compilation process divides into three major parts:

#### Part 1: Source Language Understanding

Involves three analysis phases:

| Phase | Input | Process | Output |
|:--|:--|:--|:--|
| **Lexical** | Character stream | Tokenization | Token stream |
| **Syntax** | Token stream | Parsing | Parse tree |
| **Semantic** | Parse tree | Type checking | Verified AST |

**Purpose:** Understand what the source code says

#### Part 2: Transformation

Converts representation:

| Phase | Input | Output | Purpose |
|:--|:--|:--|:--|
| **Intermediate Code Gen** | Semantic tree | Intermediate representation | Platform-independent |
| **Optimization** | Intermediate code | Optimized intermediate code | Better performance |

**Purpose:** Create efficient internal representation

#### Part 3: Target Code Generation

| Phase | Input | Output | Purpose |
|:--|:--|:--|:--|
| **Code Gen** | Optimized IR | Target assembly/machine code | Platform-specific execution |

**Purpose:** Generate executable code for specific platform

---

## Lexical Analysis (Phase 1)

### Objective

Transform a stream of characters into meaningful **tokens** (words).

### Process

```
Source Code
    ↓
Character Analysis
    ↓
Pattern Matching
    ↓
Token Recognition
    ↓
Token Stream
```

### Example

**Input (Character Stream):**
```
int x = 42;
```

**Output (Token Stream):**
```
[KEYWORD: int] [IDENTIFIER: x] [OPERATOR: =] [NUMBER: 42] [PUNCTUATION: ;]
```

---

## Tokens and Categories

### Token Definition

A **Token** is the smallest meaningful unit recognized by the lexical analyzer.

### Token Categories

Tokens in programming languages fall into six main categories:

#### 1. Keywords (Finite)

**Definition:** Predefined, reserved words with special meaning

**Characteristics:**
- Fixed set for each language
- Cannot be used as variable names
- Reserved by language specification

**Examples:**
```
if, else, while, for, int, float, return, class, public, private
```

**Representation:**
```
<key> => if | else | while | int | float | ...
```

#### 2. Identifiers (Infinite)

**Definition:** Names given to variables, functions, classes, etc.

**Characteristics:**
- Infinite possibilities (user-defined)
- Follow naming rules
- Represent program entities

**Naming Rules (Typical):**
- Starts with letter or underscore
- Contains letters, digits, underscores
- Case-sensitive

**Regular Expression:**
```
<id> => (letter | _)(letter | digit | _)*
```

**Examples:**
```
myVariable, Count_1, _private, calculateSum, x, student_name
```

#### 3. Numbers (Infinite)

**Definition:** Numeric literals used in code

**Characteristics:**
- Infinite number of possible values
- Can be integers or floating-point
- May include sign

**Types:**
- **Integers:** `42`, `-17`, `0`, `1000`
- **Floats:** `3.14`, `2.0`, `-0.5`, `1.23e-4`

**Regular Expression:**
```
<Num> => (+ | - | ε) (<int> | <float>)
<int> => digit+
<float> => digit*.digit+
```

#### 4. Literals (Mostly Infinite)

**Definition:** String and character constants

**Characteristics:**
- Enclosed in quotes
- Character set is finite, but combinations infinite

**Types:**
- **Character Literal:** `'a'`, `'Z'`, `'\n'`
- **String Literal:** `"Hello"`, `"world"`, `"test string"`

**Regular Expression:**
```
<literal> => <char> | <string>
<char> => '<All>'           (any character in quotes)
<string> => "<All>+"        (one or more characters)
<All> => letter | digit | special_char | operator | escape_seq
```

#### 5. Operators (Finite)

**Definition:** Symbols representing operations

**Categories:**
- **Arithmetic:** `+`, `-`, `*`, `/`, `%`
- **Logical:** `&&`, `||`, `!`
- **Comparison:** `<`, `>`, `<=`, `>=`, `==`, `!=`
- **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- **Unary:** `++`, `--`

**Regular Expression:**
```
<op> => <Arithmetic> | <logical> | <Compound>
<Arithmetic> => + | - | * | / | %
<logical> => (&&) | (||)
<Comparison> => < | > | <= | >= | == | !=
<Compound> => ++ | -- | += | -= | *= | /= | %=
```

#### 6. Comments (Infinite)

**Definition:** Non-executable text for documentation

**Types:**
- **Single-line:** `// comment text` (rest of line)
- **Multi-line:** `/* comment text */` (spans multiple lines)

**Regular Expression:**
```
<Comments> => <single> | <multi>
<single> => // <All>*              (to end of line)
<multi> => /* <All>* */            (can span lines)
```

---

## Regular Expressions (RE)

### Purpose

**Regular Expressions** describe patterns for recognizing tokens from character streams.

### Key Operators

| Operator | Name | Meaning | Example |
|:--|:--|:--|:--|
| **concatenation** | Sequence | One pattern followed by another | `ab` matches "ab" |
| **\|** | Alternation (OR) | Either pattern | `a\|b` matches "a" or "b" |
| **\*** | Kleene Star | Zero or more repetitions | `a*` matches "", "a", "aa", ... |
| **+** | Plus | One or more repetitions | `a+` matches "a", "aa", ... |
| **?** | Optional | Zero or one occurrence | `a?` matches "" or "a" |

### Regular Expression Examples

| Pattern | Language | Examples |
|:--|:--|:--|
| `ab*` | a followed by zero or more b's | a, ab, abb, abbb |
| `(ab)*` | Zero or more repetitions of "ab" | "", ab, abab, ababab |
| `(a\|b)*` | Zero or more a's or b's | "", a, b, aa, ab, ba, bb, aba |
| `[a-z]+` | One or more lowercase letters | a, abc, xyz |
| `[0-9]{1,3}` | 1 to 3 digits | 1, 42, 999 |

---

## Deterministic vs Non-Deterministic Automata

### The Conversion Challenge

A regex describes a pattern, but directly implementing it may lose important details. We need to convert through automata stages.

### NFA vs DFA

#### Non-Deterministic Finite Automaton (NFA)

**Characteristics:**
- **Non-Deterministic:** From one state with input, multiple possible next states (choice points)
- **Detailed:** Preserves all structural information from RE
- **Elaborate:** Represents regex complexity explicitly

**Disadvantages:**
- Not suitable for direct implementation
- Requires backtracking (inefficient)
- Multiple paths to explore

#### Deterministic Finite Automaton (DFA)

**Characteristics:**
- **Deterministic:** From one state with input, exactly one next state (no choices)
- **Compact:** Consolidates similar paths
- **Summarized:** Skips some details for efficiency

**Advantages:**
- Suitable for implementation
- Single path (no backtracking)
- Efficient execution

### Conversion Problem

```
Regex → NFA          DFA → Implementation
        (Detailed)   (Efficient)
         ↓           ↓
Problem: Direct NFA implementation is inefficient!

Solution:
Regex → NFA → DFA → Implementation
         ↓     ↓
    Preserve  Optimize
    detail    for speed
```

---

## Converting to Deterministic Finite Automata (DFA)

### What is a DFA?

A **Deterministic Finite Automaton** is a mathematical model with:
- **Q:** Set of states
- **Σ:** Input alphabet
- **δ:** State transition function
- **q₀:** Starting state
- **F:** Accepting states

### State Table Representation

A DFA is often represented as a **transition table**:

```
       Input: a  b  c
State
  1      2   3   3
  2      2   3   -
  3      3   4   4
  4      4   4   5
  5      5   5   7
  6      5   5   7
  7      7   8   7
  8      7   8   -
```

**Rules:**
- **Rows:** States (1, 2, 3, ...)
- **Columns:** Input symbols (a, b, c, ...)
- **Entries:** Next state or '-' (error)
- **Accepting states:** Often marked in table

### Types of DFAs

#### Complete DFA
- **Definition:** Every state has a transition for every input symbol
- **Characteristic:** No gaps in transition table
- **Efficiency:** Always know next state

#### Characteristic DFA
- **Definition:** Some states may lack transitions for certain inputs
- **Characteristic:** Gaps in transition table (indicated by '-' or empty)
- **Efficiency:** Implicit error handling

### Example: Pattern ab*

**Regex:** `ab*` (a followed by zero or more b's)

**State Diagram:**
```
      Start
        ↓
    ┌─────────┐
    │    1    │
    └────┬────┘
         │ a
         ↓
    ┌─────────┐       b    ┌─ loop
    │    2    │◄────────────┤
    └────┬────┘             └─
   Accept↑ (also state 2)
```

**Transition Table for ab*:**

```
        a    b
  1     2    ERR
  2    ERR   2  [accepting]
  ERR  ERR   ERR
```

**Analysis:**
- State 1: Start state (looking for 'a')
- State 2: After seeing 'a' (can continue with b's or accept)
- Accepting state: State 2 (we've seen 'a')

---

## DFA Optimization

### Process: Minimize States

When you have a DFA, you can optimize it by merging equivalent states.

#### Steps

1. **Create Transition Table**
2. **Separate States into Groups**
   - Group 1: Non-accepting states
   - Group 2: Accepting states
3. **Refine Groups**: Merge states with identical transitions
4. **Build Optimized DFA**

#### Example Optimization

**Original States:**
- State 1, 2: Non-accepting (similar transitions) → Merge
- State 7, 8: Accepting (similar transitions) → Merge

**Result:** Fewer states, same language recognition

---

## Syntax Analysis (Phase 2)

### Objective

Transform a stream of tokens into a meaningful sentence structure (parse tree).

### Process

```
Token Stream
    ↓
Parser (Syntax Analyzer)
    ↓
Sentence Validation
    ↓
Parse Tree
    ↓
Semantic Verification
```

### Input vs Output

| Phase | Level | Input | Output |
|:--|:--|:--|:--|
| **Lexical** | Words | Characters | Tokens |
| **Syntax** | Sentences | Tokens | Parse tree |
| **Semantic** | Meaning | Parse tree | Verified tree |

### Key Difference from Lexical Analysis

**Lexical Analysis:**
- Uses Regular Expressions
- Can only iterate within sequences
- Example: `a*b` is easy

**Syntax Analysis:**
- Uses Context-Free Grammars
- Can iterate without sequence (recursion)
- Example: Nested parentheses, nested functions

---

## Context-Free Grammars (CFG)

### Purpose

**CFG** provides rules to generate sentences from a language, or to validate if a token sequence forms a valid sentence.

### Key Concepts

#### Terminals

- **Definition:** Alphabet symbols (the tokens)
- **Notation:** Lowercase or quoted symbols
- **Example:** `if`, `(`, `)`, identifier, number

#### Non-Terminals

- **Definition:** Variables representing language constructs
- **Notation:** Angle brackets or uppercase
- **Example:** `<statement>`, `<expression>`, `<program>`

### Production Rules

A **Production** specifies how to expand a non-terminal into a sequence of terminals and non-terminals.

**Notation:** `A → α` where:
- `A` is a non-terminal (left side)
- `α` is a sequence of terminals/non-terminals (right side)

### Example CFG

**Simple Expression Grammar:**

```
<expr>      → <expr> + <term> | <term>
<term>      → <term> * <factor> | <factor>
<factor>    → ( <expr> ) | number | identifier
```

**Explanation:**
- Expression is: term, or term+term, or term+term+term...
- Term is: factor, or factor*factor...
- Factor is: number, identifier, or grouped expression

### Language Definition

- Given start symbol and productions, the CFG defines the language
- Language = all possible token sequences derivable from start symbol

---

## Parse Trees

### Definition

A **Parse Tree** (or Derivation Tree) shows how a token sequence was derived from the grammar.

### Structure

- **Root:** Start symbol
- **Internal Nodes:** Non-terminals
- **Leaf Nodes:** Terminals (tokens)
- **Edges:** Production applications

### Derivation Process

Transform the start symbol step-by-step using production rules:

**Example:** For `<expr> → <expr> + <term>`

```
Step 1: <expr>
        ↓ (apply <expr> → <expr> + <term>)
Step 2: <expr> + <term>
        ↓ (apply <expr> → <term>)
Step 3: <term> + <term>
        ↓ (continue expanding...)
Step N: Final token sequence
```

### Corresponding Parse Tree

Shows the full derivation graphically:

```
           <expr>
          /  |  \
      <expr> + <term>
        |       |
     <term>   factor
        |       |
    <factor>   number
        |
     number
```

**Reading Leaves Left-to-Right:** `number + number`

---

## Advanced Topics

### Correlation Between Sentence and Grammar

For a valid sentence:
- Every production application follows the rules
- Syntax tree shows valid derivation
- Semantic checks verify meaning

### Error Handling

**Syntax Errors:**
- Token sequence doesn't match any production
- Parser detects: "Expected X but found Y"

**Recovery Strategies:**
- Skip unexpected token
- Attempt alternative production
- Synchronize at known points

### Grammar Characteristics

| Property | Significance |
|:--|:--|
| **Ambiguity** | Multiple derivations for same sentence (usually bad) |
| **Left Recursion** | Production like `A → Aα` (can cause infinite loops) |
| **Precedence** | Operator priority (*, / before +, -) |
| **Associativity** | Order for same-precedence operators (left vs right) |

---

## Summary & Learning Path

### Compilation Stages in Order

1. **Lexical** → Convert characters to tokens
2. **Syntax** → Convert tokens to parse tree
3. **Semantic** → Verify meaning and type correctness
4. **IR Generation** → Create internal representation
5. **Optimization** → Improve efficiency
6. **Code Generation** → Create executable

### Key Technologies

- **Regex** for pattern matching
- **Automata** for recognition
- **Grammar** for structure

### Important Concepts

- Finite vs Infinite token categories
- NFA vs DFA tradeoff
- RE vs CFG differences
- Token recognition flow

---

## Implementation Notes

### Lexer Implementation

```
Input: Character stream
Process:
  1. Read characters
  2. Match against token patterns (regex)
  3. When match complete, emit token
  4. Continue with next character
Output: Token stream
```

### Parser Implementation

```
Input: Token stream
Process:
  1. Read tokens
  2. Check against grammar rules
  3. When rule matches, reduce
  4. Build parse tree
Output: Parse tree or error
```

### Integration

Both lexer and parser work together:
```
Source Code → Lexer → Token Stream → Parser → Parse Tree
```
