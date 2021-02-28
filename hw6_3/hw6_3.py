n = int(input('Input numbers : '))
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0
result = []
i = 0
while i < len(numbers):
    if numbers[i] != 0:
        result.append(numbers[i])
    i += 1
print(result)