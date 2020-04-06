"""
#eg.1
>>> foods_list=['milk','mango','beer']
>>> sports_list=['football','swimming']
>>> print('my favourite foods :\n',foods_list)
my favourite foods :
 ['milk', 'mango', 'beer']
>>> print('my favourite sports :\n',sports_list)
my favourite sports :
 ['football', 'swimming']
>>> 

#eg.2
>>> 100*4+45*2+50*4+100*2
890
>>> 

#eg.3
>>> str_name='zyy'
>>> str_hello='hello'
>>> str_hello='hello!%s'
>>> print(str_hello % str_name)
hello!zyy
>>>

"""

#eg.4
shop={'cola':4,'hamburger':6.5,'hotdog':3.5,'pizza':16}
a = int(input('cola:'))
b = int(input('hamburger:'))
c = int(input('hotdog:'))
d = int(input('pizza:'))
total_price = a*shop['cola']+b*shop['hamburger']+c*shop['hotdog']+d*shop['pizza']
hint = 'you need pay %s yuan!'
print(hint % total_price)

cola:1
hamburger:5
hotdog:7
pizza:0
you need pay 61.0 yuan!
>>> 



"""
阶段性练习
1.  列出自己最喜爱的食物列表和运动项目列表,并且打印
    eg.1
2.  算术题
    动物园里面有100只大象，45只鸭子，50只鳄鱼，100只小鹿，用python计算全部动物有多少只脚
3.  利用占位符输出自己的名字
    #eg.3
4.  可乐[4]，汉堡包[6.5]，pizza[16],热狗[3.5][强行转换int()]
    eg.4
    
"""
