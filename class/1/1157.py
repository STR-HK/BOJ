import operator
i = input()
d = {}
for a in i:
    try:
        d[a.lower()] += 1
    except:
        d[a.lower()] = 1


if len([k for k, v in d.items() if v == max(d.values())]) > 1:
    print('?')
else:
    print(max(d.items(), key=operator.itemgetter(1))[0].upper())