matrix=[]
for _ in range(5):
    row=[int(x) for x in input().split()]
    matrix.append(row)
# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
x=y=0
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            x=i+1 
            y=j+1 
print( abs(x-3) +abs(y-3))
