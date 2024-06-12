n=int(input("enter the number of rows : "))
m=int(input("enter the number of columns : "))
A=[[] for i in range(n)]
for i in range(n):
    for j in range(m):
        x=int(input(f"enter data for the matrix {i+1}th row {j+1}th column : "))
        A[i].append(x)
print(A)