class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self):
        # Tato metoda vrátí jednodušší, uživatelsky přívětivý výstup
        return f"Lokalita: {self.name}, Koeficient: {self.locality_coefficient}"


class Property:
    def __init__(self, locality, size, property_type):
        if not isinstance(locality, Locality):  # Kontrola, že locality je objekt typu Locality
            raise ValueError("locality musí být objekt třídy Locality.")
        self.locality = locality
        self.size = size
        self.property_type = property_type

    def __str__(self):
        # Tato metoda vrátí uživatelsky přívětivý výstup pro Property
        return f"Nemovitost ({self.property_type}) o velikosti {self.size} m², lokalita: {self.locality}"


# Příklad použití:
locality = Locality(name="Praha", locality_coefficient=1.5)
property1 = Property(locality=locality, size=100, property_type="Byt")

print(property1)  # Použití metody __str__