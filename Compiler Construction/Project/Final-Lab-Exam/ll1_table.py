from ll1_helper import LL1Helper

class LL1ParsingTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.helper = LL1Helper(grammar)
        self.table = {}  # {(non_terminal, terminal): production_index}
        self.build_table()
    
    def build_table(self):
        for nt in self.grammar.non_terminals:
            for terminal in self.grammar.terminals:
                self.table[(nt, terminal)] = None
        
        # Build the table
        for nt in self.grammar.non_terminals:
            for prod_idx, production in enumerate(self.grammar.productions[nt]):
                first_of_prod = self.helper.first_of_production(production)
                
                for terminal in first_of_prod:
                    if terminal != 'ε':
                        self.table[(nt, terminal)] = (nt, prod_idx, production)
                
                if 'ε' in first_of_prod:
                    for terminal in self.helper.get_follow_set(nt):
                        self.table[(nt, terminal)] = (nt, prod_idx, production)
    
    def get_production(self, non_terminal, terminal):
        return self.table.get((non_terminal, terminal), None)
    
    def print_table(self):
        terminals = sorted(self.grammar.terminals)
        non_terminals = sorted(self.grammar.non_terminals)
        
        # Print header
        print("\n" + "="*80)
        print("LL(1) PARSING TABLE")
        print("="*80)
        
        # Calculate column width
        col_width = 20
        
        # Print table header
        print(f"{'Non-Terminal':<15}", end="")
        for terminal in terminals:
            print(f"{terminal:<{col_width}}", end="")
        print()
        
        print("-" * (15 + len(terminals) * col_width))
        
        # Print table rows
        for nt in non_terminals:
            print(f"{nt:<15}", end="")
            for terminal in terminals:
                entry = self.table.get((nt, terminal), None)
                if entry is None:
                    print(f"{'':>{col_width}}", end="")
                else:
                    nt_rule, prod_idx, production = entry
                    prod_str = f"{nt_rule} → {' '.join(production)}"
                    print(f"{prod_str:<{col_width}}", end="")
            print()
        
        print("="*80 + "\n")
    
    def print_table_compact(self):
        terminals = sorted(self.grammar.terminals)
        non_terminals = sorted(self.grammar.non_terminals)
        
        print("\n" + "="*80)
        print("LL(1) PARSING TABLE")
        print("="*80)
        
        all_productions = self.grammar.get_all_productions_numbered()
        
        print("\nProductions:")
        for rule_num, nt, prod in all_productions:
            print(f"  {rule_num}: {nt} → {' '.join(prod)}")
        
        print("\nTable:")
        print(f"{'Non-Term':<10}", end="")
        for terminal in terminals:
            print(f"{terminal:<8}", end="")
        print()
        print("-" * (10 + len(terminals) * 8))
        
        for nt in non_terminals:
            print(f"{nt:<10}", end="")
            for terminal in terminals:
                entry = self.table.get((nt, terminal), None)
                if entry is None:
                    print(f"{'':>8}", end="")
                else:
                    _, prod_idx, _ = entry
                    prod_num = sum(len(self.grammar.productions[n]) 
                                 for n in sorted(self.grammar.productions.keys()) 
                                 if n < nt) + prod_idx
                    print(f"{prod_num:<8}", end="")
            print()
        
        print("="*80 + "\n")
