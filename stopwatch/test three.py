import time as q

class stopwatch:
    def start(self):
        self.begin=q.localtime()
        print('开始')

    def stop(self):
        self.lasted=[]
        self.end=q.localtime()
        print('结束')

    def _calc(self):
        self.lasted=[]
        self.prompt='共运行了'
        self.prompt += self.lasted
        return prompt
