Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list = [1,2,3,4,5]
>>> list.reverse
<built-in method reverse of list object at 0x02F310A8>
>>> list.reverse()
>>> 
>>> list
[5, 4, 3, 2, 1]
>>> 
>>> 
>>> list1 = [9,5,6,3,6,7]
>>> list.sort
<built-in method sort of list object at 0x02F310A8>
>>> list.sort()
>>> list
[1, 2, 3, 4, 5]
>>> list1.sort
<built-in method sort of list object at 0x02F31080>
>>> list1.sort()
>>> list1
[3, 5, 6, 6, 7, 9]
>>> 
>>> 
>>> list2 = [4,10,4,6,3,7]
>>> list.sort(reverse=True)
>>> list2.sort(reverse=True)
>>> list2
[10, 7, 6, 4, 4, 3]
>>> 
