



"""
《内置函数3》
知识点：
1.eval()可以将program转换成表达式
2.exec()可以将program转换为函数使用,可以利用来读取外部文件或程序
3.float()
4.int()
5.round()

eg.1
>>> program='5+5'
>>> type(program)
<class 'str'>
>>> eval(program)#可以将program转换成表达式
10
>>>

eg.2
program='''
for i in range(0,11):
    print(i)'''

>>> exec(program)
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

eg.3
program='''
a=0
for i in range(0,11):
    a+=i
print(a)
'''

>>> exec(program)
55
>>>

eg.4
>>> float(12)
12.0
>>> float('-25')
-25.0
>>> float('3.5')
3.5

a=float(input('a='))
b=float(input('b='))
print(a,'+',b,'=',a+b)

a=4
b=5
4.0 + 5.0 = 9.0
>>> 

eg.5
>>> int(5)
5
>>> int(4.99)
4
>>> int(-6.79)
-6
>>> round(5.6)
6
>>> round(6.754,3)
6.754
>>> int('33')
33
>>>  

"""
