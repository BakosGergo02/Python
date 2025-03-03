#!/usr/bin/env python3

def main():

    #1.feladat
    lista = ['auto','villamos','metro']

    nagy = [jarmu.upper() + '!' for jarmu in lista]
    print(nagy)
    #2.feladat
    nevek = ['aladar', 'bela', 'cecil']
    nevek2= [nev.capitalize for nev in nevek]
    print(nevek2)

    #3.feladat
    n = [0 for i in range(1,10+1)]
    print(n)
    #4.feladat
    a = [i for i in range(1,10+1)]
    b = [i*2 for i in a]
    print(b)
    #13.feladat

    betuk = [chr(kod) for kod in range(65, 90+1)]
    a = "".join(betuk)
    print(a)


if __name__ == "__main__":

    main()