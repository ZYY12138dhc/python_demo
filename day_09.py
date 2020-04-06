#eg.1
#Pan[P要大写]
>>> import turtle
>>> p = turtle.Pen()
#方向是0°，路径是100（向前）像素
>>> p.forward(100)
#方向是0°，路径是50（向前）像素[比第一条长了一点]
>>> p.forward(50)
>>> p.left(90)
>>> p.right(180)
>>> p.backward(200)
#向左转一圈
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
>>> p.left(45)
#向右转一圈
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)
>>> p.right(45)

>>> p.clear()
>>> p.forward(150)
>>> p.right(90)
>>> p.forward(150)
>>> p.reset()

>>> p.circle(30)

#画两条平行线
>>> p.forward(150)
>>> p.right(90)
>>> p.up()
>>> p.forward(80)
>>> p.right(90)
>>> p.down()
>>> p.forward(150)



"""
知识点
1.  turtle[模块，组块]
    功能：绘图
    1)需要调用import
    2)调用手写功能，调用小窗口[p = turtle.Pen()][Python Turtle Graphics]
2.  p.forward[直行][向前像素单位，方向是0°]
    p.left(90)[左转90°]
    p.right(180)[右转180°]
    p.backward(200)[向后直行200像素单位，方向是0°]
    p.clear()[清屏，线段消失，箭头不消失]
    p.reset()[屏幕上线段和箭头都消失，箭头返回起点位置]
    p.circle()[画一个圆，value值为圆的半径]
    eg.1
    p.up()[抬笔，不做动作]
    p.down()[放笔，做动作]
3.  










"""
