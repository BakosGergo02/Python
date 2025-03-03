#!/usr/bin/env python3

def negyzetekosszege():
    a = 0
    for i in range(1,100+1):
        a += i**2
    return a

def osszegeknegyzete():
    a = 0
    for i in range(1,100+1):
        a += i
    return a**2

def main():

    res = osszegeknegyzete()- negyzetekosszege()
    print(res)

if __name__ == "__main__":
    main()