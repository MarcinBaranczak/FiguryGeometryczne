# ----- pobieranie danych -----
def pobierzDane(info):
    return int(input(info))


# ----- rysuje kwadrat o zadanym boku -----
def kwadrat(bok):
    for i in range(bok):
        print("*", end="")
    # endFor

    for i in range(bok - 2):
        print("\n*", end="")

        for i in range(1, bok - 1):
            print(" ", end="")
        # endFor

        print("*")
    # endFor

    for i in range(bok):
        print("*", end="")
    # endFor


# ----- rysuje romb o zadanej wysokości -----
def romb(wysokosc):
    for j in range(wysokosc):

        for i in range(wysokosc - j):
            print(" ", end="")
        # endFor

        print("/", end="")

        for i in range(j * 2):
            print(" ", end="")
        # enFor

        print("\\")
    # endFor

    for j in range(wysokosc):

        for i in range(j + 1):
            print(" ", end="")
        # endFor

        print("\\", end="")

        for i in range(2 * (wysokosc - j - 1), 0, -1):
            print(" ", end="")
        # enFor

        print("/")
    # endFor


# ----- rysuje trójkąt prostokątny, równoramienny o zadanym boku -----
def trojkat(bok):
    print("*")

    for i in range(bok-2):
        print("*", end="")

        for j in range(i):
            print(" ", end="")
        # endFor

        print("*")
    # endFor

    for i in range (bok):
        print("*", end="")
    # endFor


# ----- menu -----
def menu():
    print("Wybierz figure: ")
    print("1: Kwadrat")
    print("2: Trojkat")
    print("3: Romb")

    wybor = pobierzDane("Twoj wybor: ")
    bok = pobierzDane("Podaj wielkosc boku: ")

    if wybor == 1:
        kwadrat(bok)
    if wybor == 2:
        trojkat(bok)
    if wybor == 3:
        romb(bok)


# ----- program głóny -----
menu()
