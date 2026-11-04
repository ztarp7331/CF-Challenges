# imo just do early exit if min(array) is not at index 0 because operation never allows to fix that.
n = int(input())
for _ in range(n):
    x = int(input())
    l = list(map(int, input().split()))
    if l[0] != 1:
        print("No")

    else:
        print("Yes")
