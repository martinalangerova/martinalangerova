# jmeno = "Martina "
# prijmeni = "Langerova"
# cele_jmeno = jmeno + prijmeni
# # obrácení hodnoty
# print (cele_jmeno[::-1])

inzerat = "Na této pracovní pozici se bude využívat Python a SQL"
# Je řetězec "Python" v řetězci inzerat?
if "Python" in inzerat:
    print("Hura")
else:
    print("Bůůů")
email = "spatny-mail.cz"
if "@" not in email:
    print("V e-mailu chybí zavináč!")