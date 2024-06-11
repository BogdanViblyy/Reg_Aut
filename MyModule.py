import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

loginid = []
paroolid = []
postid = []

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


def Salvesta():
    with open('Accounts.txt', 'w') as file:
        for login, parool, email in zip(loginid, paroolid, postid):
            file.write(f"{login} {parool} {email}\n")


def Saada_email(pealkiri, kiri, kasutaja_post, saatja_post, saatja_posti_parool):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = saatja_post
    msg['To'] = kasutaja_post
    msg['Subject'] = pealkiri

    msg.attach(MIMEText(kiri, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(saatja_post, saatja_posti_parool)

        server.send_message(msg)
        print()
        print(f"Teie '{kasutaja_post}' aadressile saadeti meil taastekoodiga")
        vastus = True
    except Exception as e:
        print()
        print(f"{RED}Saatmise viga: {e}{RESET}")
        vastus = False
    finally:
        server.quit()

    return vastus

def Parooli_sisestamine():
    while True:
        print()
        print("Parooli iseseisev loomine - 1 ")
        print("Parooli genereerimine - 2 ")

        try:
            print()
            valik = int(input("Valik: "))
            if valik == 1:
                print()
                kasutaja_parool = input("Sisestage parool: ")
                if Kontrolli_parool(kasutaja_parool):
                    break
                else:
                    print()
                    print(f"{RED}Viga: Liiga nõrk parool{RESET}")
            elif valik == 2:
                kasutaja_parool = Genereeri_parool()
                print()
                print(f"Teie genereeritud parool on: '{kasutaja_parool}'")
                break
            else:
                print()
                print(f"{RED}Viga: Vale number{RESET}")
        except ValueError:
            print()
            print(f"{RED}Viga: Sisestage number{RESET}")

    return kasutaja_parool

def Loe_failist(faili_nimi):
    with open(faili_nimi, 'r') as file:
        for line in file:
            login, parool, email = line.strip().split(' ')
            loginid.append(login)
            paroolid.append(parool)
            postid.append(email)
    return loginid, paroolid, postid

def Genereeri_parool():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    parool = ''.join(random.choice(ls) for x in range(12))
    return parool

def Kontrolli_parool(parool):
    if not any(char.isupper() for char in parool):
        return False
    if not any(char.islower() for char in parool):
        return False
    if not any(char.isdigit() for char in parool):
        return False
    if not any(char in string.punctuation for char in parool):
        return False
    return True

def Registreerimine():
    print()
    print(f"{BLUE}===== REGISTREERIMINE ====={RESET}")
    while True:
        print()
        kasutaja_nimi = input("Sisestage oma nimi: ")
        if kasutaja_nimi and len(kasutaja_nimi) < 25:
            if kasutaja_nimi in loginid:
                print()
                print(f"{RED}Viga: See nimi on juba võetud{RESET}")
            else:
                break
        else:
            print()
            print(f"{RED}Viga: Nimi on liiga pikk või te ei sisestanud mitte midagi{RESET}")

    while True:
        print()
        kasutaja_post = input("Sisestage oma posti, teda kasutatakse  parooli Taastumiseks: ")
        if kasutaja_post:
            break
        else:
            print()
            print(f"{RED}Viga: Te ei sisestanud mitte midagi{RESET}")

    kasutaja_parool = Parooli_sisestamine()

    loginid.append(kasutaja_nimi)
    paroolid.append(kasutaja_parool)
    postid.append(kasutaja_post)

    print()
    print(f"{GREEN}Olete edukalt registreeritud{RESET}")
    input("'Enter' jätkamiseks")


def Sisse_logimine():
    print()
    print(f"{BLUE}===== SISSE LOGIMINE ====={RESET}")
    while True:
        print()
        kasutaja_nimi = input("Sisestage oma nimi: ")
        if kasutaja_nimi:
            if kasutaja_nimi not in loginid:
                print()
                print(f"{RED}Viga: Nime ei leitud{RESET}")
            else:
                break
        else:
            print()
            print(f"{RED}Viga: Te ei sisestanud mitte midagi{RESET}")
    while True:
        print()
        kasutaja_parool = input("Sisestage parool: ")
        if kasutaja_parool in paroolid and loginid.index(kasutaja_nimi) == paroolid.index(kasutaja_parool):
            break
        else:
            print()
            print(f"{RED}Viga: Vale parool{RESET}")

    print()
    print(f"{GREEN}Olete sisse logitud{RESET}")
    input("'Enter' jätkamiseks")


    return loginid.index(kasutaja_nimi)


def Nime_muutmine(kasutaja_nimi):
    print()
    print(f"{BLUE}===== NIME MUUTMINE ====={RESET}")
    while True:
        print()
        uus_nimi = input("Sisestage uus nimi: ")

        if uus_nimi and len(uus_nimi) < 25:
            if uus_nimi != kasutaja_nimi:
                loginid[loginid.index(kasutaja_nimi)] = uus_nimi
                break
            else:
                print()
                print(f"{RED}Viga: Uus nimi on sama, mis vana{RESET}")

        else:
            print()
            print(f"{RED}Viga: Nimi on liiga pikk või te ei sisestanud mitte midagi{RESET}")
    print()
    print(f"{GREEN}Nimi on edukalt muudetud{RESET}")

    input("'Enter' jätkamiseks")


def Parooli_muutmine(kasutaja_parool):
    print()
    print(f"{BLUE}===== PAROOLI MUUTMINE ====={RESET}")
    while True:
        print()
        vana_parool = input("Parooli muutmiseks sisestage vana parool: ")
        if vana_parool == kasutaja_parool:
            uus_parool = Parooli_sisestamine()
            if uus_parool != kasutaja_parool:
                paroolid[paroolid.index(kasutaja_parool)] = uus_parool
                print()
                print(f"{GREEN}Parool on edukalt muudetud{RESET}")
                input("'Enter' jätkamiseks")

                break
            else:
                print()
                print(f"{RED}Viga: Uus parool on sama, mis vana{RESET}")

        else:
            print()
            print(f"{RED}Viga: Vale parool{RESET}")

def Parooli_taastamine(kasutaja_post, kasutaja_parool):
    print()
    print(f"{BLUE}===== PAROOLI TAASTAMINE ====={RESET}")


    taastekood = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    pealkiri = "Taastekood"
    kiri = (f"Teie konto taastamise kood: {taastekood}\nÄrge näidake seda kellelegi")
    saatja_post = "aut.reg.pyt@gmail.com"
    saatja_posti_parool = "bwfc oibz twxz hzlb"

    if Saada_email(pealkiri, kiri, kasutaja_post, saatja_post, saatja_posti_parool):
        while True:
            try:
                print()
                sisestatud_kood = int(input("Sisestage kood: "))

                if sisestatud_kood == int(taastekood):
                    print()
                    print(f"Teie parool on: '{kasutaja_parool}'")
                    print("Ärge kaotage seda enam")
                    input("'Enter' jätkamiseks")

                    break
                else:
                    print()
                    print(f"{RED}Viga: Vale taastamise kood{RESET}")

            except ValueError:
                print()
                print(f"{RED}Viga: Sisestage kood{RESET}")