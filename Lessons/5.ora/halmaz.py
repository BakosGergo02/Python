#!/usr/bin/env python3

def main():

    kosar = ["alma", "alma","banan", "narancs", "narancs", "alma"]

    gyumolcs = set(kosar)

    li = list(gyumolcs)

    li.sort()

    gyumolcs.add("Dinnye")

    gyumolcs.remove("banan")

    gyumolcs_ketto = set(["alma", "dinnye", "citrom"])

    print(gyumolcs.union(gyumolcs_ketto))
    print(gyumolcs.intersection(gyumolcs_ketto))
    print(gyumolcs.difference(gyumolcs_ketto))

    print(gyumolcs_ketto)
    print(gyumolcs)
    print(li)

if __name__ == "__main__":
    main()