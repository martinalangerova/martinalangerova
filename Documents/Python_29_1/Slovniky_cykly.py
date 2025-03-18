item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
item['price'] = 929
item['weight'] = 0.4

# key = 'price'
# item[key] = 929
# print(item[key], "Kč.")

# if "weight" in item:
#     print(f"Hmotnost předmětu je {item['weight']} kg.")
# else:
#     print("Hmotnost není zadána.")

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# for key in sales:
#     print(key)
# for key, value in sales.items():
    # print(f"Knihy {key} bylo prodáno {value} výtisků.")
# for key, value in sales.items():
#     item = (key, value)
#     print("Knihy", item[0], "bylo prodáno", item[1])

# for key, value in sales.items():
    # print("Knihy", key, "bylo prodáno", value, "vytisků.")

sales_values = sales.values()
total_sales = sum(sales_values)
print(total_sales)

total_sales = 0

for key, value in sales.items():
    # print(f"Knihy {key} bylo prodáno {value} výtisků.")
    print("Knihy", key, "bylo prodáno", value, "vytisků.")
    total_sales = total_sales + value

print(f"Celkem bylo prodáno {total_sales} výtisků.")