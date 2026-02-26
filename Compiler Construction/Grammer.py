from Regex import check_match

def grammar1():

    print("\n...................Grammar 1...................")
    print("  A => a+")
    print("  B => b*")
    print("  D => d*")
    print("  X => (AB)*|D")
    print("  Resolved: X = (a+b*)*|d*\n")

    A = r'a+'
    B = r'b*'
    D = r'd*'
    X = rf'({A}{B})*|{D}'  # (a+b*)*|d*

    word = input("Enter word to test against Grammar 1: ")
    check_match("X = (AB)*|D", X, word)


def grammar2():
    print("\n ...................Grammar 2...................")
    print("  R => (r*ar)*")
    print("  M => (m*)*")
    print("  Y => Ry*")
    print("  X => MY|R")
    print("  Resolved: X = (m*)*(r*ar)*y*|(r*ar)*\n")

    R = r'(r*ar)*'
    M = r'(m*)*'
    Y = rf'{R}y*'           # (r*ar)*y*
    X = rf'{M}{Y}|{R}'      # (m*)*(r*ar)*y*|(r*ar)*

    word = input("Enter word to test against Grammar 2: ")
    check_match("X = MY|R", X, word)
