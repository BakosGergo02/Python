#!/usr/bin/env python3

def main():

    d = {}
    d["a"] = "alfa"
    d["b"] = "beta"
    d["g"] = "gamma"

    for k in sorted(d.keys()):
        print(f"{k} => {d[k]}")


    print(d)

if __name__ == "__main__":
    main()