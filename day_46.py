"""
《python常用模块（4）》
知识点：
1.sys[接收键盘值]
2.time()
3.sleep[延迟]
#eg.1
>>> import sys
>>> a=sys.stdin.readline()
你好吗
>>> a
'你好吗\n'
>>> print(a)
你好吗

>>> a=sys.stdin.readline(10)
hello,my name zyy
>>> a
'hello,my n'
>>> sys.stdout.write('hello world!')
hello world!12
>>> sys.version
'3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]'
>>>

>>> import time
>>> time.asctime()
'Fri Apr 17 14:22:26 2020'
>>> tuple=(2020,4,5,15,34,55,2,0,0)
>>> time.asctime(tuple)
'Wed Apr  5 15:34:55 2020'
>>> t=time.localtime()
>>> t
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=17, tm_hour=14, tm_min=25, tm_sec=30, tm_wday=4, tm_yday=108, tm_isdst=0)
>>> t.tm_year
2020
>>> t.tm_hour
14
>>> t.tm_wday
4
>>> t[0]#当成列表
2020
>>> t[1]
4
>>> t[2]
17
>>> t[3]
14
>>> t[4]
25
>>> t[5]
30
>>> time.time()
1587104941.522555#1970年到现在的秒数 
>>> 


#eg.2
#计算打印100个数字的时间
import time
t1=time.time()
for i in range(0,99):
	print(i)
t2=time.time()
print('it took python %s seconds tp finish!'%(t2-t1))

"""

#eg.3
import time
for i in range(0,9):
    print(i)
    time.sleep(1)
