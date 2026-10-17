n=int(input())
for _ in range(n):
    x=int(input())
    s=input()
    if s.count('1')==1:
        print(0)
    elif s.count('1')==2:
        print(1)
    else:
        print(s.rfind('1')-s.find('1'))
