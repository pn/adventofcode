numbers = []
for line in open('input1.txt'):
    number1 = int(line)
    for number2 in numbers:
        if number1 + number2 == 2020:
            print(number1 * number2)
    numbers.append(number1)
