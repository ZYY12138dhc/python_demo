"""
《python常用模块（3）》
知识点：
1.keyword[关键字模块]
2.random[随机数]

#eg.1
>>> import keyword
>>> 
>>> keyword.iskeyword('if')
True
>>> keyword.iskeyword('for')
True
>>> keyword.iskeyword('zyy')
False
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> import random
>>> for i in range(0,100):
	print(random.randint(1,100),end=',')

	
22,74,96,16,15,4,55,84,68,98,42,26,97,85,74,65,59,33,72,62,90,53,66,9,85,55,7,21,72,27,86,24,66,62,84,45,39,92,84,80,62,13,20,28,49,36,58,95,63,63,98,94,6,93,10,95,25,27,14,60,72,3,15,90,71,27,97,37,5,6,88,2,77,41,75,68,83,88,50,41,11,7,94,23,89,21,90,86,96,90,8,33,7,81,48,32,80,43,52,23,
>>>

#eg.2
import random
t=1
number=random.randint(1,100)
while True:
    a=float(input('开始第%s此次猜测：'%t))
    if a>number:
        print('need lower!')
    elif a<number:
        print('need higher!')
    else:
        print('bingo!')
        break
    t+=1
    
    
#eg.3
import random as randomnumber
result = randomnumber.randint(1,100)
times = 1
print('我现在得到1--100之间的随机整数，猜猜数字是多少?')
while True:
    str1 ='你知道这个数字是多少么？请输入你的第%s次猜测：'
    guess = int(input(str1%times))
    times+=1
    if guess>100 or guess<1:
        print('你好聪明！')
        break
    elif guess>result:
        print('大了，往小的数猜！')
    elif guess<result:
        print('小了，往大的数猜！')

"""


#eg.4
>>> import random
>>> foodlist=['饺子','面包','面条','炒饭']
>>> print(random.choice(foodlist))
面条
>>> random.shuffle(foodlist)#洗牌
>>> foodlist
['面包', '饺子', '炒饭', '面条']
>>> 
