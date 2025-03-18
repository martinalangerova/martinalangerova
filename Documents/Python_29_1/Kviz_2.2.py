# def kofein_za_den(pocet_espresso, pocet_filtrkava=0):
#     return pocet_espresso * 75 + pocet_filtrkava * 150
# print(kofein_za_den(2,1))

def spocitej_cenu(cena_za_kus, kusy, postovne):
    return cena_za_kus * kusy + postovne

print(spocitej_cenu(cena_za_kus=100, postovne=90, kusy=5))