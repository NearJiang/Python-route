import time as q

class stopwatch:
    def __init__(self):
        self.prompt='按下开始好不好'
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt
    __repr__=__str__
        
    def start(self):
        self.begin=q.localtime()
        print('开始')

    def stop(self):
        self.end=q.localtime()
        self._calc()
        print('结束')

    def _calc(self):
        self.lasted=[]
        self.prompt='共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt += str(self.lasted[index])
