N, M = map(int, input().split())
BOARD = []
for i in range(N):
    BOARD.append(input())
yOffsetMax = N - 8
xOffsetMax = M - 8
line1 = "WBWBWBWB"
line2 = "BWBWBWBW"
diffs = []
for x in range((xOffsetMax + 1) * (yOffsetMax + 1) * 2):
    diffs.append(0)
cnt = 0
for i in range(xOffsetMax + 1):
    for j in range(yOffsetMax + 1):
        for c in range(2):
            for k in range(8):
                linet = BOARD[k + j][i:(i + 9)]
                if k % 2 == 1:
                    for a in range(8):
                        if c % 2 == 1:
                            if line1[a] != linet[a]:
                                diffs[cnt] += 1
                        else:
                            if line2[a] != linet[a]:
                                diffs[cnt] += 1
                else:
                    for a in range(8):
                        if c % 2 == 1:
                            if line2[a] != linet[a]:
                                diffs[cnt] += 1
                        else:
                            if line1[a] != linet[a]:
                                diffs[cnt] += 1

            cnt += 1
print(min(diffs))