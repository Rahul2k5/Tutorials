"""
class matrix:
    def __init__(self,n:int,m:int,x:int,A:list):
        self.n=n
        self.m=m
        self.x=x
    def create(self):
        self.n=int(input("enter rows : "))
        self.m=int(input("enter columns : "))
        self.A=[]
        #for i in range(self.n):
            for j in range(self.m):
               self.x=int(input(f"enter {i+1}th row {j+1}th element of the matrix : "))
               self.A[i].append(self.x)

"""
def Matrix_multiple2():
    
    cnt=1
    print("enter value of n : ")
    n=int(input())
    m=int(input())
    print(n,m)
    A=[]*(m*n)
    for i in range(n):
        #print("outer loop",i)
        b=[]
        for j in range(m):
            #print("inner loop",i,j)
            
            b.append(2*cnt)
            cnt+=1
            #print("i,j",i,j,A[i][j])
        A.append(b)
    print(A)




def Matrix_multiple2_m():
    n=int(input("enter number of rows : "))
    m=int(input("enter number of columns : "))
    x=1
    A=[]*(n)
    for i in range(n):
        b=[]
        for j in range(m):
            b.append(2*x)
            x+=1
        A.append(b)
    print(A)
Matrix_multiple2_m()
            