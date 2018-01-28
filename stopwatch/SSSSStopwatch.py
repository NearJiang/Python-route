import time as q

class stopwatch():
    def __init__(self):
        self.unit=['年','月','天','小时','分','秒']
        self.prompt="你还没说开始啊，骚年，怎么不按套路出牌呢"
        #一开始提示indented block，这种情况就是你空格缩进没搞好，重新空格缩进一下
        self.lasted=[]
        self.begin=0
        self.end=0
        
    def __str__(self):
        return self.prompt
    __repr__=__str__

    def __add__(self):
        prompt='总共运行了'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+self.unit[index])
        return prompt
    
    def start(self):
        self.begin=q.localtime()
        self.prompt='骚年，你还没说结束呢!'
        print('开始计时')
        
    def stop(self):
        if not self.begin:
            print('骚年,你干撒子哟，你倒是先说开始啊')
        else:
            self.end=q.localtime()    
            self._calc()
            print('时间到！')

    def _calc(self):
        self.lasted=[]
        self.prompt='你运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt+=(str(self.lasted[index])+self.unit[index])
        self.begin=0
        self.end=0
        

    

