# def vynasob_cislo_deseti(cislo):
#     return cislo*10
# print(vynasob_cislo_deseti(5))

# def spocitej_cenu(cena_za_kus, kusy, postovne):
#     cena = cena_za_kus * kusy
#     return cena
# print(spocitej_cenu(250, 3, 90))

# def vypocitej_slevu(kod):
#     if kod == "MAM_RADA_JAVU":
#         return 5
#     elif kod == "MAM_RADA_PYTHON":
#         return 30
#     else:
#         return 0
    
def vypocitej_slevu(kod):
    if kod == "MAM_RADA_JAVU":
        return 5  # Funkce se zde ukončí, pokud podmínka platí
    elif kod == "MAM_RADA_PYTHON":
        return 30  # Funkce se ukončí zde, pokud platí tato podmínka
    return 0  # Pokud žádná podmínka neplatí, vrátí 0
kod = (vypocitej_slevu("MAM_RADA_JAVU"))
print(kod)

# def vypocitej_slevu(kod):
#     slevy = {
#         "MAM_RADA_JAVU": 5,
#         "MAM_RADA_PYTHON": 30
#     }
#     return slevy.get(kod, 0)  # Vrátí hodnotu ze slovníku nebo 0 jako výchozí hodnotu

