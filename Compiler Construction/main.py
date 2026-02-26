from Regex import regix
from Grammer import grammar1,grammar2


def main():
    while True:
        print("\n...................Regex Grammar Checker...................")
        print("1. Basic Regex Check")
        print("2. Grammar 1:  X => (AB)*|D")
        print("3. Grammar 2:  X => MY|R")
        print("4. Exit")
        choice = input("Select option (1-4): ")

        if choice == '1':
            regix()
        elif choice == '2':
            grammar1()
        elif choice == '3':
            grammar2()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()