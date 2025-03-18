class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
    def take_holiday(self, days):
        if days <= self.holiday_entitlement:
            self.holiday_entitlement = self.holiday_entitlement - days
            return "Užij si to."
        else:
            return f"Máš nárok jenom na {self.holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér", 25)
print(frantisek.take_holiday(20))
print(frantisek.take_holiday(10))
# Chci zjistit nárok na dovolenou Františka
print(frantisek.holiday_entitlement)