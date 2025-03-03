
def sort_s(s):
    return s[-1]



def main():
    words = ["xd", "yz" ," wa", "ba"]
    print(sorted(words, key=sort_s))

if __name__ == '__main__':
    main()