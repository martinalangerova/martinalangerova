# class Employee:
#     def __init__(self, name, position, holiday_entitlement):
#         self.name = name
#         self.position = position
#         self.holiday_entitlement = holiday_entitlement
    
#     def get_info(self):
#         return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    
# frantisek = Employee("František Novák", "konstruktér", 25)
# print(frantisek.get_info())


class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
    
    def delivery_price(self):
        if self.weight < 10:
            return 129
        if self.weight < 20:
            return 159
        return 359

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    

package_1 = Package("Krakovská 583/9, Praha", 1, "nedoručen")
package_2 = Package("Pernerova 702/39, Praha", 30, "nedoručen")
print(package_1.get_info())
print(package_2.get_info())
print(package_2.delivery_price())