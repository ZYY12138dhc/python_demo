"""
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
    def test(self):
        print("%s is %s years old"%(self.name,self.age))

#eg.2
class test1:
    def print1(self):
        print(self.name)

class test2:
    def print2(self):
        print(self.name)


zyy1=test1()
zyy2=test2()
zyy1.name="111111"
zyy2.name="666666"

知识点：
1.self(自己)

2.
"""







