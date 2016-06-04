#!/usr/bin/python3


def quote():
    quote=input("What is the quote? ")
    person = input("Who said it? ")
    print("{} says, \"{}\" ".format(person,quote))


if __name__=="__main__":
    quote()
