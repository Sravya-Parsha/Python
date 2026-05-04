class abc:
    num=100
    def set_dim(self,a,b):
        self.total=a+b+abc.num
    def display(self):
        print("Addition is: ",self.total)
        # print(a)
a=abc()
b=abc()
a.set_dim(20,30)
a.display()
b.set_dim(30,50)
b.display()
