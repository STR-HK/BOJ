N, X = map(int, input().split())
A = list(map(int, input().split()))
s = []
for item in A:
    if X > item:
        s.append(str(item))
print(' '.join(s))