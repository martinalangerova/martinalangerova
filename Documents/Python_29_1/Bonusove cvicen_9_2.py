# cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# # zjistete kolik znaku zabira nejdelsi cislo na seznamu
# délky_cisel = []
# for c in cisla:
#     c = str(c)
#     aktualni_delka = len(c)
#     delky_cisel.append(aktualni_delka)
# print(delky_cisel)

# cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# # Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
# delky_cisel = []
# for c in cisla:
#     c = str(c)
#     aktualni_delka = len(c)
#     delky_cisel.append(aktualni_delka)
# print(delky_cisel)
# maximalni_delka = max(delky_cisel)
# for c in cisla:
#     c = str(c)
#     aktualni_delka = len(c)
#     print(".." + c)



# cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# # Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
# delky_cisel = []
# for c in cisla:
#     c = str(c)
#     aktualni_delka = len(c)
#     delky_cisel.append(aktualni_delka)
# print(delky_cisel)
# maximalni_delka = max(delky_cisel)
# for c in cisla:
#     c = str(c)
#     aktualni_delka = len(c)
#     c = c.rjust(maximalni_delka, ".")
#     print(c)

cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
max_cislo = max(cisla)
max_cislo = str(max_cislo)
maximalni_delka = len(max_cislo)
for c in cisla:
    c = str(c)
    c = c.rjust(maximalni_delka, ".")
    print(c