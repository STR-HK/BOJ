N = int(input())
words = []
for i in range(N):
    words.append(input())
words = list(set(words))
words.sort()
maxlength = 0
for i in range(len(words)):
    if len(words[i]) > maxlength:
        maxlength = len(words[i])
for i in range(maxlength):
    for j in range(len(words)):
        if (len(words[j]) == i + 1):
            print(words[j])