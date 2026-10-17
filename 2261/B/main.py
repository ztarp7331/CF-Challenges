
t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    mn = min(li)
    mx = max(li)

    diff = mn ^ mx

    if diff == 0:
        print(mx)
    else:
        k = diff.bit_length() - 1
        ans = mx | ((1 << k) - 1)
        print(ans)

