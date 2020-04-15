"""
《python常用模块（2）》
知识点：
1.对象列表存在(浅拷贝,深拷贝)
2.浅拷贝（copy）：没有生成自己的对象，和照镜子一样,变量共用
  深拷贝（deepcopy）：生成自己的对象，不随原来的拷贝对象改变，变量不共用


"""
>>> class weirdbird:
    def __init__(self,wings,legs,eyes,color):
        self.w = wings
        self.l = legs
        self.e = eyes
        self.c = color
        self.showbird()
    def showbird(self):
        print('you have %s wings&%s legs&%s eyes&%s color.'%(self.w,self.l,self.e,self.c))

    
>>> tom=weirdbird(3,3,3,'blue')
you have 3 wings&3 legs&3 eyes&blue color.
>>> jerry=weirdbird(4,4,4,'red')
you have 4 wings&4 legs&4 eyes&red color.
>>> nick=weirdbird(5,5,5,'black')
you have 5 wings&5 legs&5 eyes&black color.
>>> birlist1=[tom,jerry,nick]
>>> import copy
>>> birlist2=copy.copy(birlist1)
>>> birlist1[0].w=666
>>> birlist1[0].showbird()
you have 666 wings&3 legs&3 eyes&blue color.
>>> birlist2[0].showbird()
you have 666 wings&3 legs&3 eyes&blue color.
>>> alice=weirdbird(6,6,6,'pink')
you have 6 wings&6 legs&6 eyes&pink color.
>>> birlist1.append(alice)
>>> len(birlist1)
4
>>> len(birlist2)
3
>>> birlist2=copy.copy(birlist1)
>>> len(birlist1)
4
>>> len(birlist2)
4
>>> birlist2=copy.deepcopy(birlist1)
>>> birlist1[0].w=108
>>> birlist1[0].showbird()
you have 108 wings&3 legs&3 eyes&blue color.
>>> len(birlist1)
4
>>> birlist2[0].showbird()
you have 666 wings&3 legs&3 eyes&blue color.
>>> no5=weirdbird(7,7,7,'white')
you have 7 wings&7 legs&7 eyes&white color.
>>> birlist1.append(no5)
>>> len(birlist1)
5
>>> len(birlist2)
4
>>> 
