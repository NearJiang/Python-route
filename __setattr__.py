class rectangle:
    def __init__(self,length=0,width=0):
        self.length = length
        self.width=width

    def __setattr__(self,name,value):
        if name=='square':
            self.length=value
            self.width=value
        else:
            super().__setattr__(name,value)

    def getarea(self):
        return self.length*self.width
