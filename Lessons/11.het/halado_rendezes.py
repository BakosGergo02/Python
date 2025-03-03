
def sort_matrix(x):
    return x[1]

def sort_users(s):
    return int(s.split(":")[0])

def sort_s(s):
    return s[-1]

def main():


    data = [
        (1, 'Albany', 'NY', 162692),
        (121, 'Wyoming', 'NY', 8722),
        (3, 'Allegany', 'NY', 11986),
        (123, 'Yates', 'NY', 5094)
    ]

    print(sorted(data, key=sort_s))

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

    print(sorted(users, key=sort_users))

    matrix = [ [2, 6], [1, 3], [5, 4] ]

    print(sorted(matrix, key=sort_matrix))



if __name__ == '__main__':
    main()
