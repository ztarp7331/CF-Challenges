import math
n =int(input())
x=list(map(int,input().split()))
for i in x:
    count=0
    for j in range(2,math.isqrt(i)):
        if i%j==0:
            count+=1
    if count ==1:
        print("YES")
    else:
        
        print("NO")
