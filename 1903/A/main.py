n = int(input())
for i in range(n):
    l, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k >= 2:
        print("YES")
    if k < 2:
        if sorted(arr) == arr:
            print("YES")
        else:
            print("NO")
