N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))
for i in range(M):
    start = 0
    end = N - 1
    fin = False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == numbers[i]:
            print(1)
            fin = True
            break
        elif A[mid] > numbers[i]:
            end = mid - 1
        else:
            start = mid + 1
    if not fin:
        print(0)
