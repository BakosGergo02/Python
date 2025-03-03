# mycat.py

import sys


def cat(fname):
    try:
        f = open(fname, 'r')
        text = f.read()
        print('---', fname)
        print(text)
        f.close()
    except IOError as e:
        print(f"Error while running the {fname}  file! Error message: {e}", file=sys.stderr)

#####

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        cat(arg)