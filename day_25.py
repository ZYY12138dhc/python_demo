#eg.1
'''
#地球上人的体重和月球上的体重计算
def moon_weight(now_weight,add_weight,year):#三个参数，当前体重，每年预计增加体重，增加年数
    print('this is on the moon your weight will be(kg):%s'%round(now_weight*0.165,2))
    for i in range(1,year):
        print('the %s\'s your on the moon your weight will be(kg):'%(i+1),round(0.165*(now_weight+i*add_weight),2))

while True:
    a=int(input('now_weight(kg):'))
    b=int(input('add_weight(kg):'))
    c=int(input('how many years do you wanna count？:'))
    if a==-1 or b==-1 or c==-1:
        print('that\'s all for today!')
        break
    moon_weight(a,b,c)
'''

#eg.2
#地球上人的体重和月球上的体重计算【增加模块】
import sys
def moon_weight(now_weight,add_weight,year):#三个参数，当前体重，每年预计增加体重，增加年数
    print('this is on the moon your weight will be(kg):%s'%round(now_weight*0.165,2))
    for i in range(1,year):
        print('the %s\'s your on the moon your weight will be(kg):'%(i+1),round(0.165*(now_weight+i*add_weight),2))

while True:
    print('now_weight:',end='')
    a=int(sys.stdin.readline())
    print('add_weight:',end='')
    b=int(sys.stdin.readline())
    print('years:',end='')
    c=int(sys.stdin.readline())
    if a==-1 or b==-1 or c==-1:
        print('that\'s all for today!')
        break
    moon_weight(a,b,c)



'''
知识点：
1.round(*,2),四舍五入,*表示求四舍五入的数，2表示保留到小数点后两位
2.

'''
