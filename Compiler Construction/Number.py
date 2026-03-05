from Regex import check_match


def number_grammar():
    print("\n...................Number Grammar...................")
    print("  <int>   => [0-9]+")
    print("  <float> => [0-9]+\\.[0-9]+")
    print("  <Num>   => (+|-|E)(<int>|<float>)")
    print("  Note: E = epsilon (empty string)")
    print("  Resolved: [+\\-]?([0-9]+|[0-9]+\\.[0-9]+)\n")

    sign = r'[+\-]?'          # (+|-|epsilon)
    integer = r'[0-9]+'       # <int>
    floating = r'[0-9]+\.[0-9]+'  # <float>
    Num = rf'{sign}({integer}|{floating})'  # [+\-]?([0-9]+|[0-9]+\.[0-9]+)

    word = input("Enter word to test against Number Grammar: ")
    check_match("<Num> = (+|-|E)(<int>|<float>)", Num, word)
