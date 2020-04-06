#eg.4
class test1:
    def move(self):
        print('move!')

class test2(test1):#test1是test2的父类
    def dance(self):
        print('dance!')

class test3(test2):#test2是test3的父类
    def sing(self):
        self.move()#调用祖类
        self.dance()#调用父类
        print('大家high起来！')
    



"""
#eg.1
class self_test:
    def __init__(self,a,b):#初始化函数,记住，是两条横杠
        self.a=a#给self赋值，在别的函数里面也能使用a和b
        self.b=b
        print('a+b=',self.a+self.b)
    def chengfa(self):
        print('a*b=',self.a*self.b)


>>> zyy=self_test(3,5)
a+b= 8
>>> zyy.chengfa()
a*b= 15
>>> 


#eg.2
class self_test:
    def count(self,a,b):
        print('a+b=',a+b)
    def minus(self,a,b):
        print('a-b=',a-b)


>>> zyy=self_test()
>>> zyy.count(3,5)
a+b= 8
>>> zyy.minus(3,5)
a-b= -2
>>>


#eg.3
class self_test:
    def __init__(self,a,b):#初始化的函数，要在对象的时候加入参数
        self.a=a
        self.b=b
    def count(self):
        print('a+b=',self.a+self.b)
    def minus(self):
        print('a-b=',self.a-self.b)
    def show(self):
        self.count()
        self.minus()



>>> zyy=self_test(3,5)
>>> zyy.count()
a+b= 8
>>> zyy.minus()
a-b= -2
>>> 
>>> zyy.show()
a+b= 8
a-b= -2
>>> 


类与对象（4）
知识点：
1.初始化函数，对象
2.
"""
