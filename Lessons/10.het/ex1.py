from py_utily.py import is_prime

def main():
    for n in range(100):
        if is_prime(n):
            print(n)


if __name__ == "__main__":
    main()
