t = int(input())
for _ in range(t):
    n = input()
    s = input()
    if s.find("...") != -1:
        print(2)
    else:
        print(s.count("."))
