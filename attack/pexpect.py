import sys, random
import time
import itertools
#The purpose of this part of the code is to generate a dictionary with a .txt file extension.
def main():
    words = "123456789"  # Elements used to form the dictionary.You can certainly do it like this: `'abcdefjABCDEFG-+*@?'`
    temp = itertools.permutations(words, 2)  # Generate permutations of length 2 using words
    password = open("dic.txt", "a")
    for i in temp:
        password.write("".join(i))  # Write to file
        password.write("\n")
    password.close()
    pass

if __name__ == "__main__":
    main()