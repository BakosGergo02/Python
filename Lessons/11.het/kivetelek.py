
def main():
    try:
        file = open("unkown.txt", "r", encoding="utf-8")

    except IOError as e:
        print("error while opening file")
        print("error message: ", e)
        exit(5)
    except:
        print("error!")
        exit(100)
    finally:
        print("The program is Still runing...")
        file.close()

    #TEXT = file.read()

    #file.close()

if __name__ == '__main__':
    main()