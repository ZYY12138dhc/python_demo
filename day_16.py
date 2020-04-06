#if...else小练习
"""
#eg.1
money = 100
if money > 500:
    print('你好有钱！')
else:
    print('你好穷！')
        print('你需要工作了')#格式有误
        
"""
#eg.2
#猜数字游戏

import random as randomnumber
result = randomnumber.randint(1,100)#取一个随机的整数，范围是1--100
times = 1#记录猜了多少次
print('我现在得到1——100之间的随机整数，猜猜数字是多少?')

while True:
    str1='你知道这个数字是多少么?请输入你的第%s次猜测：'
    guess = int(input(str1%times))
    times+=1 #times=times+1
    if guess==result:
        print('你好聪明，猜对了！')
        break
    elif guess>result:
        print('大了，往小的数字猜！')
    elif guess<result:
        print('小了，往大的数字猜！')
    else:
        print('请注意！输入1~100之间的数字！')




"""
知识点：
1）random:随机函数


"""
