a, b, c = int(input()), int(input()), int(input())
pi = a * b * c
d = {}
for i in range(len(str(pi))):
    try:
        d[str(pi)[i]] += 1
    except:
        d[str(pi)[i]] = 1
for i in range(10):
    try:
        print(d[str(i)])
    except:
        print(0)