class matrix:
    def __init__(self,n:int,m:int):
        self.n=n
        self.m=m
    def create(self):
        a=[]
        x=1
        for i in range(self.n):
            b=[]
            for j in range(self.m):
                b.append(2*x)
                x+=1
            a.append(b)
        print(a)
    
print("i am rahul ")
#matrixA=matrix(2,2)
#matrixA.create()

#if __name__=="__main__":
   #print("this is also printed ")

