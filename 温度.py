class celsius:
    def __init__(self,value=26.0):
        self.value=float(value)
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)
class fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel*1.8+32
    def __set__(self,insatnce,value):
        instance.cel=(float(value)-32)/1.8

class temprature:
    cel=celsius()
    fah=fahrenheit()
