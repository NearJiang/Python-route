import time as q

class stopwatch:
    def __init__(self):
        self.unit=['年','月','天','分','钟']
        self.prompt='按下开始好不好'
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt
    __repr__=__str__  
        
    def start(self):
        self.begin=q.localtime()
        self.prompt='骚年，别急啊，你倒是停下来啊'
        print('开始')
            

    def stop(self):
        if not self.begin:
            print('骚年，别急啊，你倒是先跑起来啊')
        else:
            self.end=q.localtime()
            self._calc()
            print('结束')
        

    def _calc(self):
        self.lasted=[]
        self.prompt='共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                #self一定要记得带上！！！
                self.prompt += (str(self.lasted[index])+self.unit[index])
                #开头空格啊！
