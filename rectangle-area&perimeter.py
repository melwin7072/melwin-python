class rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
       ar=self.length*self.breadth
       print("area:",ar)

    def perimeter(self):
       pr=2*(self.length+self.breadth)
       print("perimeter:",pr)
       
l=int(input("enter length"))
b=int(input("enter breadth"))
ob=rectangle()
ob.getdata(l,b)
ob.area()
ob.perimeter()
