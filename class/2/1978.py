import math
N = int(input())
numbers = sorted(list(map(int, input().split())))
Eratos = []
for i in range(1000):
    isPrime = True
    for j in range(int(math.sqrt(i+1))):
        if i+1 == 1:
            isPrime = False
        if j+1 == 1:
            continue
        if (i+1) % (j+1) == 0:
            isPrime = False
    if isPrime:
        Eratos.append(i+1)
c = 0
for number in numbers:
    start = 0
    end = len(Eratos)-1
    while start <= end:
        mid = (start + end) // 2
        if Eratos[mid] == number:
            c+=1
            break
        elif Eratos[mid] > number:
            end = mid - 1
        else:
            start = mid + 1
print(c)