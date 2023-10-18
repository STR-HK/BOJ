while True:
    n = input()
    b = 'yes'
    if n == '0':
        break
    if len(n) % 2 == 1:
        max=int((len(n) - 1) / 2)
        for i in range(max):
            if n[i] != n[max*2-i]:
                b = 'no'
    else:
        max = int(len(n)/ 2)
        for i in range(max):
            if n[i] != n[max*2-i-1]:
                b = 'no'
    print(b)