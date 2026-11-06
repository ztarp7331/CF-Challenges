t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    values = sorted([1 << x for x in a], reverse=True)
    total = sum(values)
    target = total // 2

    x = 0
    for v in values:
        if x + v <= target:
            x += v

    print(x * (total - x))
