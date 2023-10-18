import sys
N = int(input())
numbers = list(map(int, [sys.stdin.readline().strip() for i in range(N)]))
numbers.sort()
for number in numbers:
    print(number)