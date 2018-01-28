Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.path.basename('E:\\A\\B\\C')
'C'
>>> os.path.dirname('E:\\A\\B\\C')
'E:\\A\\B'
>>> os.path.join('E:\\','A')
'E:\\A'
>>> os.path.split('E:\\a\\b\\c')
('E:\\a\\b', 'c')
>>> os.path.splitext('E:\\a\\b\\modern.family')
('E:\\a\\b\\modern', '.family')
>>> os.path.splitext('E:\\a\\b\\modern_family.mp4')
('E:\\a\\b\\modern_family', '.mp4')
>>> os.path('E:\\a\\b\\modern_family.mp4')
