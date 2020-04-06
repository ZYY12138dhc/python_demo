"""

#eg.1

>>> list1 = [1,2,3,'zyy',True]
>>> list1[1]
2
>>> list1[4]
True

#eg.2
>>> list1[3]='lo'
>>> print(list1)
[1, 2, 3, 'lo', True]

#eg.3
>>> list1=[1,2,3]
>>> list2=['a','b','c']
>>> print(list1+list2)
[1, 2, 3, 'a', 'b', 'c']
>>> 

>>> list1=['i love']
>>> list2=['zyy!']
>>> print(list1+list2)
['i love', 'zyy!']
>>> 

#eg.4
#嵌套列表
>>> list1=[1,2,3,'zyy',[1,2,3],True]
>>> list1[4]
[1, 2, 3]
>>> 

#eg.5
#在列表尾加一个元素
>>> list1 = [1,2,3,'zyy',True]
>>> list1.append(0.5)
>>> list1
[1, 2, 3, 'zyy', True, 0.5]
>>> 
#加多个元素
>>> list1+[-8,10,'zyy']
[1, 2, 3, 'zyy', True, 0.5, -8, 10, 'zyy']
>>> 

#在列表里面加一个字列表
>>> list1.append([8,8,8])
>>> list1
[1, 2, 3, 'zyy', True, 0.5, [8, 8, 8]]
>>> 

#eg.6
#在指定位置加入元素
>>> list1=[1,2,3,4,6]
>>> list1.insert(4,5)
>>> list1
[1, 2, 3, 4, 5, 6]
>>> 

#eg.7
#删除列表中指定的元素
>>> list1=[1,2,3,4,5,6]
>>> del list1[4]
>>> list1
[1, 2, 3, 4, 6]
>>> 

#eg,8
#删除指定位置后面所有的元素
>>> del list1[2:]
>>> list1
[1, 2]
>>> 

#eg.9
#读取列表中从0位置开始的所有元素
>>> list1[0:]
[1, 2, 3, 4, 5, 6]
>>> 

#eg.10
#读取列表中指定位置之前的所有元素，不包括当前位置
>>> list1[:3]
[1, 2, 3]
>>> 

#eg.11
#删除整个列表
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> 

#eg.12
#列表相乘
>>> list1=[1,2,3]
>>> list1*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 

#eg.13
#如何换行
>>> list1=[1,2,3,'\n']
>>> list1*5
[1, 2, 3, '\n', 1, 2, 3, '\n', 1, 2, 3, '\n', 1, 2, 3, '\n', 1, 2, 3, '\n']



#eg,14
>>> list1 = [1,2,3,'zyy',True]
>>> list1/2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list1/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> 


"""

"""
知识点
1.  列表[]
    标号从0开始，
2.  列表里面可以放数字，字符串，布尔值
3.  可以修改特定的列表里面的元素
    eg.2
4.  列表可以相加
    eg.3
5.  列表可以嵌套
    eg.4
6.  sppend()函数，在列表尾加一个元素
    eg.5
7.  #在指定位置加入元素
    #eg.6
8.  #删除列表中指定的元素
    #eg.7
9.  #删除指定位置后面所有的元素
    #eg,8
10. #读取列表中从0位置开始的所有元素
    #eg.9
11. #读取列表中指定位置之前的所有元素，不包括当前位置
    #eg.10
12. #删除整个列表
    #eg.11
13. #列表相乘
    #eg.12

14.

15. 列表不能和整型进行减法，除法运算


"""
