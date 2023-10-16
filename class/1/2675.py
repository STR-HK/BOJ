t = int(input())
rl = []
sl = []
for i in range(t):
    r, s = input().split()
    rl.append(int(r))
    sl.append(s)

for i in range(t):
    r = rl[i]
    s = sl[i]
    for j in range(len(s)):
        for k in range(r):
            print(s[j], end="")
    print("")