"""
DFA (Deterministic Finite Automaton) for Lexical Analysis
Implements lexical rules using DFA state machines to recognize tokens
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple


class TokenType(Enum):
    """Token types recognized by the DFA"""
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    FLOAT = "FLOAT"
    OPERATOR = "OPERATOR"
    PUNCTUATION = "PUNCTUATION"
    STRING = "STRING"
    COMMENT = "COMMENT"
    WHITESPACE = "WHITESPACE"
    UNKNOWN = "UNKNOWN"
    EOF = "EOF"


@dataclass
class Token:
    """Represents a recognized token"""
    type: TokenType
    value: str
    line: int
    column: int

    def __str__(self):
        return f"<{self.type.value}: '{self.value}' at {self.line}:{self.column}>"


class DFALexer:
    """
    DFA-based Lexical Analyzer
    Uses deterministic finite automata to recognize lexical tokens
    """

    # Keywords set
    KEYWORDS = {
        'if', 'else', 'while', 'for', 'do', 'break', 'continue',
        'return', 'int', 'float', 'char', 'void', 'main', 'class',
        'public', 'private', 'static', 'const', 'true', 'false'
    }

    # Operators
    OPERATORS = {
        '+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
        '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '+=', '-=',
        '*=', '/=', '%='
    }

    # Punctuation
    PUNCTUATION = {'(', ')', '{', '}', '[', ']', ';', ',', '.', '?', ':'}

    def __init__(self):
        self.input_text = ""
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def tokenize(self, text: str) -> List[Token]:
        """
        Main tokenization method
        Converts input text into list of tokens using DFA
        """
        self.input_text = text
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []

        while self.position < len(self.input_text):
            self._skip_whitespace()

            if self.position >= len(self.input_text):
                break

            token = self._next_token()
            if token and token.type != TokenType.WHITESPACE:
                self.tokens.append(token)

        return self.tokens

    def _current_char(self) -> Optional[str]:
        """Get current character without advancing"""
        if self.position < len(self.input_text):
            return self.input_text[self.position]
        return None

    def _peek_char(self, offset: int = 1) -> Optional[str]:
        """Peek ahead at character"""
        pos = self.position + offset
        if pos < len(self.input_text):
            return self.input_text[pos]
        return None

    def _advance(self) -> Optional[str]:
        """Move to next character and return current"""
        if self.position < len(self.input_text):
            ch = self.input_text[self.position]
            self.position += 1
            if ch == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            return ch
        return None

    def _skip_whitespace(self):
        """DFA State: Skip whitespace characters"""
        while self.position < len(self.input_text) and self.input_text[self.position].isspace():
            self._advance()

    def _next_token(self) -> Optional[Token]:
        """Main DFA token recognition"""
        if self.position >= len(self.input_text):
            return Token(TokenType.EOF, "", self.line, self.column)

        start_line = self.line
        start_column = self.column
        ch = self._current_char()

        # DFA State: String literals (single or double quoted)
        if ch in ('"', "'"):
            return self._dfa_string(start_line, start_column)

        # DFA State: Comments
        if ch == '/' and self._peek_char() == '/':
            return self._dfa_line_comment(start_line, start_column)

        if ch == '/' and self._peek_char() == '*':
            return self._dfa_block_comment(start_line, start_column)

        # DFA State: Numbers (integers and floats)
        if ch.isdigit():
            return self._dfa_number(start_line, start_column)

        # DFA State: Identifiers and Keywords
        if ch.isalpha() or ch == '_':
            return self._dfa_identifier(start_line, start_column)

        # DFA State: Operators
        if ch in self.OPERATORS or (ch in '!<>=' or ch in '+-*/%&|^'):
            return self._dfa_operator(start_line, start_column)

        # DFA State: Punctuation
        if ch in self.PUNCTUATION:
            self._advance()
            return Token(TokenType.PUNCTUATION, ch, start_line, start_column)

        # Unknown character
        self._advance()
        return Token(TokenType.UNKNOWN, ch, start_line, start_column)

    def _dfa_string(self, start_line: int, start_column: int) -> Token:
        """
        DFA for String Recognition
        States: START -> IN_STRING -> END
        """
        quote_char = self._advance()  # Consume opening quote
        value = quote_char

        # IN_STRING state
        while self.position < len(self.input_text):
            ch = self._current_char()

            if ch == quote_char:
                # Check if escaped
                if value[-1] != '\\':
                    value += self._advance()  # Consume closing quote
                    break
                else:
                    value += self._advance()
            elif ch == '\\':
                value += self._advance()
                if self.position < len(self.input_text):
                    value += self._advance()  # Consume escaped character
            else:
                value += self._advance()

        return Token(TokenType.STRING, value, start_line, start_column)

    def _dfa_line_comment(self, start_line: int, start_column: int) -> Token:
        """
        DFA for Line Comment Recognition
        States: START -> IN_COMMENT -> END
        """
        value = ""
        while self.position < len(self.input_text) and self._current_char() != '\n':
            value += self._advance()
        return Token(TokenType.COMMENT, value, start_line, start_column)

    def _dfa_block_comment(self, start_line: int, start_column: int) -> Token:
        """
        DFA for Block Comment Recognition
        States: START -> IN_COMMENT -> MAYBE_END -> END
        """
        value = ""
        self._advance()  # /
        self._advance()  # *
        value = "/*"

        while self.position < len(self.input_text) - 1:
            ch = self._current_char()
            value += self._advance()

            if ch == '*' and self._current_char() == '/':
                value += self._advance()
                break

        return Token(TokenType.COMMENT, value, start_line, start_column)

    def _dfa_number(self, start_line: int, start_column: int) -> Token:
        """
        DFA for Number Recognition
        States: START -> DIGITS -> [DECIMAL_POINT -> DIGITS] -> END
        """
        value = ""
        token_type = TokenType.NUMBER

        # INTEGER state
        while self.position < len(self.input_text) and self._current_char().isdigit():
            value += self._advance()

        # Check for decimal point (transition to FLOAT)
        if self._current_char() == '.' and self._peek_char() and self._peek_char().isdigit():
            token_type = TokenType.FLOAT
            value += self._advance()  # Consume decimal point

            # FLOAT state
            while self.position < len(self.input_text) and self._current_char().isdigit():
                value += self._advance()

        # Optional exponent
        if self._current_char() in ('e', 'E'):
            token_type = TokenType.FLOAT
            value += self._advance()
            if self._current_char() in ('+', '-'):
                value += self._advance()
            while self.position < len(self.input_text) and self._current_char().isdigit():
                value += self._advance()

        return Token(token_type, value, start_line, start_column)

    def _dfa_identifier(self, start_line: int, start_column: int) -> Token:
        """
        DFA for Identifier and Keyword Recognition
        States: START -> ALPHA -> [ALPHA|DIGIT|UNDERSCORE] -> END
        """
        value = ""

        # First character (already checked to be alpha or underscore)
        while self.position < len(self.input_text):
            ch = self._current_char()
            if ch.isalnum() or ch == '_':
                value += self._advance()
            else:
                break

        # Check if it's a keyword
        if value in self.KEYWORDS:
            return Token(TokenType.KEYWORD, value, start_line, start_column)
        else:
            return Token(TokenType.IDENTIFIER, value, start_line, start_column)

    def _dfa_operator(self, start_line: int, start_column: int) -> Token:
        """
        DFA for Operator Recognition
        States: START -> SINGLE_CHAR -> [MAYBE_DOUBLE_CHAR] -> END
        """
        value = self._advance()

        # Try to form two-character operators
        if self.position < len(self.input_text):
            two_char = value + self._current_char()
            if two_char in self.OPERATORS:
                value = self._advance()
                return Token(TokenType.OPERATOR, value, start_line, start_column)

        return Token(TokenType.OPERATOR, value, start_line, start_column)

    def print_tokens(self, verbose: bool = False):
        """Print all recognized tokens"""
        print("\n" + "="*80)
        print("TOKENS RECOGNIZED BY DFA")
        print("="*80)
        print(f"{'Token Type':<15} {'Value':<20} {'Line:Column':<15}")
        print("-"*80)

        for token in self.tokens:
            if verbose:
                print(f"{token.type.value:<15} {token.value:<20} {token.line}:{token.column}")
            else:
                print(f"{token.type.value:<15} '{token.value}'")

        print("="*80)
        print(f"Total tokens: {len(self.tokens)}\n")


def main():
    """Test the DFA Lexer with sample inputs"""
    lexer = DFALexer()

    # Test case 1: Simple expressions
    print("\n" + "▶"*40)
    print("TEST 1: Simple Expression")
    print("▶"*40)
    code1 = "int x = 5 + 3.14;"
    print(f"Input: {code1}")
    tokens1 = lexer.tokenize(code1)
    lexer.print_tokens()

    # Test case 2: Keywords and identifiers
    print("\n" + "▶"*40)
    print("TEST 2: Keywords and Identifiers")
    print("▶"*40)
    code2 = "if (x > 10) { return true; }"
    print(f"Input: {code2}")
    tokens2 = lexer.tokenize(code2)
    lexer.print_tokens()

    # Test case 3: Operators
    print("\n" + "▶"*40)
    print("TEST 3: Complex Operators")
    print("▶"*40)
    code3 = "a += 5; b = c && d || e;"
    print(f"Input: {code3}")
    tokens3 = lexer.tokenize(code3)
    lexer.print_tokens()

    # Test case 4: Strings and comments
    print("\n" + "▶"*40)
    print("TEST 4: Strings and Comments")
    print("▶"*40)
    code4 = '''char *str = "Hello World"; // This is a comment
    /* Block comment */ int num = 42;'''
    print(f"Input:\n{code4}")
    tokens4 = lexer.tokenize(code4)
    lexer.print_tokens()

    # Test case 5: Numbers (integers, floats, scientific notation)
    print("\n" + "▶"*40)
    print("TEST 5: Different Number Formats")
    print("▶"*40)
    code5 = "int a = 123; float b = 45.67; double c = 1.5e-10;"
    print(f"Input: {code5}")
    tokens5 = lexer.tokenize(code5)
    lexer.print_tokens()

    # Interactive mode
    print("\n" + "▶"*40)
    print("INTERACTIVE MODE")
    print("▶"*40)
    while True:
        user_input = input("\nEnter code to tokenize (or 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            break
        if user_input:
            tokens = lexer.tokenize(user_input)
            lexer.print_tokens()


if __name__ == "__main__":
    main()
