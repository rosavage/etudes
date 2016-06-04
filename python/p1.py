#!/usr/bin/python3

def greeting():
    str = input("What is your name?")
    output = "Hello, {}, nice to meet you!".format(str)
    print(output)


if __name__=="__main__":
    greeting()
