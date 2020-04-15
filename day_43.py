"""
《python常用模块（1）》
知识点：
1.turtle
2.模块：集合的形式（类，函数，对象，变量）

#eg.1
>>> import turtle
>>> draw=turtle.Pen()
>>> draw.forward(100)
>>> math.pi
3.141592653589793
>>> math.pow(7,2)#c乘方
49.0
>>> math.sqrt(49)#开方
7.0
>>> math.sin(math.radians(30))#radians是弧度，sin只接受弧度计算
0.49999999999999994
>>>

"""

#eg,2
class weirdbird:
    def __init__(self,wings,legs,eyes,color):
        self.w = wings
        self.l = legs
        self.e = eyes
        self.c = color
        self.showbird()
    def showbird(self):
        print('you have %s wings&%s legs&%s eyes&%s color.'%(self.w,self.l,self.e,self.c))
    
"""
>>> zyy=weirdbird(3,3,3,'red')
you have 3 wings&3 legs&3 eyes&red color.
>>> import copy
>>> nancy=copy.copy(zyy)
>>> nancy.showbird()
you have 3 wings&3 legs&3 eyes&red color.
>>> zyy.w=9
>>> zyy.showbird()
you have 9 wings&3 legs&3 eyes&red color.
>>> nancy.showbird()
you have 3 wings&3 legs&3 eyes&red color.
>>> 
"""
