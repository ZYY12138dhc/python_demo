

"""
《类与对象（self用法）总结》
知识点：
1.
2.

#eg.1
class test1:
    def print1(self):
        print('a+b=',self.a+self.b)

class test2(test1):
    def print2(self,a,b):
        self.a=a
        self.b=b
        self.print1()#调用父类函数
        
>>> zyy=test2()
>>> zyy.print2(3,6)
a+b= 9
>>>

#eg.2
class juxing:
    def round(self,a,b):
        self.a=a
        self.b=b
        print('round is:',2*(a+b))
    def area(self):
        print('area is:',self.a*self.b)


>>> zyy=juxing()
>>> zyy.round(3,5)
round is: 16
>>> zyy.area()
area is: 15
>>>

#eg.3
class juxing():
    def count(self,a,b):
        self.a=a
        self.b=b
        self.area_round()#不用声明self
    def area_round(self):
        print('round is:',2*(self.a+self.b))
        print('area is:',self.a*self.b)


>>> zyy=juxing()
>>> zyy.count(3,6)
round is: 18
area is: 18
>>>

"""
