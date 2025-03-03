#!/usr/bin/env python3

def main():

    a = str(2**256)

    count = 0
    for i in a:
        count+=1

    print(count)

if __name__ == "__main__":
    main()