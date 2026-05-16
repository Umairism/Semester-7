"""
Main LL(1) Parser Program
Demonstrates the complete LL(1) parsing process
"""

from grammar import Grammar
from ll1_helper import LL1Helper
from ll1_table import LL1ParsingTable
from tokenizer import Tokenizer, TokenArray
from ll1_parser import LL1Parser

def main():
    print("="*80)
    print("LL(1) PARSER IMPLEMENTATION")
    print("="*80)
    
    # Step 1: Define Grammar
    print("\n[STEP 1: GRAMMAR DEFINITION]")
    grammar = Grammar()
    print(grammar)
    
    # Step 2: Compute FIRST and FOLLOW sets
    print("\n[STEP 2: COMPUTE FIRST AND FOLLOW SETS]")
    helper = LL1Helper(grammar)
    helper.print_sets()
    
    # Step 3: Build LL(1) Parsing Table
    print("\n[STEP 3: BUILD LL(1) PARSING TABLE]")
    parsing_table = LL1ParsingTable(grammar)
    parsing_table.print_table_compact()
    
    # Step 4: Tokenize Input
    print("\n[STEP 4: TOKENIZE INPUT]")
    test_input = "n + n * n"
    print(f"Input: {test_input}")
    
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(test_input)
    
    token_array = TokenArray(test_input)
    token_array.print_array()
    
    print(f"\nTokenized: {' '.join(tokens)}")
    
    # Step 5: Parse using LL(1) Parser
    print("\n[STEP 5: PARSE INPUT]")
    parser = LL1Parser(grammar, parsing_table)
    success, message = parser.parse(tokens)
    
    parser.print_parse_trace()
    parser.print_summary()
    
    print(f"\nResult: {message}")
    
    # Test with more examples
    print("\n" + "="*80)
    print("ADDITIONAL TEST CASES")
    print("="*80)
    
    test_cases = [
        "n",
        "n + n",
        "n * n",
        "n + n * n",
        "(n)",
        "(n + n)",
        "(n + n) * n"
    ]
    
    for test_case in test_cases:
        print(f"\n{'─'*60}")
        print(f"Test: {test_case}")
        print('─'*60)
        
        try:
            tokens = tokenizer.tokenize(test_case)
            parser = LL1Parser(grammar, parsing_table)
            success, message = parser.parse(tokens)
            
            if success:
                print(f"✓ ACCEPTED - {message}")
            else:
                print(f"✗ REJECTED - {message}")
            
            # Print brief trace
            print("\nParsing steps:")
            for i, trace in enumerate(parser.parse_trace):
                if i % 2 == 0 or i == len(parser.parse_trace) - 1:  # Show every other step
                    print(f"  Step {trace['step']}: {trace['action']}")
        
        except Exception as e:
            print(f"✗ ERROR: {e}")
    
    print("\n" + "="*80)


if __name__ == "__main__":
    main()
