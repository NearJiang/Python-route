Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> mylist = ['蒋爸爸'.'琪宝宝','ourson']
SyntaxError: invalid syntax
>>> mylist = ['蒋爸爸','琪宝宝','ourson']
>>> picklejar = open('mylist.pickle','wb')
>>> pickle.dump(mylist, picklejar)
>>> picklejar.close()
>>> picklejar = open('mylist.pickle','rb')
>>> mylist2 = pickle.load(picklejar)
>>> print(mylist2)
['蒋爸爸', '琪宝宝', 'ourson']
>>> 
