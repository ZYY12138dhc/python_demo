#如果条件语句只有两个结果，则使用if...else
#eg.1

a=int(input('how much is 2 plus 3 ? the answer is :'))
if a==5:
    print('bingo!')
else:
    print('stupid!')


#eg.2
while True:#为真，一直循环
    a=int(input('how much is 2 plus 3 ? the answer is :'))
    if a==5:
        print('bingo!')
        break#退出循环
    else:
        print('stupid!')

#eg.3
while True:
    a=input('enter your score:')#返回字符串
    if a=='exit':
        print('程序结束，感谢使用！')
        break
    if int(a)>100 or int(a)<0:
        print('数据有错，请重新输入...')
    else:
        if int(a) >=85 and int(a)<=100:
            print('优秀')
        if int(a) >=60 and int(a)<=85:
            print('良好')
        if int(a) <=60:
            print('不及格')


#eg.4
while True:
    a=input('enter your score:')#返回字符串
    if a=='exit':
        print('程序结束，感谢使用！')
        break
    if int(a)>100 or int(a)<0:
        print('数据有错，请重新输入...')
    else:
        if int(a) >=85 and int(a)<=100:
            print('优秀')
        else:
            if int(a) >=60 and int(a)<=85:
                print('良好')
            else:
                if int(a) <=60:
                    print('不及格')

    
"""
知识点：
1）if...else
2）break[跳出循环语句]
3）嵌套if...else
"""

"""
