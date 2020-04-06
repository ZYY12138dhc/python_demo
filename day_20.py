"""
#eg.1
for x in range(0,20):
    print('hello_%s'%x)
    if x<9:
        break

====================== RESTART: F:/lo/Python/day_20.py ======================
hello_0
>>> 


for x in range(0,20):
    print('hello_%s'%x)
    if x>9:
        break

====================== RESTART: F:/lo/Python/day_20.py ======================
hello_0
hello_1
hello_2
hello_3
hello_4
hello_5
hello_6
hello_7
hello_8
hello_9
hello_10
>>> 


#eg.2
#体重预测
weight=int(input('现在的体重是：'))
plus=int(input('预计每年增重多少kg:'))
print('您现在在月球上的体重是：',weight*0.165)
for year in range(0,10):
    print('您第%s年在月球上的体重：'%(year+1),int((weight+plus*year)*0.165))

====================== RESTART: F:/lo/Python/day_20.py ======================
现在的体重是：65
预计每年增重多少kg:3
您现在在月球上的体重是： 10.725
您第1年在月球上的体重： 10
您第2年在月球上的体重： 11
您第3年在月球上的体重： 11
您第4年在月球上的体重： 12
您第5年在月球上的体重： 12
您第6年在月球上的体重： 13
您第7年在月球上的体重： 13
您第8年在月球上的体重： 14
您第9年在月球上的体重： 14
您第10年在月球上的体重： 15
>>> 



#eg.3
age = input('您的年龄是：')
while age!='exit':
    if int(age)%2==0:
        for a in range(0,int(age)):
            if a%2==0:
                print(a,'',end='')
    else:
        for a in range(0,int(age)):
            if a%2!=0:
                print(a,'',end='')
    age = input('\n您的年龄是：')


====================== RESTART: F:/lo/Python/day_20.py ======================
您的年龄是：33
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 您的年龄是：
====================== RESTART: F:/lo/Python/day_20.py ======================
您的年龄是：33
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 
您的年龄是：45
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 
您的年龄是：23
1 3 5 7 9 11 13 15 17 19 21 
您的年龄是：

"""



"""
知识点
1）复习whlie循环，for循环,if..else判断语句
"""
