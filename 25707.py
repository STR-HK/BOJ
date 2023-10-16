count = int(input())
numbers = list(map(int, input().split(' ')))
numbers.sort(reverse=True)
bracelet = []

for i in range(len(numbers)):
    if i == 0:
        bracelet.append(numbers[i])
    elif 2 * i - 1 < len(numbers):
        bracelet.append(numbers[2 * i - 1])
    else:
        b = 2 * int(len(numbers) / 2)
        a = 2 * (i - int((len(numbers) + 1) / 2))
        bracelet.append(numbers[b-a])

sum = 0
for i in range(len(bracelet)):
    if i + 1 != len(bracelet):
        sum += abs(int(bracelet[i]) - int(bracelet[i+1]))
    else:
        sum += abs(int(bracelet[0]) - int(bracelet[i]))

print(sum)