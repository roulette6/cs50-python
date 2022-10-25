def main():
    mass = input("m: ")
    E = energy(mass)
    print(E)


def energy(mass):
    mass = int(mass)
    c = int(300000000)
    return mass * pow(c, 2)


main()