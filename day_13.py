"""
#eg.1
>>> age = 26
>>> if age < 30:
	print('你可以称为一个小年轻！')

	
你可以称为一个小年轻！
>>> 

#eg.2
>>> age = 26
>>> if age < 30:
	print('你可以称为一个小年轻！')
		print('你真的可以称为一个小年轻！')
		
SyntaxError: unexpected indent
>>> 

>>> age = 26
>>> if age < 30:
	print('你可以称为一个小年轻！')
print('你可以称为一个小年轻！')
SyntaxError: invalid syntax
>>> 

>>> age = 26
>>> if age < 30:
	print('你可以称为一个小年轻！')
    print('你可以称为一个小年轻！')
    
SyntaxError: unindent does not match any outer indentation level
>>> 

#eg.3
>>> a=input('来一个数字....')
来一个数字....36
>>> print(a)
36
>>> type(a)
<class 'str'>
>>> 

>>> a=int(input('猜猜还记得庄老师的生日吗？'))
猜猜还记得庄老师的生日吗？24
>>> type(a)
<class 'int'>
>>> 
"""

#eg.4
a=int(input('猜猜还记得庄老师的生日吗？'))
if a == 728:
        print('i am so happy')
if a != 728:
        print('i am so angry')
        
b=int(input('how much 2 plus 3 ？ the answer is:'))
if a == 5:
        print('bingo!')
if a != 5:
        print('stupid')




"""
知识点：
1.  if else 语句[判断语句]
    1) 按下回车会自动缩进,只有缩进，才表示为一个功能块，四个空格
    2）返回结果为真，执行下面语句；返回结果为假，跳过判断语句
    3）不是同一个组块会报错，eg.2
2.  input语句后面无论输入什么，都是字符串
    eg.3
3.  




"""
