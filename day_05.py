"""
#eg.1
#元组
>>> tuple1=(1,2,3,'zyy',True)
>>> tuple1
(1, 2, 3, 'zyy', True)
>>> print(tuple1)
(1, 2, 3, 'zyy', True)
>>> tuple1[0]
1
>>> tuple1[1]
2
>>> 
>>> tuple1=1,2,3,'zyy',True
>>> tuple1
(1, 2, 3, 'zyy', True)
>>> 
>>> type(tuple1)
<class 'tuple'>
>>> a=1
>>> type(a)
<class 'int'>
>>> type(0.2)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type('zyy')
<class 'str'>
>>> type([1,2,3])
<class 'list'>
>>> 

#eg.2
#如何判断是否是元组
#思考编辑器会把tuple1当成元组还是int整型
>>> tuple1=1
>>> type(tuple1)
<class 'int'>

>>> tuple1=(1)
>>> type(tuple1)
<class 'int'>
>>> 

#关键是否有逗号
>>> tuple1=1,
>>> type(tuple1)
<class 'tuple'>
>>>

#eg.3
#输出元组所有元素
>>> tuple1=1,2,3,'zyy',True
>>> tuple1[:]
(1, 2, 3, 'zyy', True)

#输出指定元组后所有元素
>>> tuple1[1:]
(2, 3, 'zyy', True)
>>>

#输出指定元组位置前的所有元素，不包括当前位置
>>> tuple1[:3]
(1, 2, 3)
>>> 
>>> tuple1[1:4]
(2, 3, 'zyy')
>>> 

#eg.4
#不能使用append()
>>> tuple1.append(88)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    tuple1.append(88)
AttributeError: 'tuple' object has no attribute 'append'
>>>

#不能使用del删除元组
>>> del tuple1
>>> tuple1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    tuple1
NameError: name 'tuple1' is not defined
>>> 

#不支持del
>>> tuple1=1,2,3,'zyy',True
>>> del tuple1[3]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    del tuple1[3]
TypeError: 'tuple' object doesn't support item deletion
>>> 

#eg.5
#元组相乘
>>> tuple2=(8,)
>>> tuple1*8
64
>>> tuple2*8
(8, 8, 8, 8, 8, 8, 8, 8)
>>> 


#eg.6
#如何聪明的增加，减少元组元素
#增加
>>> tuple1=1,2,3,4,6
>>> tuple1=tuple1[:4]+(5,)+tuple1[4:]
>>> tuple1
(1, 2, 3, 4, 5, 6)
>>> tuple1=tuple1[:4]+(5,)+(tuple1[4],)
>>> tuple1
(1, 2, 3, 4, 5, 5)

#减少
>>> tuple1=1,2,3,4,5,6,6
>>> tuple1=tuple1[:5]+tuple1[6:]
>>> tuple1
(1, 2, 3, 4, 5, 6)
>>> 

"""


"""
知识点
1.  元组
    eg.1
2.  如何判断是否是元组
    #eg.2
3.  输出元组
    eg.3
4.  元组不支持append(),del,insert()[可以删除整个元组，但是不能单独增加或删除某个元组元素]
    eg.4
5.  元组相乘
    eg.5
6.  如何聪明的增加，减少元组元素[本质的方法]
    增加：tuple1=tuple1[:4]+(5,)+tuple1[4:]
    减少：tuple1=tuple1[:5]+tuple1[6:]
    
"""
