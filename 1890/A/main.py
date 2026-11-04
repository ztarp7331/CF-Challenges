t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    freq = {}
    for i in range(n):
        freq[l[i]] = freq.get(l[i], 0) + 1
    if len(freq) > 2:
        print("No")
    elif len(freq) == 1:
        print("Yes")
    else:
        valueFreq = list(freq.values())
        if abs(valueFreq[0] - valueFreq[1]) <= 1:
            print("Yes")
        else:
            print("No")
