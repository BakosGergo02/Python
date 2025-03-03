#!/usr/bin/env python3

#kiss solid yagni -> i

import sys

def kozos_karakterek(argumentumok):
    elso = argumentumok[0]
    argumentumok.pop(0)
    eredmeny = []

    for karakter in elso:
        benne_van = True
        for sztring in argumentumok:
            if karakter not in sztring:
                benne_van = False
        if benne_van:
            eredmeny.append(karakter)

    return "".join(eredmeny)

def main():
    if len(sys.argv) -1 < 2:
        print("Hiba! MInimum 2 darab parancssori argomentumot meg kell adni!", file=sys.stderr)
        exit(1)

    sys.argv.pop(0)
    eredmeny = kozos_karakterek(sys.argv)
    print(eredmeny)




    #sor intedexek betu-pontok txt file
    #1. betu-pontok
    #2. A-1
    #3. B-10

    #szótárral 0 végjelig legtobb pontot erő szó
if __name__ == "__main__":
    main()