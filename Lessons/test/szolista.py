#!/usr/bin/env python3

import random

def main():
    szavak = input("Kérem adja meg legfeljebb négy szót, vesszővel és szóközzel elválasztva: ").split(", ")

    if szavak and len(szavak) <= 4:
        legrovidebb_szavak = [szo for szo in szavak if len(szo) == min(map(len, szavak))]
        print("A legrövidebb szó(k):", legrovidebb_szavak)

        leghosszabb_szo = max(szavak, key=len)
        leghosszabb_szo_atalakitva = leghosszabb_szo[0] + leghosszabb_szo[1:-1][::-1] + leghosszabb_szo[-1]
        print("Az egyik leghosszabb szó átalakítva:", leghosszabb_szo_atalakitva)

        ismetlodik = len(szavak) != len(set(szavak))
        if ismetlodik:
            print("Van olyan szó, ami többször szerepel a listában.")
        else:
            print("Nincs olyan szó, ami többször szerepel a listában.")

        veletlen_szo = random.choice(szavak)
        veletlen_szo_betuk = list(veletlen_szo)
        random.shuffle(veletlen_szo_betuk)
        veletlen_szo_veletlen_sorrendben = "".join(veletlen_szo_betuk)
        print("Véletlenszerűen kiválasztott szó betűi véletlen sorrendben:", veletlen_szo_veletlen_sorrendben)
    else:
        print("Nem adott meg szavakat vagy több mint négy szót adott meg.")

if __name__ == "__main__":
    main()
