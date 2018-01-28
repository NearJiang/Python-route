Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.rename('E:\\SHDownload','搜狐下载')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    os.rename('E:\\SHDownload','搜狐下载')
PermissionError: [WinError 5] 拒绝访问。: 'E:\\SHDownload' -> '搜狐下载'
>>> os.rename('E:\\SHDownload','E:\\搜狐下载')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.rename('E:\\SHDownload','E:\\搜狐下载')
PermissionError: [WinError 5] 拒绝访问。: 'E:\\SHDownload' -> 'E:\\搜狐下载'
>>> os.rename('E:\\SHDownload,E:\\搜狐下载')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.rename('E:\\SHDownload,E:\\搜狐下载')
TypeError: Required argument 'dst' (pos 2) not found
>>> os.system('cmd')
-1073741510
>>> os.system('calc')
-1073741510
>>> os.curdir
'.'
>>> os.listdir(os.curdir)
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.name
'nt'
>>> 
