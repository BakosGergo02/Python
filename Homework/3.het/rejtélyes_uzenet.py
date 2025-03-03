#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""
def ugras(text):
    for words in TEXT:
        for c in words:
            a = ord(c)
            b = ord(c)+2
            c.replace(chr(a), chr(b))
    return text

def ugrastest(TEXT):
    value = 2

    res = []
    for line in TEXT:
        line = line.strip()
        res_chars = []
        for char in line:
            i = ord(char)
            i += value
            res_char = chr(i)

            res_chars.append(res_char)
        res_strings = ''.join(res_chars)
        res.append(res_strings)


    return res

def main():

    #print(ugras(TEXT))

    a = ugrastest(TEXT)
    b = ''.join(a)
    print(b)

if __name__ == "__main__":
    main()