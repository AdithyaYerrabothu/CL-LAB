l=[]
k=[]
s=0
n=int(input("Enter number of dimensions of vector: "))
for i in range(n):
    a=int(input("Enter coefficient of vector a:"))
    b=int(input("Enter coefficient of vector b:"))
    l.append(a)
    k.append(b)
print("vector 1 =",l)  
print("vector 2 =",k)

for i in range(len(l)):
    s=s+l[i]*k[i]
    
print("dot product=",s)