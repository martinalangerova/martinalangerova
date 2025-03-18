class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# Do závorek píšeme, od jaké třídy dědíme
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.subordinates = subordinates
        self.car = car

frantisek = Employee("František Novák", "konstrukter", 25)
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Škoda Octavia 1.5 TSI")
# if isinstance(frantisek, Manager):
#     print("Objekt pochází ze tříy manager.")
#     print(f"Má auto: {marian.car}")
# else:
#     print("Objekt pochází z jiné třídy.")

# if isinstance(frantisek, Employee):
#     print(f"Zbyva dovolene: {frantisek.holiday_entitlement}")
# else:
#     print("Objekt pochází z jiné třídy.")

# marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
# frantisek = Employee("František Novák", "konstruktér", 25)
# employee_list = [marian, marketa, frantisek]

# expected_people = 0

# for item in employee_list:
#     if isinstance(item, Manager):
#         # Připravíme si pozvánku
#         print(f"Pozvánka pro {item.name} na školení leadershipu.")
#         # Započítáme si jednoho člověka navíc
#         expected_people = expected_people + 1

# print(f"Čekáme {expected_people} osob.")

marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
attribute = input("Zadej hodnotu atributu: ")
print(getattr(marketa, attribute, "neznámý atribut"))
