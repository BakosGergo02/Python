#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0

# http://code.google.com/edu/languages/google-python-class/

# Szathmáry László (jabba.laci@gmail.com)

# Írjuk meg az alábbi függvények törzsét. A main() fv.
# paraméterekkel. Ha egy fv.-t helyesen írtunk meg, akkor
# A fv.-eknek vmilyen értéket kell visszaadniuk, ezt a 'return'


# Bemenet: egy egész szám (a fánkok száma).
# ahol <count> a bemenetként kapott érték.
# a 'sok' szót használjuk.
# donuts(23) visszatérési értéke 'Fánkok száma: sok'
def donuts(count):
    # TODO...
    return


# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# Vagyis 'spring' esetén a visszatérési érték 'spng'.
# sztringet adjunk vissza.
def both_ends(s):
    # TODO...
    return


# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# szerepel, kivéve a legelső pozíciót.
# Feltételezhetjük, hogy a bemeneti sztring hossza legalább 1.
# melyben az stra összes előfordulása ki van cserélve strb-re.
def fix_start(s):
    # TODO...
    return


# Adott két bemeneti sztring, a és b. Adjunk vissza egyetlen sztringet,
# Ezen túl cseréljük fel a két sztring első két karakterét az eredményben.
#   'mix', 'pod' -> 'pox mid'
# Feltételezhetjük, hogy a bemeneti sztringek hossza legalább 2.
def mix_up(a, b):
    # TODO...
    return


# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
def main():
    print('donuts')
    # Minden egyes sor meghívja a donuts() fv.-t s összehasonlítja a visszaadott
    # értéket a várt eredménnyel.
    test(donuts(4), 'Fánkok száma: 4')
    test(donuts(9), 'Fánkok száma: 9')
    test(donuts(10), 'Fánkok száma: sok')
    test(donuts(99), 'Fánkok száma: sok')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

#############################################################################

if __name__ == '__main__':
    main()
