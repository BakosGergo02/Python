#!/usr/bin/env python3

# A. donuts
# Bemenet: egy egész szám (a fánkok száma).
# Adjunk vissza egy sztringet a köv. formában: 'Fánkok száma: <count>',
# ahol <count> a bemenetként kapott érték.
# Viszont ha a fánkok száma 10 vagy több, akkor a tényleges szám helyett
# a 'sok' szót használjuk.
# Vagyis donuts(5) visszatérési értéke 'Fánkok száma: 5', míg
# donuts(23) visszatérési értéke 'Fánkok száma: sok'
def donuts(count):
    if (count >= 10):
        return print("fánkok száma: sok")
    else:
        return print("fánkok száma: {count}")

# B. both_ends
# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# mely az eredeti sztring első 2 és utolsó 2 karakteréből áll.
# Vagyis 'spring' esetén a visszatérési érték 'spng'.
# Ha az input sztring hossza 2-nél rövidebb, akkor egy üres
# sztringet adjunk vissza.
def both_ends(s):
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]

# C. fix_start
# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# melyben az első karakter összes előfordulása helyén egy '*'
# szerepel, kivéve a legelső pozíciót.
# Példa: 'babble' => 'ba**le'
# Feltételezhetjük, hogy a bemeneti sztring hossza legalább 1.
# Tipp: s.replace(stra, strb) egy olyan sztringet ad vissza,
# melyben az stra összes előfordulása ki van cserélve strb-re.
def fix_start(s):
    first = s[0]
    return first + s[1:].replace(first,"*")


# D. mix_up
# Adott két bemeneti sztring, a és b. Adjunk vissza egyetlen sztringet,
# melyben a és b konkatenálva van úgy, hogy köztük egyetlen szóköz szerepel.
# Ezen túl cseréljük fel a két sztring első két karakterét az eredményben.
# Példa:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Feltételezhetjük, hogy a bemeneti sztringek hossza legalább 2.
#def mix_up(a, b):
#   return f"{b[:2]+a[2:]}"

def egesz_szam(a):
    if str(a)[: -1] != 0:
        return str(a)[::-1]

def hello(name,color,obj):
    print("{0}! {1} a(z) {2}.".format(name.capitalize(),color,obj))
    print("{}! {} a(z) {}.".format(name.capitalize(),color,obj))
    print("{n}! {c} a(z) {o}.".format(n =name.capitalize(),c =color,o = obj))
    print("{0}! {1} a(z) {2}.".format(name.capitalize(),color,obj))

def main():
    #Geza! kek az eg.
    hello("geza", "kek", "eg")
    donuts(5)
    both_ends("string")
    print("Hello World")


if __name__ == "__main__":
    main()