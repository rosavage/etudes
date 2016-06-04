#!/usr/bin/python3

"""Character Counter"""

def charcount():
    str = input("What is the input string? ")
    length = len(str)
    print("{} has {} characters.".format(str,length))


if __name__=="__main__":
    charcount()

