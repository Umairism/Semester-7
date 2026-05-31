class Grammar:
    def __init__(self):
        # Grammar rules
        self.productions = {
            'E': [
                ['a', 'w'],       # E → aw
                ['b']             # E → b
            ],
            'W': [
                ['b', 'W'],       # W → bW
                ['c', 'R']        # W → cR
            ],
            'R': [
                ['c'],            # R → c
                ['r', 'R']        # R → rR
            ]
        }
        
        # Start symbol
        self.start_symbol = 'E'
        
        # Terminals
        self.terminals = {'a', 'b', 'c', 'r', '$'}
        
        # Non-terminals
        self.non_terminals = {'E', 'W', 'R'}
    
    def get_production_number(self, non_terminal, production_index):
        rule_num = 0
        for nt in ['E', 'W', 'R']:
            if nt == non_terminal:
                return rule_num + production_index
            rule_num += len(self.productions[nt])
        return -1
    
    def get_all_productions_numbered(self):
        productions = []
        rule_num = 0
        for non_terminal in ['E', 'W', 'R']:
            for production in self.productions[non_terminal]:
                productions.append((rule_num, non_terminal, production))
                rule_num += 1
        return productions
    
    def __repr__(self):
        result = ""
        for nt in ['E', 'W', 'R']:
            for prod in self.productions[nt]:
                result += f"{nt} → {' '.join(prod)}\n"
        return result
