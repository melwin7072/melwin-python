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
ch=0       
l=int(input("enter length"))
b=int(input("enter breadth"))
ob=rectangle()
ob.getdata(l,b)
while ch!=3:
    print("1.area")
    print("2.perimeter")
    print("3.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        ob.area()
    if ch==1:
        ob.perimeter()
else:
    print("exit")
ob.area()
ob.perimeter()
