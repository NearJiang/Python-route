import time as q

class stopwatch:
    def start(self):
        self.begin=q.localtime()
        print('开始')

    def stop(self):
        self.end=q.localtime()
        self.lasted=[]
        print('结束')

    def _calc(self):
        self.lasted=[]
        self.prompt='共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt += str(self.lasted[index])
        return prompt
