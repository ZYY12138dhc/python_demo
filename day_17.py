
#eg.1
#打印5个hello方法1
print('hello!')
print('hello!')
print('hello!')
print('hello!')
print('hello!')
#打印5个hello方法2
print('hello!\nhello!\nhello!\nhello!\nhello!\n')
#打印5个hello方法3
print('hello!\n'*5)

#eg.2
>>> for i in range(1,5):#i是循环变量,range是范围
	print('hello!')

	
hello!
hello!
hello!
hello!
>>> #为什么只出现4个hello

>>> for i in range(1,5):#i是循环变量,range是范围
	print('hello!+,',+i)

	
hello!+, 1
hello!+, 2
hello!+, 3
hello!+, 4
>>>

#修改
>>> for i in range(1,5):#i是循环变量,range是范围
	print('hello!+,',+i)

	
hello!+, 1
hello!+, 2
hello!+, 3
hello!+, 4
>>>

>>> for i in range(0,5):
	print('hello!+,',+i)

	
hello!+, 0
hello!+, 1
hello!+, 2
hello!+, 3
hello!+, 4
>>> 

hello!+, 4
>>> for i in range(1,6):
	print('hello!+,',+i)

	
hello!+, 1
hello!+, 2
hello!+, 3
hello!+, 4
hello!+, 5
>>> 

>>> for i in range(1,6):
	print('hello!+%s'%i)

	
hello!+1
hello!+2
hello!+3
hello!+4
hello!+5
>>> 

#eg.3
>>> list1 = ['zyy',True,75,3.14]
>>> for i in list1:
	print(i)

	
zyy
True
75
3.14
>>> 

>>> for i in list1:
	print('打印列表中的第%s项:'%a,i)#%a显示序号，i显示列表里面的元素
	a+=1

	
打印列表中的第1项: zyy
打印列表中的第2项: True
打印列表中的第3项: 75
打印列表中的第4项: 3.14


#eg.4

list1 = ['zyy',True,75,3.14]
a=1

for i in list1:
	print('打印列表中的第%s项:'%a,i)
	print('打印列表中的第%s项:'%a,i)
	a+=1


"""
知识点：
1）循环
    for i in range(1,5): #i是循环变量,range是范围
    eg.2
2）列表
   1. 列表是一个很包容的概念，可以容纳字符，布尔值，整型，浮点型
    eg.3

"""
