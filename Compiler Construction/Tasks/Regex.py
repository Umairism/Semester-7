import re


def check_match(pattern_name, pattern, word):
    if re.fullmatch(pattern, word):
        print(f"\n  [{pattern_name}] '{word}' is CORRECT   (pattern: {pattern})")
    else:
        print(f"\n  [{pattern_name}] '{word}' is INCORRECT (pattern: {pattern})")


def regix():
    word = input("Enter Word: ")
    regular = input("Enter Your RE for the expression: ")
    re.compile(regular)
    if re.fullmatch(regular, word):
        print("Word is correct")
        print("__________________")
    else:
        print("Word is incorrect")
        print("__________________")