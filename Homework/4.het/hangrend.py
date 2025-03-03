#!/usr/bin/env python3

def hangrend(str1):

    mely = 'aáoóuú'
    magas = 'eéiíöőüű'

    melycount =0
    magascount = 0

    for s in str1:
        for m in mely:
            if m in s:
                melycount+=1
        for n in magas:
            if n in s:
                magascount +=1
        if melycount > 0 or magascount > 0:
            if melycount > 0 and magascount > 0:
                print("vegyes")
            if melycount > 0 and magascount == 0:
                print("mély")
            if magascount > 0 and melycount == 0:
                print("magas")
        else:
            print ("semmilyen")
        melycount = 0
        magascount = 0

def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély","Pfff"]


    hangrend(words)
if __name__ == "__main__":
    main()