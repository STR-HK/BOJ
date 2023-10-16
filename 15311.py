li=list(map(int,input().split()))

n=len(li)

possible = [False for _ in range(10000000)]

print('create possib')

possible[0]=True

for i in range(n):
    for j in range(i,n):
        s=sum(li[i:j+1])
        possible[s]=True

for i in range(1000000):
    if not possible[i]:
        print(i, end=' ')
    if i>100000:
        break