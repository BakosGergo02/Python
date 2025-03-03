#!/usr/bin/env python3

def xor(str1,str2):
    if (bool(str1) == False and bool(str2) == True) or (bool(str1) == True and bool(str2) == False):
        print("igaz a változókra az XOR művelet")

    else:
        print("Nem igaz a változókra az XOR művelet")

def main():

    str1 = "py"
    str2 = []

    

    xor(str1,str2)

if __name__ == "__main__":
    main()