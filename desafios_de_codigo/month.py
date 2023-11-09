# month = int(input("Num: "))

months_dict = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"}

try:
    month = int(input("Num: "))
    if month in months_dict.keys():
        print(months_dict[month])
except ValueError:
    print("Digite um número")

# Tentativa 1
# if month in months_dict.keys():
#     print(months_dict[month])
# else:
#     print("Digite  um número")
