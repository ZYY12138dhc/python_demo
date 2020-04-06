"""
#eg.1
#zyy是key值，173是value值
>>> dict1={'zyy':173,'zyy2':180,'zyy3':175}
>>> dict1['zyy']
173
>>> 

#eg.2
#删除某一个字典元素
>>> del dict1['zyy']
>>> dict1
{'zyy2': 180, 'zyy3': 175}
>>> 
#删除整个字典
>>> del dict1
>>> dict1
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    dict1
NameError: name 'dict1' is not defined
>>>

#eg.3
>>> dict1={'zyy':173,'zyy2':180,'zyy3':175}
>>> dict1['zyy']=185
>>> dict1
{'zyy': 185, 'zyy2': 180, 'zyy3': 175}
>>> 

#eg.4
>>> dict1={'zyy':173,'zyy2':180,'zyy3':175}
>>> dict2={'a':1,'b':3}
>>> dict1+dict2
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict1+dict2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>>

#字符串相加
>>> 'abc'+'def'
'abcdef'

#列表相加
>>> [1,2,3,]+[4,5,6]
[1, 2, 3, 4, 5, 6]
#元组相加
>>> (1,2,3,)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> 


"""




"""
知识点
1.  字典map[dict]
    eg.1
2.  删除某一个字典元素[del dict1['zyy']]
    删除整个字典[del dict1]
    eg.2
3.  修改字典中某个值[dict1['zyy']=185]
    eg.3
4.  加法不支持字典类型运算
    eg.4
5.  
"""
