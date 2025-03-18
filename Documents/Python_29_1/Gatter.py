
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.subordinates = subordinates
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
auto = getattr(marian, "car", "Nemá auto")
# Vypíše "Škoda Octavia 1.5 TSI"
print(auto)

frantisek = Employee("František Novák", "konstruktér", 25)
auto = getattr(frantisek, "car", "Nemá auto")
# Vypíše "Nemá auto"
print(auto)