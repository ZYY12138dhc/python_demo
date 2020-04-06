#eg.1
#调用turtle模块
'''
>>> import turtle as t#t表示全权代表turtle
>>> t.pen()#[.后面表示模块里面的函数，函数是模块的一部分]
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> t.forward(100)
>>> t.left(90)
>>> 
'''

'''
#eg.2
#调用random库中randint函数，产生随机整数，并且以自定义函数的形式输出两个数相加结果
>>> import random as sjs
>>> def sj():
	a=sjs.randint(1,100)
	b=sjs.randint(1,100)
	print(a,'plus',b,'=',a+b)

	
>>> sj()
66 plus 25 = 91
>>> sj()
48 plus 56 = 104
>>> sj()
50 plus 44 = 94
>>> 
'''

'''
#eg.3
#调用time模块,显示电脑当前时间
>>> import time as t
>>> print(t.asctime())
Thu Dec 12 22:15:14 2019
>>> 
'''

'''
#eg.4
#调用sys模块
>>> import sys
>>> a=sys.stdin.readline()#sys模块-里面的对象stdin-里面的函数readline(),功能是输出原来输入的东西，功能单一
小庄老师
>>> print(a)
小庄老师

>>>

#测试，不使用a=sys.stdin.readline()也能输出原来输入的东西
>>> 123
123
>>> 345
345
>>>

>>> type(a)
<class 'str'>
>>>

'''

'''
#eg.5
#定义一个无参函数，使用sys.stdin.readline()代替输入语句input()
>>> def compare():
	age=int(sys.stdin.readline())
	if age>30:
		print('You so old!')
	else:
		print('You so young!')

		
>>> compare()
32
You so old!
>>> compare()
24
You so young!
>>> 

'''


'''
知识点：
1. 模块，将内置函数结合起来更强大的东西，需要先声明，有一些可以模块函数可以直接导入【例如print,input,for,range】
2. turtle模块
   eg.1[比如，当我们打上一点后，等待几秒中，python会显示关于这个模块的所有函数]
3. random模块/库
   eg.2
4. time模块
   eg.3
5. sys模块-里面的对象stdin-里面的函数readline(),输出对象为字符串
   eg.4
'''
