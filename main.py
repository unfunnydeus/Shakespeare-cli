number = int(input("Введите номер сонета: "))

roman = {
    10: "X",
    5: "V",
    1: "I",
    50: "L",
    100: "C",
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC"
}

result_roman = ""

while number >= 100:
    result_roman += roman[100]
    number -= 100
while number >= 90:
    result_roman += roman[90]
    number -= 90
while number >= 50:
    result_roman += roman[50]
    number -= 50
while number >= 40:
    result_roman += roman[40]
    number -= 40
while number >= 10:
    result_roman += roman[10]
    number -= 10
while number >= 9:
    result_roman += roman[9]
    number -= 9
while number >= 5:
    result_roman += roman[5]
    number -= 5
while number >= 4:
    result_roman += roman[4]
    number -= 4
while number >= 1:
    result_roman += roman[1]
    number -= 1


print(result_roman)
