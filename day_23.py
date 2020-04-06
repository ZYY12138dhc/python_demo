#eg.1
#函数参数可以为空
'''
>>> def chengfa():
	a=13
	b=15
	print('%s * %s ='%(a,b),a*b)

	
>>> chengfa()
13 * 15 = 195
>>>
'''

#eg.2
#作用域
'''
>>> a
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
'''

#eg.3
#函数参数外部调用
'''
>>> a=13
>>> b=15
>>> def chengfa(c1,c2):
	return (c1*c2)

>>> chengfa(a,b)
195
>>> chengfa(8,8)
64
>>>
'''

#eg.4
#累加程序
def leijia(s):
    number = 0
    for i in range(1,s+1):
        number +=i
    return print('result is :',number)

while True:
    a=input('尾数：')
    if a=='exit':
        break
    else:
        leijia(int(a))






'''
知识点：
1. 函数参数可以为空
   eg.1
2. 作用域问题
   eg.2,a,b的作用域都在函数chengfa里面，在函数以外无定义
3. 定义到函数体里的变量只适用于函数的函数体本身，在函数体外无权限使用；
   定义到函数外的变量，可用于全局，即为全局变量
4. 
'''
