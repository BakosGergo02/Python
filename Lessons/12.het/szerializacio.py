
from pprint import pprint
import json

def main():
    file = open("Person.json", "r", encoding="utf-8")
    d = json.load(file)

    file.close()

    print(type(d))

    pprint(d, indent=8)


    post = """{
        "first_name": "asd",
        "course": "Scripting languages",
    }"""
    #d_ketto = json.loads(post)

    #pprint(d_ketto)
    f_ketto = open("AnotherPerson.json", "w", encoding="utf-8")

    json.dump(d, f_ketto)


if __name__ == '__main__':
    main()
