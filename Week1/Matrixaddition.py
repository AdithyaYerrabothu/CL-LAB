a=[[1,2,3],
    [1,2,3],
    [1,2,3]]

b=[[1,1,1],
    [1,1,1],
    [1,1,1]]
r=[[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        r[i][j]=a[i][j]+b[i][j]

for r in r:
    print(r)