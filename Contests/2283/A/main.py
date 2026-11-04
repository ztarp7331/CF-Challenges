t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l > 0 or r < 0:
        print(abs(abs(r) - abs(l)))
        continue
    elif l == 0 and r == 0:
        print(0)
        continue
    elif l == 0 and r > 0:
        print(r - 1)
        continue
    elif l < 0 and r == 0:
        print(abs(l) - 1)
    else:
        if abs(l) == abs(r):
            print(0)
        elif abs(l) < abs(r):
            hashSet = set(range(abs(l) + 1, r + 1))
            print(len(hashSet) - 1)
        else:
            hashSet = set(range(l, -r))
            print(len(hashSet) - 1)
