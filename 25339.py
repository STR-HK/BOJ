N, Q = map(int,input().split())
p = [i+1 for i in range(N)]
for i in range(Q):
    a, l, r = map(int, input().split())
    if a == 1:
        lth = p[l-1]
        p[l-1] = p[r-1]
        p[r-1] = lth
    else:
        p = p[:l-1] + p[l-1:r][::-1] + p[r:]
    s = 0
    for j in range(len(p)):
        for k in range(j+1, len(p)):
            print(j, k)
            # if p[j]>p[k]:
            #     s+=1
    print(s%2)