#eg.绘制一个正方形
import turtle as p
p.reset()
p.Pen()
p.pencolor('red')
p.bgcolor('yellow')
p.pensize(5)
p.fillcolor('green')
p.begin_fill()

p.forward(150)
p.right(90)
p.forward(150)
p.right(90)
p.forward(150)
p.right(90)
p.forward(150)
p.right(90)

p.end_fill()

"""
知识点
1.  绘制一个正方形
    import turtle as p[调用时直接赋变量]
    p.pencolor('red')[画笔颜色]
    p.bgcolor('yellow')[背景颜色]
    p.pensize(5)[笔的粗细]
    p.fillcolor('green')[填充颜色]
    p.begin_fill().........p.end_fill()[只要是封闭区域，就填充颜色]
    
"""
