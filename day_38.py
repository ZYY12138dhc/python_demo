"""
《内置函数（5）》
知识点：
1.range()返回迭代器对象
2.

#eg.1
i=0
list1 = []
while True:
    a = input('请为列表添加元素，以exit结束添加！\n')
    if a == 'exit':
        break
    else:
        list1.insert(i,float(a))
        i+=1

print('您创建的列表是：',list1)
print('您创建的列表中最大数字是：%s'%max(list1))
print('您创建的列表中最小数字是：%s'%min(list1))
print('您创建的列表中数字相加和是：%s'%sum(list1))

#eg.2
>>> for i in range(0,11):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
>>> 

>>> list1=list(range(0,11))
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(range(0,10))
range(0, 10)
>>> for i in range(0,11):
	print(i,end=',')

	
0,1,2,3,4,5,6,7,8,9,10,
>>> for i in range(0,11,2):#增加了步长2
	print(i,end=',')

	
0,2,4,6,8,10,
>>> sum([1,2,3])
6  

>>> sum(list(range(1,101)))
5050
>>> 

"""


