"""
《递归算法（斐波那切数列）》
知识点：
1.递归：自己调用自己的方法,从上往下传递。
2.斐波那切数列：


#eg.1阶乘的计算
while True:
    def jiecheng(s):
        result=1
        for i in range(1,s+1):
            result=result*i
        return result
    a=int(input('a=?'))
    if a==0:
        break
    else:
        print('%s的阶乘结果是：%s'%(a,jiecheng(a)))


#eg.2阶乘的计算
while True:
    def jiecheng(s):
        if s==1:
            return 1
        else:
            return s*jiecheng(s-1)
    a=int(input('a=?'))
    if a==0:
        break
    else:
        print('%s的阶乘结果是：%s'%(a,jiecheng(a)))


"""

#eg.3
while True:
    def fab(n):
        if n<1:
            print('error!')
        if n==1 or n==2:
            return 1
        else:
            return fab(n-1)+fab(n-2)
    a=int(input('a=?'))
    print('result=%s'%fab(a))
            








