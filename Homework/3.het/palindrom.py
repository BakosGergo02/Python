#!/usr/bin/env python3

def Palindrome1(s):
    return s[::-1]

def Palindrome2(s):
    s = "".join(reversed(s))

    return s

def main():

    s = "görög"

    if s == Palindrome2(s):
        print("Palindróm")
    else:
        print("nem palindróm")

    if s == Palindrome1(s):
        print("Palindróm")
    else:
        print("nem palindróm")





if __name__ == "__main__":
    main()