#!/usr/bin/env python3

def szorzat(a):
    res = 1
    for i in a:
        res *= i
    return res

def main():

    #a = [1,2,3,4,5]

    #a.append('a')

    #a.pop()

    #del a[0]

    #a.index()

    #a.sort()

    #sorted(a)

    print(sum(range(100)))

    a = [1,2,3,4,5]

    print(szorzat(a))

if __name__ == "__main__":
    main()
