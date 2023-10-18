N, K = map(int, input().split())
from collections import deque
deq = deque([i+1 for i in range(N)])
josephus = []
while len(deq) != 0:
    for i in range(K-1):
        a = deq.popleft()
        deq.append(a)
    josephus.append(str(deq.popleft()))
print(f"<{', '.join(josephus)}>")
