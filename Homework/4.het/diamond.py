#!/usr/bin/env python3

def diamond(n):
    if n % 2 != 0:
        for i in range(1, n, 2):
            print(" "*(n//2-i//2), "*"*i)
        for i in range(n, 0, -2):
            print(" "*(n//2-i//2), "*"*i)

    else:
        print("Páratlan számot adjon meg!")


def main():

    diamond(int(input("Adja meg a gyémánt magasságát: ")))

if __name__ == "__main__":
    main()
