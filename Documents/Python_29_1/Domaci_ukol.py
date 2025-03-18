
import math

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient
    
class Property:
    def __init__(self, locality: Locality):
        if not isinstance(locality, Locality):
            raise ValueError("locality musí být objekt třídy Locality.")
        self.locality = locality

class Estate(Property):
    def __init__(self, locality: Locality, estate_type: str, area: float):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    ESTATE_COEFFICIENTS = {
        "land": 0.85,
        "building site": 9,
        "forrest": 0.35,
        "garden": 2
    }
    def calculate_tax(self) -> int:
        tax = self.area * self.ESTATE_COEFFICIENTS[self.estate_type] * self.locality.locality_coefficient
        return math.ceil(tax)

class Residence(Property):
    def __init__(self, locality: Locality, area: float, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self) -> int:
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax *= 2
        return math.ceil(tax)
    
# Příklad použití:
locality1 = Locality("Manětín", 0.8)
estate1 = Estate(locality1, "land", 900)
residence1 = Residence(locality1, 120, False)
locality2 = Locality("Brno", 3)
residence2 = Residence(locality2, 90, True)

print("Tax for estate:", estate1.calculate_tax())
print("Tax for residence (non-commercial):", residence1.calculate_tax()) 
print("Tax for residence (commercial):", residence2.calculate_tax())




