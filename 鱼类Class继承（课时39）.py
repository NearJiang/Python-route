import random as q

class 大波龙王:
    def __init__(self):
        self.x = q.randint(0,10)
        self.y = q.randint(0,10)

    def move(self):
        self.x += 1
        print('位置：',self.x, self.y)

class 大个(大波龙王):
    pass

class 日天(大波龙王):
    pass

class 小杰子(大波龙王):
    def __init__(self):
        super()__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('饿啊，要吃~！！！')
            self.hungry = False
        else:
            print('吃饱了，这次算你走运')
    

