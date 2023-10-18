while True:
    seg = sorted(list(map(int, input().split())))
    if seg[0] == 0:
        break
    if seg[0] ** 2 + seg[1] ** 2 == seg[2] ** 2:
        print("right")
    else:
        print("wrong")