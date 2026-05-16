"""
FIRST and FOLLOW Set Computation for LL(1) Parser
"""

class LL1Helper:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first_sets = {}
        self.follow_sets = {}
        self.compute_first_sets()
        self.compute_follow_sets()
    
    def compute_first_sets(self):
        """Compute FIRST sets for all non-terminals"""
        # Initialize FIRST sets
        for nt in self.grammar.non_terminals:
            self.first_sets[nt] = set()
        
        # Base case: if production is epsilon, add epsilon to FIRST
        for nt in self.grammar.non_terminals:
            for production in self.grammar.productions[nt]:
                if production == ['ε']:
                    self.first_sets[nt].add('ε')
        
        # Iteratively compute FIRST sets until no changes
        changed = True
        while changed:
            changed = False
            for nt in self.grammar.non_terminals:
                old_size = len(self.first_sets[nt])
                
                for production in self.grammar.productions[nt]:
                    if production == ['ε']:
                        continue
                    
                    # Add FIRST of the production
                    first_of_prod = self.first_of_production(production)
                    self.first_sets[nt].update(first_of_prod)
                
                if len(self.first_sets[nt]) > old_size:
                    changed = True
    
    def first_of_production(self, production):
        """Compute FIRST set of a production (list of symbols)"""
        first_set = set()
        all_can_derive_epsilon = True
        
        for symbol in production:
            if symbol == 'ε':
                # Epsilon production handled separately
                continue
            elif symbol in self.grammar.terminals:
                # Terminal: add it and stop
                first_set.add(symbol)
                all_can_derive_epsilon = False
                break
            else:
                # Non-terminal: add its FIRST except epsilon
                first_set.update(self.first_sets.get(symbol, set()) - {'ε'})
                # If this symbol cannot produce epsilon, stop
                if 'ε' not in self.first_sets.get(symbol, set()):
                    all_can_derive_epsilon = False
                    break
        
        # If all symbols can derive epsilon, add epsilon to FIRST
        if all_can_derive_epsilon:
            first_set.add('ε')
        
        return first_set
    
    def compute_follow_sets(self):
        """Compute FOLLOW sets for all non-terminals"""
        # Initialize FOLLOW sets
        for nt in self.grammar.non_terminals:
            self.follow_sets[nt] = set()
        
        # Add $ to FOLLOW(start symbol)
        self.follow_sets[self.grammar.start_symbol].add('$')
        
        # Iteratively compute FOLLOW sets
        changed = True
        while changed:
            changed = False
            
            for nt in self.grammar.non_terminals:
                for production in self.grammar.productions[nt]:
                    for i, symbol in enumerate(production):
                        if symbol in self.grammar.non_terminals:
                            old_size = len(self.follow_sets[symbol])
                            
                            # Add FIRST of symbols after this symbol
                            rest = production[i + 1:]
                            first_of_rest = set()
                            
                            if not rest:
                                # Nothing after, add FOLLOW(nt)
                                first_of_rest.update(self.follow_sets[nt])
                            else:
                                all_nullable = True
                                for rest_symbol in rest:
                                    if rest_symbol == 'ε':
                                        continue
                                    elif rest_symbol in self.grammar.terminals:
                                        first_of_rest.add(rest_symbol)
                                        all_nullable = False
                                        break
                                    else:
                                        first_of_rest.update(
                                            self.first_sets.get(rest_symbol, set()) - {'ε'}
                                        )
                                        if 'ε' not in self.first_sets.get(rest_symbol, set()):
                                            all_nullable = False
                                            break
                                
                                if all_nullable:
                                    first_of_rest.update(self.follow_sets[nt])
                            
                            self.follow_sets[symbol].update(first_of_rest - {'ε'})
                            
                            if len(self.follow_sets[symbol]) > old_size:
                                changed = True
    
    def get_first_set(self, symbol):
        """Get FIRST set of a symbol"""
        if symbol in self.grammar.terminals:
            return {symbol}
        return self.first_sets.get(symbol, set())
    
    def get_follow_set(self, symbol):
        """Get FOLLOW set of a symbol"""
        return self.follow_sets.get(symbol, set())
    
    def print_sets(self):
        """Print all FIRST and FOLLOW sets"""
        print("FIRST Sets:")
        for nt in sorted(self.first_sets.keys()):
            print(f"  FIRST({nt}) = {sorted(self.first_sets[nt])}")
        
        print("\nFOLLOW Sets:")
        for nt in sorted(self.follow_sets.keys()):
            print(f"  FOLLOW({nt}) = {sorted(self.follow_sets[nt])}")
