#!/usr/bin/env python3

def main():

    with open("valami.txt", "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()