class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.position = 0
    
    def tokenize(self, input_string):
        self.tokens = []
        self.position = 0
        
        input_string = input_string.replace(' ', '')
        
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
        
        self.tokens.append('$')
        
        return self.tokens
    
    def get_token(self, index):
        if index < len(self.tokens):
            return self.tokens[index]
        return '$'
    
    def get_tokens_as_string(self):
        return ' '.join(self.tokens)
    
    def get_tokens_as_array(self):
        return {i: token for i, token in enumerate(self.tokens)}
    
    def __repr__(self):
        return f"Tokens: {self.tokens}"


class TokenArray:
    def __init__(self, input_string):
        self.tokenizer = Tokenizer()
        self.tokens = self.tokenizer.tokenize(input_string)
    
    def get_array(self):
        return {i: token for i, token in enumerate(self.tokens)}
    
    def print_array(self):
        print("\nToken Array:")
        for i, token in enumerate(self.tokens):
            print(f"{i}: ${token}$")
    
    def __repr__(self):
        return str(self.get_array())
