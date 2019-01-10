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

        for i in range(wysokosc-j):
            print(" ", end="")
        # endFor

        print("/", end="")

        for i in range(j*2):
            print(" ", end="")
        # enFor

        print("\\")
    # endFor

    for j in range(wysokosc):

        for i in range(j+1):
            print(" ", end="")
        # endFor

        print("\\", end="")

        for i in range(2*(wysokosc-j-1),0,-1):
            print(" ", end="")
        # enFor

        print("/")
    # endFor


# ----- pobieranie danych -----
def pobierzDane():
    return int(input("podaj x: "))


# ----- program głóny -----

romb(pobierzDane())
