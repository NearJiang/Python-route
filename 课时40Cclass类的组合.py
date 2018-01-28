class Turtle:
    def __init__(self,x):self没有实际含义，单纯的创class时要写在第一位，一定要写
        self.num=x 别管什么self什么意思啊之类的，这句表达的就是 num=x

class Fish:
    def __init__(self,x):
        self.num=x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)

    def print_num(self):
        print('Pool中有%d个乌龟，%d条鱼'%(self.turtle.num,self.fish.num))


class xxx:
    def __init__(self,x):
        self.num=x
        
    def xxx(self):
        print('   ')
class的俩种def后的形式。init就没print。不然就print。
