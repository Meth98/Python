# Script that it says if a string is palindrome or not

import sys

if len(sys.argv) != 1:
    print("Warning!! You should not put any argument!", end="")
else:
    string = input("Type a string that you want reverse: ")
    index = len(string) - 1
    new_string = ""

    while index >= 0:
        new_string += string[index]
        index -= 1

    if string == new_string:
        print("The string '" + str(string) + "' is palindrome!", end="")
    else:
        print("The string '" + str(string) + "' isn't palindrome!", end="")