"""
#eg.1
<class 'int'>
>>> a = 3.1415
>>> type(a)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(0<1)
<class 'bool'>
#返回值是1或0
>>> (0<1)+(3>5)
1
>>> True+True
2
>>> True+False
1
>>> True>False
True
>>> 
#强制转换
>>> a = 3.1415
>>> type(a)
<class 'float'>
>>> int(a)
3
>>> int(3.1415)
3
>>> int(4.0)
4
>>> float(3)
3.0
>>> float(5+10)
15.0
>>> type(float(3))
<class 'float'>

#强制转换字符
>>> str('3.1415')
'3.1415'
>>> str(3.1415)
'3.1415'
>>> str(True)
'True'

#必须满足同种类型才能转换
>>> int('3.8')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int('3.8')
ValueError: invalid literal for int() with base 10: '3.8'
>>>


#eg.2
>>> 1/3
0.3333333333333333
>>> 1//3
0
>>> 7//2
3
>>> 2/3
0.6666666666666666
>>> 2//3
0
>>> 


#eg.3
>>> 5%2
1
>>> 1%3
1
>>> 6%3
0
>>> 

#eg.4
#and
>>> (1>0) and (2>1)
True
>>> (1>0) and (2<1)
False

#or
>>> (1>0) or (2<1)
True
>>> (1<0) or (2<1)
False

#not
>>> not 1
False
>>> not 0
True
>>> 

>>> True and False
False
>>> True and True
True
>>> True or False
True
>>> False or False
False
>>>

>>> 5>2 and 2-1
1
>>> not(5>2) and 2-1
False
>>> 

"""

eg.5
#优先级or <and <not 
a = 10
b = 20
c = 50
d = 45
if not a<b or c<d and b>c :
    print("yes")
else:
    print("no")

no
>>> 

"""
知识点
1.  int[整数] float[小数] bool[布尔值0/1]
    eg.1
2.  +-*/ //[整除运算符]
    eg.2
3.  %[除余]
    eg.3
4.  逻辑运算符
    and[两边同时成立才True,有一个为假则是False]
    or[两边只要有一个为真，就是True,两个都为假，才是False]
    not[非运算]
    eg.4
5.  优先级[or <and <not ]
    eg.5


"""
