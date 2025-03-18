# def zkontroluj_telefonni_cislo(telefonni_cislo: str):
#     if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
# # zacina s 420 a délka je 13
#         return True
#     else:
#         return False
    
# vysledek_1 = zkontroluj_telefonni_cislo("+420724856740")
# print(vysledek_1)
# vysledek_2 = zkontroluj_telefonni_cislo("text")
# print(vysledek_2)


# def zkontroluj_telefonni_cislo(telefonni_cislo: str) -> bool:
#     # Začíná s +420 A délka je 13
#     if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
        

# vysledek_1 = zkontroluj_telefonni_cislo("+420734123456")
# vysledek_2 = zkontroluj_telefonni_cislo("test")

# def zkontroluj_telefonni_cislo_bool(telefonni_cislo: str) -> bool:
#     # Začíná s +420 A délka je 13
#     if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
#         return True
#     else:
#         return False
# def zkontroluj_telefonni_cislo_str(telefonni_cislo: str) -> str:
#     # Začíná s +420 A délka je 13
#     if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
#         return "OK"
#     else:
#         return "Číslo musí začínát +420 a mít 13 znaků"

# vysledek_1 = zkontroluj_telefonni_cislo_bool("+420734123456")
# print(vysledek_1)
# vysledek_2 = zkontroluj_telefonni_cislo_bool("test")
# print(vysledek_2)
# vysledek_1 = zkontroluj_telefonni_cislo_str("+420734123456")
# print(vysledek_1)
# vysledek_2 = zkontroluj_telefonni_cislo_str("test")
# print(vysledek_2)

def zkontroluj_telefonni_cislo_bool(telefonni_cislo):
    # Začíná s +420 A délka je 13
    if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
        return True
    else:
        return False
def zkontroluj_telefonni_cislo_str(telefonni_cislo: str) -> str:
    # Začíná s +420 A délka je 13
    if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
        return "OK"
    else:
        return "Číslo musí začínát +420 a mít 13 znaků"
testovaci_cislo = "+420734123456"
vysledek_1 = zkontroluj_telefonni_cislo_bool(testovaci_cislo)
print(vysledek_1)
len(vysledek_1)