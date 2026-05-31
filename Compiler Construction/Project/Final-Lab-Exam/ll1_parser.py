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
        self.stack = []
        self.input_tokens = input_tokens
        self.input_position = 0
        self.parse_trace = []
        
        self.stack.append('$')
        self.stack.append(self.grammar.start_symbol)
        
        step = 0
        max_steps = 1000
        
        while step < max_steps:
            step += 1
            
            top = self.stack[-1] if self.stack else None
            current_token = self.get_current_token()
            
            trace_entry = {
                'step': step,
                'stack': self.stack[:],
                'input_pos': self.input_position,
                'remaining_input': ' '.join(self.input_tokens[self.input_position:]),
                'top': top,
                'current_token': current_token,
                'action': ''
            }
            
            if top == '$' and current_token == '$':
                trace_entry['action'] = 'ACCEPT'
                self.parse_trace.append(trace_entry)
                return True, "Parsing successful!"
            
            if top is None or current_token is None:
                trace_entry['action'] = f'ERROR: Invalid state'
                self.parse_trace.append(trace_entry)
                return False, "Parsing failed: Stack or input error"
            
            if top in self.grammar.terminals and top != 'ε':
                if top == current_token:
                    self.stack.pop()
                    self.input_position += 1
                    trace_entry['action'] = f'MATCH {top}'
                else:
                    trace_entry['action'] = f'ERROR: Expected {top}, got {current_token}'
                    self.parse_trace.append(trace_entry)
                    return False, f"Expected {top}, got {current_token}"
            
            elif top == 'ε':
                self.stack.pop()
                trace_entry['action'] = 'POP ε'
            
            elif top in self.grammar.non_terminals:
                production = self.parsing_table.get_production(top, current_token)
                
                if production is None:
                    trace_entry['action'] = f'ERROR: No entry in M[{top},{current_token}]'
                    self.parse_trace.append(trace_entry)
                    return False, f"No production for M[{top},{current_token}]"
                
                nt, prod_idx, prod_symbols = production
                
                self.stack.pop()
                
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
        if self.input_position < len(self.input_tokens):
            return self.input_tokens[self.input_position]
        return None
    
    def print_parse_trace(self):
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
