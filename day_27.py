#eg.1

class dongwu:
    def chifan(self):
        print("chifan")
    def zoudong(self):
        print("zoudong")
    def huxi(self):
        print("huxi")

class jizhuidongwu(dongwu):
    def youjizhui(self):
        print("youjizhui")

class purudongwu(jizhuidongwu):
    def weinai(self):
        print("weinai")

class heixingxing(purudongwu):
    def zhilixingzou(self):
        print("zhilixingzou")
    def shiyonggongju(self):
        print("zhilixingzou")

==== RESTART: E:/巨无霸/DADALELE/lo/Python/day_27.py ====
>>> leo=heixingxing()
>>> nancy=heixingxing()
>>> leo.chifan()
chifan
>>> nancy.weinai()
weinai
>>> leo.shiyonggongju()
zhilixingzou
>>> leo.youjizhui()
youjizhui
>>> 

"""
知识点：
1. 类与对象（2）
2. 类传递对象需要用self来传递对象，

"""
