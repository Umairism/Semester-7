from Regex import regix
from Grammer import grammar1,grammar2
from Identifier import identifier_grammar
from Number import number_grammar


def main():
    while True:
        print("\n...................Regex Grammar Checker...................")
        print("1. Basic Regex Check")
        print("2. Grammar 1:  X => (AB)*|D")
        print("3. Grammar 2:  X => MY|R")
        print("4. Identifier: <Identifier> => (<Ai>|-)(<Ai>|_|<dat>)*")
        print("5. Number:     <Num> => (+|-|E)(<int>|<float>)")
        print("6. Exit")
        choice = input("Select option (1-6): ")

        if choice == '1':
            regix()
        elif choice == '2':
            grammar1()
        elif choice == '3':
            grammar2()
        elif choice == '4':
            identifier_grammar()
        elif choice == '5':
            number_grammar()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()