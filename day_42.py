"""
《递归算法（汉诺塔问题）》
知识点：
1.
2.

"""
def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        print(a,'->',c)
        move(n-1,b,a,c)

a=int(input('几个圆盘？'))
move(a,'a','b','c')
