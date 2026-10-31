t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    gapArray = []
    for i in range(1, n):
        gapArray.append(a[i] - a[i - 1])
    gapArray.append(a[0] - 0)
    gapArray.append((x - a[n - 1]) * 2)
    print(max(gapArray))
