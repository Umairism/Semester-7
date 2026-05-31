# Compiler Construction - Final Term Study Notes

## Context-Free Grammar (CFG)

A context-free grammar is a formal way to describe the syntax of a language.

- A CFG is written as `G = (V, T, P, S)`.
- `V` is the set of non-terminals.
- `T` is the set of terminals.
- `P` is the set of productions.
- `S` is the start symbol.

CFG is important because regular expressions can describe simple token patterns, but CFG is needed for nested and recursive syntax.

Example:

- `S -> aSb | epsilon`

This generates strings like `ab`, `aabb`, and `aaabbb`.

## Ambiguity in CFG

A grammar is ambiguous if one string has more than one parse tree or more than one derivation.

Example:

- `E -> E + E | E * E | id`

The string `id + id * id` may mean either `(id + id) * id` or `id + (id * id)`.

Ambiguity is a problem because it creates confusion about precedence and makes semantic analysis unreliable.

To remove ambiguity, rewrite the grammar to enforce precedence and associativity.

Better grammar for expressions:

- `E -> E + T | T`
- `T -> T * F | F`
- `F -> id`

This gives `*` higher precedence than `+`.

## Top-Down Parsing

Top-down parsing starts from the start symbol and tries to derive the input string.

- It builds the parse tree from root to leaves.
- It expands non-terminals using productions.
- Common forms are recursive descent and predictive parsing.

For predictive parsing, the grammar should be LL(1), not ambiguous, and free of left recursion.

## Removing Left Recursion

Left recursion happens when a non-terminal calls itself on the left side.

Example:

- `E -> E + T | T`

This causes infinite recursion in top-down parsers.

General form:

- `A -> A alpha | beta`

Transformation:

- `A -> beta A'`
- `A' -> alpha A' | epsilon`

Example after removing left recursion:

- `E -> T E'`
- `E' -> + T E' | epsilon`

## FIRST() and FOLLOW() Sets

These sets are used to build LL(1) parse tables.

FIRST(X) is the set of terminals that can begin strings derived from X. If X can produce the empty string, `epsilon` is included.

FOLLOW(A) is the set of terminals that can appear immediately after A in a sentential form. The end marker `$` is always in FOLLOW(start symbol).

FIRST helps decide which production can start with a given input token. FOLLOW helps when a non-terminal can derive `epsilon`.

## LL(1) Predictive Parsing

LL(1) means:

- Left to right scan
- Leftmost derivation
- One lookahead token

For a grammar to be LL(1):

- FIRST sets of alternative productions should not overlap.
- If a production can produce `epsilon`, its FIRST and FOLLOW should not conflict.

The parse table has rows for non-terminals and columns for terminals and `$`.

Basic stack parsing steps:

1. Push `$` and the start symbol on the stack.
2. Read the first input token.
3. If the top of the stack is a terminal, match it with the input.
4. If the top is a non-terminal, use the parse table.
5. Accept when both stack and input finish.

## Bottom-Up Parsing

Bottom-up parsing starts from the input and reduces it to the start symbol.

- It builds the parse tree from leaves to root.
- It uses shift and reduce operations.
- It is the reverse of derivation.

Shift-reduce parsing works by moving input symbols onto a stack and then reducing a handle on the stack to a non-terminal.

## LR Parsing Family

LR parsing is a strong bottom-up parsing method.

### LR(0)

- Left to right scan
- Rightmost derivation in reverse
- Zero lookahead
- Uses items with a dot to show progress in productions

### SLR

- Simple LR
- Uses FOLLOW sets to reduce conflicts
- Better than LR(0), but still limited

### CLR

- Canonical LR
- Uses lookahead tokens in items
- More powerful than SLR
- Parse tables are larger

### LALR

- Look-Ahead LR
- Combines the power of CLR with smaller tables
- Common in practical parser generators like Yacc and Bison

## Deterministic Flow in Shift-Reduce Parsing

LR parsers use a state machine.

- Each state shows how much of the grammar has been recognized.
- The parse table tells the parser whether to shift, reduce, accept, or report an error.
- The process is deterministic because the action is chosen uniquely from state and lookahead.

## Parse Table and Stack Processing

The parse table has two main parts:

- ACTION: shift, reduce, accept, or error
- GOTO: next state for non-terminals

Typical LR parser steps:

1. Initialize the stack with state 0.
2. Read the input token.
3. Use the current state and token to check ACTION.
4. Shift or reduce accordingly.
5. Use GOTO after a reduction.
6. Accept when parsing succeeds.

Example trace idea:

- For expression input like `id + id`, the parser may shift `id`, reduce to `T`, reduce to `E`, shift `+`, shift `id`, and reduce again.

## Quick Revision Points

- CFG describes syntax.
- Ambiguity must be removed.
- Left recursion must be removed for LL parsers.
- FIRST and FOLLOW build LL(1) tables.
- LL(1) parsing is top-down.
- LR parsing is bottom-up and more powerful.
- LALR is the practical compromise between power and table size.

## Short Exam Notes

- Top-down parsing is root to leaves.
- Bottom-up parsing is leaves to root.
- LL(1) uses one lookahead.
- LR parsing uses state-based shift-reduce decisions.
- Ambiguous grammars should be rewritten before table construction.
