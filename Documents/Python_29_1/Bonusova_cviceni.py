def total_price(osoba, snidane=False):
    if snidane:
        return osoba * (850 + 125)
    else:
        return osoba * 850

vysledek = total_price(1, True)
print(vysledek) 

# print(total_price(3, True))
# print(total_price(2))