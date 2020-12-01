numbers = []
for line in open('input1.txt'):
    number1 = int(line)
    for i, number2 in enumerate(numbers):
        for j in range(i):
            number3 = numbers[j]
            if number1 + number2 + number3 == 2020:
                print(number1 * number2 * number3)
    numbers.append(number1)
