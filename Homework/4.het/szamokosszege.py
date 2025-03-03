#!/usr/bin/env python3

def main():

    a = list(range(1,100+1))

    digits=[]
    for i in str(a):
       if i.isdigit():
        digits.append(int(i))
    print(sum(digits))

if __name__ == "__main__":
    main()