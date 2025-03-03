#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        print(a+b)

    else:
        print("Hiba! Adjon meg minimum 2 számot!")

    c = int(input("Adjon meg egy számot: "))
    d = int(input("Adjon meg egy másik számot: "))

    print(c+d)

if __name__ == "__main__":
    main()
