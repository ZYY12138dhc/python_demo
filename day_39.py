"""
《内置函数（6）》
知识点：
1.in指令
2.count()计数
3.reverse()倒序排序
4.sort()排序
5.open()打开记事本,text()
6.write()写入记事本
"""
#eg.1
>>> str1='zyy'
>>> '' in str1
True
>>> 'l' in str1#判断l字符是否在str1内
False
>>> '2' not in str1
True
>>> str1='13214342535634575622222'
>>> str1.count('2')#统计字符串2在str1内出现几次
7
>>> str1='123'
>>> str1.join('leo')#见缝插针
'l123e123o'
>>> list1=[1,2,3,4,5]
>>> 1 in list1
True
>>> list1.reverse()#反转
>>> list1
[5, 4, 3, 2, 1]
>>>list1=[3,5,6,8,2,5,7,5,9,0]
>>> list1.count(5)
3
>>> list1=[3,5,7,23,78,95,7,5]
>>> list1.sort()
>>> list1
[3, 5, 5, 7, 7, 23, 78, 95]
>>> >>> list1.sort(reverse=True)
>>> list1
[95, 78, 23, 7, 7, 5, 5, 3]
>>>

>>> text_file=open('C:/Users/15064/Desktop/lo.txt')#读取文件
>>> text=text_file.read()
>>> print(text)
123
>>> 
>>> text_file=open('C:/Users/15064/Desktop/lo.txt','w')#写入文件
>>> text_file.write('may i write somrthing in your?')
30
>>> text_file.close()
>>> 
