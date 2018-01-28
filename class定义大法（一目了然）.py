Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class rectangle: 
        def __init__(self,x,y):  
                self.x=x
                self.y=y
        def getperimeter(self):
                return(self.x+self.y)*2   
        def getarea(self):
                return self.x*self.y

        
>>> rect=rectangle(3,4)
>>> rect.getarea()
12
>>> rect.getperimeter()
14
>>> 
