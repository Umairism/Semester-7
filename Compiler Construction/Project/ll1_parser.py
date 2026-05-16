"""
LL(1) Stack-based Parser Implementation
"""

from grammar import Grammar
from ll1_table import LL1ParsingTable
from tokenizer import Tokenizer

class LL1Parser:
    def __init__(self, grammar, parsing_table):
        self.grammar = grammar
        self.parsing_table = parsing_table
        self.stack = []
        self.input_tokens = []
        self.input_position = 0
        self.parse_trace = []
        self.parse_tree = None
    
    def parse(self, input_tokens):
        """
        Parse the input tokens using LL(1) parsing
        input_tokens: list of tokens including $
        
        Returns:
            - (True, message): If parsing succeeds
            - (False, error_message): If parsing fails
        """
        self.stack = []
        self.input_tokens = input_tokens
        self.input_position = 0
        self.parse_trace = []
        
        # Initialize stack with $ and start symbol
        self.stack.append('$')
        self.stack.append(self.grammar.start_symbol)
        
        step = 0
        max_steps = 1000  # Prevent infinite loops
        
        while step < max_steps:
            step += 1
            
            # Get top of stack and current input token
            top = self.stack[-1] if self.stack else None
            current_token = self.get_current_token()
            
            # Trace
            trace_entry = {
                'step': step,
                'stack': self.stack[:],
                'input_pos': self.input_position,
                'remaining_input': ' '.join(self.input_tokens[self.input_position:]),
                'top': top,
                'current_token': current_token,
                'action': ''
            }
            
            # Check for success (stack has only $, input at $)
            if top == '$' and current_token == '$':
                trace_entry['action'] = 'ACCEPT'
                self.parse_trace.append(trace_entry)
                return True, "Parsing successful!"
            
            # Check for error
            if top is None or current_token is None:
                trace_entry['action'] = f'ERROR: Invalid state'
                self.parse_trace.append(trace_entry)
                return False, "Parsing failed: Stack or input error"
            
            # Terminal on top of stack
            if top in self.grammar.terminals and top != 'ε':
                if top == current_token:
                    # Match: pop from stack and advance input
                    self.stack.pop()
                    self.input_position += 1
                    trace_entry['action'] = f'MATCH {top}'
                else:
                    # Error: expected top but got current_token
                    trace_entry['action'] = f'ERROR: Expected {top}, got {current_token}'
                    self.parse_trace.append(trace_entry)
                    return False, f"Expected {top}, got {current_token}"
            
            # Epsilon (non-terminal) on top of stack - just pop it
            elif top == 'ε':
                self.stack.pop()
                trace_entry['action'] = 'POP ε'
            
            # Non-terminal on top of stack
            elif top in self.grammar.non_terminals:
                # Look up in parsing table
                production = self.parsing_table.get_production(top, current_token)
                
                if production is None:
                    trace_entry['action'] = f'ERROR: No entry in M[{top},{current_token}]'
                    self.parse_trace.append(trace_entry)
                    return False, f"No production for M[{top},{current_token}]"
                
                # Apply production
                nt, prod_idx, prod_symbols = production
                
                # Pop non-terminal
                self.stack.pop()
                
                # Push production symbols in reverse order
                # Skip epsilon
                for symbol in reversed(prod_symbols):
                    if symbol != 'ε':
                        self.stack.append(symbol)
                
                trace_entry['action'] = f'EXPAND: {nt} → {" ".join(prod_symbols)}'
            
            else:
                trace_entry['action'] = f'ERROR: Unknown symbol {top}'
                self.parse_trace.append(trace_entry)
                return False, f"Unknown symbol: {top}"
            
            self.parse_trace.append(trace_entry)
        
        return False, "Parsing failed: Max steps exceeded"
    
    def get_current_token(self):
        """Get current token from input"""
        if self.input_position < len(self.input_tokens):
            return self.input_tokens[self.input_position]
        return None
    
    def print_parse_trace(self):
        """Print the parsing trace"""
        print("\n" + "="*140)
        print("PARSING TRACE")
        print("="*140)
        print(f"{'Step':<6} {'Stack':<40} {'Input':<35} {'Action':<50}")
        print("-"*140)
        
        for trace in self.parse_trace:
            stack_str = ' '.join(trace['stack'][-7:]) if trace['stack'] else 'EMPTY'
            if len(stack_str) > 38:
                stack_str = '...' + stack_str[-35:]
            
            input_str = trace['remaining_input'][:33]
            action_str = trace['action'][:48]
            
            print(f"{trace['step']:<6} {stack_str:<40} {input_str:<35} {action_str:<50}")
        
        print("="*140 + "\n")
    
    def print_summary(self):
        """Print parsing summary"""
        if not self.parse_trace:
            print("No parsing trace available")
            return
        
        last_trace = self.parse_trace[-1]
        print(f"\nTotal steps: {len(self.parse_trace)}")
        print(f"Final action: {last_trace['action']}")
        
        if 'ACCEPT' in last_trace['action']:
            print("Status: ✓ ACCEPTED")
        elif 'ERROR' in last_trace['action']:
            print("Status: ✗ REJECTED")
        else:
            print("Status: UNKNOWN")
