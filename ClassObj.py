"""Question:
Create a Python class named Rectangle to represent rectangles.
The class should have attributes length and width, and methods to calculate the area and perimeter of the rectangle. 
Create an object of the Rectangle class with length 5 and width 3. Print the area and perimeter of the rectangle."""
class rectangle:
    def __init__(self,l:int,w:int,) -> int:
        self.l=l
        self.w=w
    def area(self):
        area=self.l*self.w
        print("area of rectangle is ",area)
    def perimeter(self):
        perimeter=((2*self.l)+(2*self.w))
        print("Perimeter of the rectangle is ",perimeter)

area1=rectangle(23,24)
perimeter1=rectangle(15,30)
x=area1.area()
y=perimeter1.perimeter()
print(x,y)