'''
#eg.1
#定义一个相加函数
def add(a,b):
    print('how much is %s plus %s equals '%(a,b),a+b)

a=int(input('加数：'))
b=int(input('被加数：'))
add(a,b)
'''

'''
#eg.2
#定义一个相加函数
def add(a,b):
    return a+b#返回所需要的值给被调用函数

while True:
    a=int(input('加数：'))
    b=int(input('被加数：'))
    print('how much is %s plus %s equals '%(a,b),add(a,b))
'''

#eg.3
def compare(a,b):
    if a>b:
        return print(a,'>',b)
    elif a<b:
        return print(a,'<',b)
    else:
        return print(a,'=',b)



'''
知识点
1. 返回值的使用return
2. return后面可接其它数值或函数
'''
