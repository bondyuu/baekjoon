n = int(input())
numbers = []

for i in range(1, n + 1):
    if len(str(i)) < 3:
        numbers.append(i)
    elif len(str(i)) == 3:
        if int(str(i)[1]) * 2 == int(str(i)[0]) + int(str(i)[2]):
            numbers.append(i)

print(len(numbers))

