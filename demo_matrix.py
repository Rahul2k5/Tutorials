class matrix:
    def __init__(self,n:int,m:int):
        self.n=n
        self.m=m
    def create(self):
        a = []
        x = 1
        for i in range(self.n):
            b = []
            for j in range(self.m):
                b.append(2 * x)
                x += 1
            a.append(b)
        print(a)


    print("hi")

    def main():
        matrixA=matrix(4,4)
        matrixA.create()

print("hi")
if __name__=="__main__":
    #main()
    pass
