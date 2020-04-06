#乘法表01
for i in range(9):#从0循环到8
  i += 1#等价于 i = i+1
  for j in range(i):#从0循环到i
    j += 1
    print(j,'*',i,'=',i*j,end = ' ',sep='')
    # end默认在结尾输出换行，将它改成空格 sep 默认 j,'*',i,'=',i*j 各元素输出中间会有空格
  print()#这里作用是输出换行符
#乘法表02
i = 1
while i <= 9:
  j = 1
  while j <= i:
    print("%d*%d=%d" % (j,i,i*j),end=' ') # 格式化输出
    j += 1
  i += 1
  print()
 
