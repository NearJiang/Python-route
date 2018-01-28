Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class C:
	def x(self):
		print('琪宝宝')

		
>>> c=C()
>>> c.x()
琪宝宝
>>> 
>>> class CC:
	def q(self,x,y):
		self.x=x
		self.y=y
                到这为止，不要去想有毛意义，他没意义，就是个仪式程序，必须这么写，就像上面的class C:def x(self):一样，只是它有俩个（x,y），所以就要写俩个
	def j(self):
		print(self.x,self.y)


class rectangle: 创造一个长方形
        def __init__(self,x,y): 初始化它的长和宽  
                self.x=x
                self.y=y
        def getperimeter(self):
                return(self.x+self.y)*2   
        def getarea(self):
                return self.x*self.y    return 用于后面可以得出“数字”
                                         print 是打出你自己diy的东西（一句话）
