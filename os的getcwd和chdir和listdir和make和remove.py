Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Near\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir('D:\\')
>>> os.getcwd()
'D:\\'
>>> os.listdir('E:\\')
['$RECYCLE.BIN', "Rachel's English", 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'Screenshot', 'SHDownload', 'sohucache', 'System Volume Information']
>>> os.mkdir('E;\\python创造的目录')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.mkdir('E;\\python创造的目录')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'E;\\python创造的目录'
>>> os.mkdir('E;\\python')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.mkdir('E;\\python')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'E;\\python'
>>> os.mkdir('D;\\python')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.mkdir('D;\\python')
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'D;\\python'
>>>  os.mkdir('D:\\A')
 
SyntaxError: unexpected indent
>>> os.mkdir('E:\\Python')
>>> os.mkdir('E:\\Python\\再来一个')
>>> os.makedirs('E:\\多层目录\\来一个')
>>> os.remove('E:\\多层目录')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.remove('E:\\多层目录')
PermissionError: [WinError 5] 拒绝访问。: 'E:\\多层目录'
>>> os.remove('E:\\多层目录\\来一个')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.remove('E:\\多层目录\\来一个')
PermissionError: [WinError 5] 拒绝访问。: 'E:\\多层目录\\来一个'
>>> os.remove('E:\\多层目录\\来一个\\新建文本文档.txt')
>>> os.rmdir('E:\\多层目录\\来一个')
>>> os.remove('E:\\多层目录\\来一个')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    os.remove('E:\\多层目录\\来一个')
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'E:\\多层目录\\来一个'
>>> os.makedirs('E:\\多层目录\\来一个')
>>> removedirs('E:\\多层目录')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    removedirs('E:\\多层目录')
NameError: name 'removedirs' is not defined
>>> os.removedirs('E:\\多层目录')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    os.removedirs('E:\\多层目录')
  File "C:\Users\Near\AppData\Local\Programs\Python\Python36-32\lib\os.py", line 238, in removedirs
    rmdir(name)
OSError: [WinError 145] 目录不是空的。: 'E:\\多层目录'
>>> os.removedirs('E:\\多层目录\\来一个')
>>> 
