def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    numbers.sort()
    numbers = str(numbers[-1]) + " " + str(numbers[0])
    return numbers

input = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
print(high_and_low(input))