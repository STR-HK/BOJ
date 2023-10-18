from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
combi = list(combinations(cards, 3))
res = 0
for com in combi:
    s = sum(com)
    if s > res:
        if s <= m:
            res = s
            
print(res)