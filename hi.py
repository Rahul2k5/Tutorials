class Matrix:
    def __init__(self, n:int, m:int, A:list):
        self.n = n
        self.m = m
        self.A = A
        
    def create(self):
        if not self.A:
            self.A = [[] for _ in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    x = int(input(f"Enter {i+1}th row {j+1}th element of the matrix: "))
                    self.A[i].append(x)
        else:
            print("Matrix already initialized.")
    
    def Matrix_multiple2(self):
        for i in range(self.n):
            for j in range(self.m):
                self.A[i][j] *= 2

class Main:
    def __init__(self):
        pass
    
    def run(self):
        n = int(input("Enter rows: "))
        m = int(input("Enter columns: "))
        A = []
        choice = input("Do you want to enter matrix manually? (y/n): ")
        if choice.lower() == 'y':
            matrix_obj = Matrix(n, m, A)
            matrix_obj.create()
        else:
            for i in range(n):
                row = list(map(int, input(f"Enter row {i+1}: ").split()))
                A.append(row)
            matrix_obj = Matrix(n, m, A)
        
        print("Original Matrix:")
        for row in matrix_obj.A:
            print(row)

        matrix_obj.Matrix_multiple2()
        
        print("Matrix after multiplication by 2:")
        for row in matrix_obj.A:
            print(row)

if __name__ == "__main__":
    main_obj = Main()
    main_obj.run()
