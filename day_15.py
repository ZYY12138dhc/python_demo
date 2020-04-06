"""
#eg.1
while True:
    a=input('enter your score:')#返回字符串
    if a=='exit':
        print('程序结束，感谢使用！')
        break
    elif int(a)>100 or int(a)<0:
        print('数据有错，请重新输入...')
    elif int(a) >=85 and int(a)<=100:
        print('优秀')
    elif int(a) >=60 and int(a)<=85:
        print('良好')
    elif int(a) <=60 and int(a)>=0:
        print('不及格')


#eg.2
>>> a=None
>>> type(a)
<class 'NoneType'>#什么类型都不是
>>> a+5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a+5
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'#类型错误
>>> a=5
>>> b='zyy'
>>> c=None#习惯变量命名
>>> print(c)
None
>>> a=None
>>> if a==None:
	print('i mean nothing!')

	
i mean nothing!
>>> 


while True:
    a=input('enter your score:')#返回字符串
    if a=='exit':
        print('程序结束，感谢使用！')
        break
    elif int(a)>100 or int(a)<0:
        print('数据有错，请重新输入...')
    elif int(a) >=85 and int(a)<=100:
        print('优秀')
    elif int(a) >=60 and int(a)<=85:
        print('良好')
    elif int(a) <=60 and int(a)>=0:
        print('不及格')

#测试：
enter your score:76.5
Traceback (most recent call last):
  File "F:/lo/Python/day_15.py", line 46, in <module>
    elif int(a)>100 or int(a)<0:
ValueError: invalid literal for int() with base 10: '76.5'
>>> 
>>> type(76.5)
<class 'float'>
>>> 
>>> int(76.5)
76
>>> 

"""


#改进
while True:
    a=input('enter your score:')#返回字符串
    if a=='exit':
        print('程序结束，感谢使用！')
        break
    elif float(a)>100 or float(a)<0:
        print('数据有错，请重新输入...')
    elif float(a) >=85 and float(a)<=100:
        print('优秀')
    elif float(a) >=60 and float(a)<=85:
        print('良好')
    elif float(a) <=60 and float(a)>=0:
        print('不及格')


>>> 3.4<9
True
>>> 3.4>0
True
>>> int(5.4+9)
14
>>> 





"""
知识点：
1）如果切换语句条件较多时，使用if...else语句不方便
2）使用if...elif语句
3）
"""
