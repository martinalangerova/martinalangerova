from datetime import datetime, timedelta
# import datetime
# print(datetime.now())
# apollo_start = datetime(1969, 7, 16, 14, 32)
# print(apollo_start.month)
# print(apollo_start.weekday())
# print(apollo_start.isoweekday())
# print(apollo_start)
# apollo_start.isoformat()

# 16. 07. 1969, 14:32
# parse
# print(apollo_start.strftime("%d. %m. %Y, %H:%M"))
# apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
# print(apollo_pristani)
# delka_mise = apollo_pristani - apollo_start
# print(delka_mise)

# planovany_prijezd = datetime(2024, 3, 13, 19, 59)
# zpozdeni = timedelta(minutes=10)
# skutecny_prijezd = planovany_prijezd + zpozdeni
# print(skutecny_prijezd)

# print(apollo_start.strftime("%m./%d./%Y,"))
# pollo_start = datetime(1969, 7, 16, 14, 32)
# print(apollo_start.strftime("%m/%d/%Y")) 

# Solar_Orbiter = datetime(2020, 2, 10, 5, 2)
# print(Solar_Orbiter.weekday())
# print(Solar_Orbiter.isoweekday())

# uplynulo = (datetime.now()) - Solar_Orbiter
# print(uplynulo)

# from faker import Faker
# fake = Faker('cs_CZ')
# for _ in range(10):
#     print(fake.name())

import humanize

# Velké číslo
large_number = 1500000000  # 1,5 miliardy

# Použití funkce intword
humanized_large_number = humanize.intword(large_number)
print(humanized_large_number)

# Malé číslo
small_number = 123

# Použití funkce apnumber
humanized_small_number = humanize.apnumber(small_number)
print(humanized_small_number)


from num2words import num2words

# Příklad převodu
small_number = 123
word_version = num2words(small_number)
print(word_version)