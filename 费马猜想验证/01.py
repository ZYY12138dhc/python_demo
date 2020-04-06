#费马猜想证明过程

print('请输入n方！')
n=int(input())
print('请输入合法数字的最大极限数！')
m=int(input())
a=int()
b=int()
c=int()
t=0
for a in range (0,m):
    if (a**n + b**n == c**n and a>0 and b>0 and c>0):
        print(a,b,c)
        t=t+1
    else:
        for b in range (0,m):
            if (a**n + b**n == c**n and a>0 and b>0 and c>0):
                print(a,b,c)
                t=t+1
            else:
                for c in range (0,m):
                    if (a**n + b**n == c**n and a>0 and b>0 and c>0):
                        print(a,b,c)
                        t=t+1
print('一共有',t,'种结果')
                        
            


    
