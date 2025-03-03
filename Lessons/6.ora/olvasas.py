#!/usr/bin/env python3

def main():

    f = open("valami.txt", "r", encoding="utf-8")

   #3.megoldás
    TEXT = f.read()#.splitlines()
    print(TEXT)

   #2. megoldás
    #lines = f.readlines()
    #print(lines)

    #1.megoldás
    #for line in f:
       # print(line, end="")
        #line = line.strip("\n")
        #print(line)

    f.close()

if __name__ == "__main__":
    main()