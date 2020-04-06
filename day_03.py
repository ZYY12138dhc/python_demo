"""
#eg.1
str1 = 'zyy'
str1
print(str1)
str1 = "zyy"
str1
print(str1)
print("zyy")
"""

"""
#eg.2


>>> str1 = i
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str1 = i
NameError: name 'i' is not defined
>>> str1 = "i
SyntaxError: EOL while scanning string literal


str1 = 'i love you'
str1 = '''i
love
zyy'''
print(str1)

#加入空格，也算字符
str1 = '''  i
    love
    zyy'''
print(str1)

"""


"""
#eg.3

>>> a = 1
>>> b = 2
>>> a>b
False
>>> a<b
True
>>> a==b
False
>>> a!=b
True
>>>

>>> str1 = 'a'
>>> str2 = 'A'
>>> str3 = '1'
>>> str1>str2
True
>>> str1>str3
True
>>> str3>str2
False
>>> 

#输出字符的ASCII码
>>> str1 = 'a'
>>> print(ord(str1))
97
>>> 

#比较方式：一个一个进行比较
>>> str1 = 'abc'
>>> str2 = 'abcd'
>>> str1>str2
False
>>> 

#a...z的ASCII码依次增加，显然d大于a,所以str1<str2
>>> str1= 'abc'
>>> str2 = 'def'
>>> str1>str2
False
>>> >>> str1 = ' i wouldnn\'t love you '
>>> str1
" i wouldnn't love you "
>>> 
"""

"""
#eg.4
#只会识别离它最近的单引号进行匹配
>>> str1 = 'i wouldn't love you '
SyntaxError: invalid syntax
>>>
#解决方法
>>> str1 = ''' i wouldn't love you '''
>>> str1
" i wouldn't love you "
>>> 

>>> str1 = ' i wouldnn\'t love you '
>>> str1
" i wouldnn't love you "
>>>
"""

"""
#eg.5
>>> money = 100
>>> sentence = 'how can i get %s from him?'
>>> print(sentence%money)
how can i get 100 from him?
>>> print(sentence%120)
how can i get 120 from him?
>>>


>>> sentence = 'how much is %s plus %s ?'
>>> print(sentence%(1,2))
how much is 1 plus 2 ?
>>> 
"""

"""
#eg.6
>>> str1 = 'a'
>>> 10*str1
'aaaaaaaaaa'
>>> 

"""


"""
#eg.7
>>> str1 = 'zyy!\n'
>>> print(10*str1)
zyy!
zyy!
zyy!
zyy!
zyy!
zyy!
zyy!
zyy!
zyy!
zyy!

>>> 
"""

"""
#eg.8
%字符串相乘
>>> str1 = 'abc'
>>> str2 = 'def'
>>> print(str1+str2)
abcdef
>>> 

>>> str3 = 100
>>> print(str1+str3)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(str1+str3)
TypeError: can only concatenate str (not "int") to str
>>> 

#修改
>>> str3 = '100'
>>> print(str1+str3)
abc100
>>> 
"""


"""
知识点
1.  字符串
    [单引号和双引号]都可以命名
2.  单双引号要互相匹配
3.  三个单引号
    1)换行，回车[在字符串里面开头''',然后其它地方自由写]
    2)屏蔽单引号
    3)转义
    
4.  数字可以比较大小，字符也可以比较大小
5.  ASIIC 比较大小：小写字母>大写字母>数字
    
    ASCII码概念：
	每个字符在电脑存储的时候，都有一个机器码，也叫ASCII码(阿斯克码) 
	0-9数字的ASCII码是十进制的48-57,
	A-Z大写字母的ASCII码是十进制的65-90, 
	a-z小写字母的ASCII码是十进制的97-122, 
	所以，字符间比较大小，其实是ASCII码之间的大小比较。
6.  只会识别离它最近的单引号进行匹配
    eg.4
7.  转义字符\,加在标号前面，相当于标准化，合法化后面的字符。
    eg.4
8.  %s,相当于一个占位，s是前面定义的变量，也可以是自己输入一个数值
    eg.5

9.  字符串可以实现乘法
    eg.6
10. \n 换行
    eg.7
11. 字符串相乘
    数据类型需要相同才能一起运算
    eg.8

"""
