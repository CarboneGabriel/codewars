def high_and_low(numbers):
    numbers = sorted(numbers.split(), key=int)
    numbers = "{} {}".format(numbers[-1], numbers[0])
    return numbers

input = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
print(high_and_low(input))