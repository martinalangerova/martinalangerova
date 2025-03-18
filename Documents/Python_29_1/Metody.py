inzerat = "Na této pracovní pozici se bude využívat Python a SQL"
# Je řetězec "Python" v řetězci inzerat?¨
inzerat_velkymi = inzerat.upper()
if "Python" in inzerat:
    print("Hura")
else:
    print("Bůůů")

print("martin".upper())

retezec = " czechitas "
print(retezec.strip())

retezec = "po ut st čt pá"
seznam_retezcu = retezec.split()
print(seznam_retezcu)

zavod = "Alena Nováková, Josef Nový, Natálie Modrá"
zavod_seznam = zavod.split(", ")
print(zavod_seznam[0])

zavod_seznam = ["Alena Nováková, Josef Nový, Natálie Modrá"]
zavod_retezec = "".join(zavod_seznam)
print(zavod_retezec)