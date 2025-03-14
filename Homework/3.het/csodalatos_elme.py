#!/usr/bin/env python3

TEXT = """
3Z 4Z UZ3N37 4Z7 4 C3L7 5Z0LG4LJ4, H0GY B3B1Z0NY1754
M1LY3N C50D4L4705 D0LG0KR4 K3P35 4Z 3LM3.
3LK3P35Z70 D0LG0KR4! N3H3Z V0L7 3L05Z0R 3L0LV45N0D
3Z7, D3 M1R3 1D33R5Z 3HH3Z 4 50RH0Z, 4Z 3LM3D
4U70M471KU54N 3L 7UDJ4 0LV45N1.
4N3LKUL H0GY G0ND0LK0DN0D K3LL3N3 R4J74.
L3GY BU5ZK3! C54K K3V35 3MB3R K3P35 3L0LV45N1 3Z7.
H4 7375Z377, 05ZD M3G M450KK4L 15!
"""

def olvashato(str):

    cserek = [('4','A'),('3', 'E'),('5','S'),('7','T'),('0','O'),('1','I')]
    for (a,b) in cserek:
        str = str.replace(a,b)

    return str
def main():
    #print(TEXT)

    print(olvashato(TEXT))

##############################################################################

if __name__ == "__main__":
    main()
