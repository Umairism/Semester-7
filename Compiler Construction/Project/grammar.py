"""
Grammar Definition for LL(1) Parser
Expression Grammar (Left Recursion Eliminated):
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → (E) | n
"""

class Grammar:
    def __init__(self):
        # Production rules: {non_terminal: [list of productions]}
        # Each production is a list of symbols (terminals and non-terminals)
        self.productions = {
            'E': [
                ['T', "E'"],      # E → T E'
            ],
            "E'": [
                ['+', 'T', "E'"], # E' → + T E'
                ['ε']              # E' → ε (epsilon)
            ],
            'T': [
                ['F', "T'"],      # T → F T'
            ],
            "T'": [
                ['*', 'F', "T'"], # T' → * F T'
                ['ε']              # T' → ε (epsilon)
            ],
            'F': [
                ['(', 'E', ')'],   # F → (E)
                ['n']              # F → n
            ]
        }
        
        # Start symbol
        self.start_symbol = 'E'
        
        # Terminals
        self.terminals = {'+', '*', '(', ')', 'n', '$', 'ε'}
        
        # Non-terminals
        self.non_terminals = {'E', "E'", 'T', "T'", 'F'}
    
    def get_production_number(self, non_terminal, production_index):
        """Get production number for a given non-terminal and production"""
        rule_num = 0
        for nt in ['E', "E'", 'T', "T'", 'F']:
            if nt == non_terminal:
                return rule_num + production_index
            rule_num += len(self.productions[nt])
        return -1
    
    def get_all_productions_numbered(self):
        """Get all productions with their numbers"""
        productions = []
        rule_num = 0
        for non_terminal in ['E', "E'", 'T', "T'", 'F']:
            for production in self.productions[non_terminal]:
                productions.append((rule_num, non_terminal, production))
                rule_num += 1
        return productions
    
    def __repr__(self):
        result = "Grammar Productions (Left Recursion Eliminated):\n"
        for nt in ['E', "E'", 'T', "T'", 'F']:
            for i, prod in enumerate(self.productions[nt]):
                result += f"{nt} → {' '.join(prod)}\n"
        return result
