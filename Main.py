from MyModule import *

onAutoriseeritud=False

kasutaja_indeks=None

Loe_failist("Accounts.txt")

while True:
    print()
    print(f"{BLUE}===== MENÜÜ ====={RESET}")
    print()
    print("Sisestage 0-6")
    print()
    print("Regisreerimine - 1 ")
    if onAutoriseeritud:
        print("Nime muutmine - 2 ")
        print("Parooli muutmine - 3 ")
        print("Unustatud parooli taastamine - 4 ")
        print()
        print("Välja logimine - 5 ")
        print("Minu andmed - 6 ")
        print()
    else:
        print("Sisse logimine - 5 ")

    print("Salvesta ja välja - 0 ")


    try:
        print()
        valik=int(input("Valik: "))

        if onAutoriseeritud:
            if valik < 0 or valik > 6:
                print()
                print(f"{RED}Viga: Vale number{RESET}")

            elif valik == 2:
                Nime_muutmine(loginid[kasutaja_indeks])

            elif valik == 3:
                Parooli_muutmine(paroolid[kasutaja_indeks])

            elif valik == 4:
                Parooli_taastamine(postid[kasutaja_indeks], paroolid[kasutaja_indeks])

            elif valik == 6:
                print()
                print(f"{BLUE}===== MINU ANDMED ====={RESET}")
                print()
                print(f"Nimi: '{loginid[kasutaja_indeks]}'")
                print(f"Post: '{postid[kasutaja_indeks]}'")
                print(f"Parool: {'*' * len(paroolid[kasutaja_indeks])}")
                print()
                input("'Enter' jätkamiseks")


        else:
            if valik not in [1, 5, 0]:
                print()
                print(f"{RED}Viga: Vale number{RESET}")

        if valik == 0:
            Salvesta()
            break

        elif valik == 1:
            Registreerimine()

        elif valik == 5:
            if onAutoriseeritud == False:
                kasutaja_indeks = Sisse_logimine()
                onAutoriseeritud = True
            else:
                onAutoriseeritud = False
                kasutaja_indeks = None

                print()
                print(f"{GREEN}Olete välja logitud{RESET}")
                input("'Enter' jätkamiseks")


    except ValueError:
        print()
        print(f"{RED}Viga: Sisestage number{RESET}")

exit(0)