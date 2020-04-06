eg.1
使用“=”直接将一个列表赋值给变量即可创建列表对象
>>> a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
>>> a_list = []                              #创建空列表

eg.2
也可以使用list()函数将元组、range对象、字符串或其他类型的可迭代对象类型的数据转换为列表。
>>> a_list = list((3,5,7,9,11))
>>> a_list
[3, 5, 7, 9, 11]

eg.3
>>> list(range(1,10,2))
[1, 3, 5, 7, 9]

eg.4
>>> list('hello world')
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

eg.5
>>> x = list()                            #创建空列表

eg.
当不再使用时，使用del命令删除整个列表，如果列表对象所指向的值不再有其他对象指向，Python将同时删除该值。
>>> del a_list
>>> a_list
Traceback (most recent call last):
File "<pyshell#6>", line 1, in <module>
a_list
NameError: name 'a_list' is not defined
