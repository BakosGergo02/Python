#!/usr/bin/env python3

def main():

    with open("string1.py", "r", encoding="utf-8") as f, open("string1_clean.py","w", encoding="utf-8") as f2:
        for line in f:
            if not line.startswith("#"):
                f2.write(line)

if __name__ == "__main__":
    main()
