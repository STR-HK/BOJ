N = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers) / N / max(numbers) * 100)