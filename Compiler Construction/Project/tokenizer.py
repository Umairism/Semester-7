"""
Tokenizer for LL(1) Parser
Converts input string to tokens
"""

class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.position = 0
    
    def tokenize(self, input_string):
        """
        Tokenize the input string
        Input format: expression like "n+n*n" or "n + n * n"
        Returns: list of tokens including $ at the end
        """
        self.tokens = []
        self.position = 0
        
        # Remove spaces
        input_string = input_string.replace(' ', '')
        
        # Tokenize character by character
        for char in input_string:
            if char == 'n':
                self.tokens.append('n')
            elif char == '+':
                self.tokens.append('+')
            elif char == '*':
                self.tokens.append('*')
            elif char == '(':
                self.tokens.append('(')
            elif char == ')':
                self.tokens.append(')')
            else:
                raise ValueError(f"Unknown character: {char}")
        
        # Add end-of-input marker
        self.tokens.append('$')
        
        return self.tokens
    
    def get_token(self, index):
        """Get token at specific index"""
        if index < len(self.tokens):
            return self.tokens[index]
        return '$'
    
    def get_tokens_as_string(self):
        """Get tokens as a string for display"""
        return ' '.join(self.tokens)
    
    def get_tokens_as_array(self):
        """Get tokens as array representation"""
        return {i: token for i, token in enumerate(self.tokens)}
    
    def __repr__(self):
        return f"Tokens: {self.tokens}"


class TokenArray:
    """Represents the token array as shown in the task"""
    def __init__(self, input_string):
        self.tokenizer = Tokenizer()
        self.tokens = self.tokenizer.tokenize(input_string)
    
    def get_array(self):
        """Get array representation"""
        return {i: token for i, token in enumerate(self.tokens)}
    
    def print_array(self):
        """Print in the format shown in the task"""
        print("\nToken Array Representation:")
        for i, token in enumerate(self.tokens):
            print(f"{i}: ${token}$")
    
    def __repr__(self):
        return str(self.get_array())
