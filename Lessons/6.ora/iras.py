#!/usr/bin/env python3

def main():

    f = open("valami.txt", "r", encoding="utf-8")

    f.write("ELSO SOR\n")
    print("MASODIK SOR", file = f)

    f.close()

if __name__ == "__main__":
    main()