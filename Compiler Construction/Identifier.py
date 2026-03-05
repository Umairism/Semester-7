from Regex import check_match


def identifier_grammar():
    print("\n...................Identifier Grammar...................")
    print("  <Ai>  => [a-zA-Z]")
    print("  <dat> => [0-9]")
    print("  <Identifier> => (<Ai>|-)(<Ai>|_|<dat>)*")
    print("  Resolved: [a-zA-Z\\-][a-zA-Z_0-9]*\n")

    Ai = r'[a-zA-Z]'
    dat = r'[0-9]'
    Identifier = rf'({Ai}|\-)({Ai}|_|{dat})*'  # [a-zA-Z\-][a-zA-Z_0-9]*

    word = input("Enter word to test against Identifier Grammar: ")
    check_match("<Identifier> = (<Ai>|-)(<Ai>|_|<dat>)*", Identifier, word)
