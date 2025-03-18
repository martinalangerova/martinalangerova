filmy = ["čtyři svatby a jeden P", "Pán Pythonů", "Herry Poter", "Foresst Python"]
cislo_filmu = int(input("Zadej číslo filmu: "))
if cislo_filmu < len(filmy):
    print(filmy[cislo_filmu])
else:
    print("Tolik filmů nemame")