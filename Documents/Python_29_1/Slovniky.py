# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavola v deset": 5619,
# }
# for key, value in sales.items():
#     print(f"Knihy {key} bylo prodáno {value} kusů.")

# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]
# total_sales = 0
# for row in books:
#     if row["year"] == 2019:
#         total_sales = total_sales + row["sold"] * row["price"]
# print(total_sales)

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
# for key, value in school_report.items():
#     print(f"Známka z předmětu {key} byla {value}.")

sum_of_marks = 0
for mark in school_report:
    sum_of_marks += mark[1]
average = sum_of_marks / len(school_report)
print(f"Průměrná známka studenta/studentky je {average}.")