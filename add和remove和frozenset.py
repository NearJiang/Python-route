Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=[1,2,3,4,5]
>>> num.add(6)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    num.add(6)
AttributeError: 'list' object has no attribute 'add'
>>> num={1,2,3,4,5}
>>> num.add(6)
>>> num
{1, 2, 3, 4, 5, 6}
>>> num.remove()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    num.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> num.remove(5)
>>> num
{1, 2, 3, 4, 6}
>>> num.remove
<built-in method remove of set object at 0x0359F378>
>>> num
{1, 2, 3, 4, 6}
>>> num=frozenset()
>>> num.add(5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    num.add(5)
AttributeError: 'frozenset' object has no attribute 'add'
>>> num1=frozenset([1,2])
>>> num1.add(0)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    num1.add(0)
AttributeError: 'frozenset' object has no attribute 'add'
>>> num2=frozenset({1,2})
>>> nums.add(0)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nums.add(0)
NameError: name 'nums' is not defined
>>> num2.add(11)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    num2.add(11)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
