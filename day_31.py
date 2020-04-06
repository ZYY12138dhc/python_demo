#eg.4
class juxing:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def round(self):
        print('round is :',2*(self.a+self.b))
    def area(self):
        print('area is :',self.a*self.b)


>>> zyy=juxing(3,7)
>>> zyy.round()
round is : 20
>>> zyy.area()
area is : 21
>>>

"""
#eg.1计算矩形的周长和面积
class juxing:
    def round_area(self,a,b):
        print('round is :',2*(a+b))
        print('area is :',a*b)

>>> zyy=juxing()
>>> zyy.round_area(3,6)
round is : 18
area is : 18
>>>


#eg.2
class juxing:
    def round(self,a,b):
        print('round is :',2*(a+b))
    def area(self,a,b):
        print('area is :',a*b)
        
>>> zyy=juxing()
>>> zyy.round(3,6)
round is : 18
>>> zyy.area(3,6)
area is : 18
>>> 

#eg.3
class juxing:
    def round(self,a,b):
        self.a=a
        self.b=b
        print('round is :',2*(a+b))
    def area(self):
        print('area is :',self.a*self.b)

>>> zyy=juxing()
>>> zyy.round(3,6)
round is : 18
>>> zyy.area()
area is : 18
>>> 


知识点：
1. 类与对象练习
2.

"""
