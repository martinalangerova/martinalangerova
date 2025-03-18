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
    

package_1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
package_2 = Package("Pernerova 702/39, Praha", 12.47, "nedoručen")
print(package_1.get_info())
print(package_2.get_info())
print(package_2.delivery_price())
