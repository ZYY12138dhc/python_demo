"""
《内置函数练习及答案》
知识点：
1.abs()绝对值
2.split()拆分功能
3. 
"""

>>> a=abs(-5)+abs(10)
>>> print(a)
15
>>> abs(-10)+10
20
>>> abs(-10)-10
0
>>> str1='i love china!'
>>> list1=str1.split()
>>> list1
['i', 'love', 'china!']
>>> for i in range(0,len(list1)):
	print(list1[i])

	
i
love
china!
>>> 
>>> text_file=open('C:/Users/15064/Desktop/01.txt')#打开文件
>>> text=text_file.read()#读取文件
>>> text2_file=open('C:/Users/15064/Desktop/paste.txt','w')#复制写入文件
>>> text2_file.write(text)
6
>>> text2_file.close()
>>> 
