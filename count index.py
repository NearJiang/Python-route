Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dir（list）
SyntaxError: invalid character in identifier
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> list = [1,2,3,4,5,6]
>>> list.count(123)
0
>>> list.count(1)
1
>>> list.count(2)
1
>>> list.index(5)
4
>>> list.index(5,3,5)
4
>>> list.index(5,1,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list.index(5,1,3)
ValueError: 5 is not in list
>>> 
