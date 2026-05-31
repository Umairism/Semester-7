from grammar import Grammar
from ll1_helper import LL1Helper
from ll1_table import LL1ParsingTable
from tokenizer import Tokenizer, TokenArray
from ll1_parser import LL1Parser

def main():
    print("="*80)
    print("LL(1) PARSER")
    print("="*80)
    
    print("\n[Grammar]")
    grammar = Grammar()
    print(grammar)
    
    print("\n[FIRST and FOLLOW Sets]")
    helper = LL1Helper(grammar)
    helper.print_sets()
    
    print("\n[Parsing Table]")
    parsing_table = LL1ParsingTable(grammar)
    parsing_table.print_table_compact()
    
    print("\n[Tokenizing Input]")
    test_input = "n + n * n"
    print(f"Input: {test_input}")
    
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(test_input)
    
    token_array = TokenArray(test_input)
    token_array.print_array()
    
    print(f"\nTokens: {' '.join(tokens)}")
    
    print("\n[Parsing]")
    parser = LL1Parser(grammar, parsing_table)
    success, message = parser.parse(tokens)
    
    parser.print_parse_trace()
    parser.print_summary()
    
    print(f"\nResult: {message}")
    
    print("\n" + "="*80)
    print("More Tests")
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
                print(f"✓ ACCEPTED")
            else:
                print(f"✗ REJECTED")
            
            print("\nSteps:")
            for i, trace in enumerate(parser.parse_trace):
                if i % 2 == 0 or i == len(parser.parse_trace) - 1:  # Show every other step
                    print(f"  Step {trace['step']}: {trace['action']}")
        
        except Exception as e:
            print(f"✗ ERROR: {e}")


if __name__ == "__main__":
    main()
