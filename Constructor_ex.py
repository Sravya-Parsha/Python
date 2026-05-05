class Rect:
    def __init__(self,a,b):
        self.area=a*b
    def display(self):
        print("Area is",self.area)
r=Rect(20,30)
r.display()
