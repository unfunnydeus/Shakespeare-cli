number = int(input("Введите номер сонета: "))

roman = {
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

result_roman = ""

for value in roman:
    while number >= value:
        result_roman += roman[value]
        number -= value

print(result_roman)
