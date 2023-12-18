class rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display(self):
       ar=self.length*self.breadth
       print("area:",ar)
l=int(input("enter length"))
b=int(input("enter breadth"))
ob=rectangle()
ob.getdata(l,b)
ob.display()
