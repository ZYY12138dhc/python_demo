"""
《内置函数（4）》
知识点：
1.len()函数
2.

#eg.1
>>> len('hello world!')
12
>>> len([1,2,3,4,5,6])
6
>>> len([1,2,3,True,'zyy',3.14])
6
>>> tuple1=1,2,3,4
>>> len(tuple1)
4
>>> dict1={'zyy':165,'lo':170}
>>> len(dict1)
2
>>> list1=[1,2,3,True,'zyy',3.14]
>>> length=len(list1) 
>>> for i in range(0,length):
	print('此列表中第%s个元素是:%s'%(i,list1[i]))

	
此列表中第0个元素是:1
此列表中第1个元素是:2
此列表中第2个元素是:3
此列表中第3个元素是:True
此列表中第4个元素是:zyy
此列表中第5个元素是:3.14
>>>

#eg.2
while True:
    a = input('请输入6位密码：')
    length = len(a)
    for i in range(0,length):
        print('*',end='')
    if length == 6:
        print('\n谢谢您，密码位数正确！')
        break
    else:
        print('\n密码位数不正确，请重新输入！')

#eg.3
>>> max(1,2,3)
3
>>> max('0','a','A')
'a'
>>> 
>>> max('1,2,3,4,5,6')
'6'
>>> min('1,2,3,4,5,6')
','
>>>

"""

        
