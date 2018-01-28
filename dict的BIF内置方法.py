Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a={1:'大波',2:'小琪'}
>>> b=a.copy()
>>> b
{1: '大波', 2: '小琪'}
>>> c=a
>>> c
{1: '大波', 2: '小琪'}
>>> c[4]='four'
>>> c
{1: '大波', 2: '小琪', 4: 'four'}
>>> c.pop(4)
'four'
>>> c
{1: '大波', 2: '小琪'}
>>> c.setdefault(5,'蒋爸爸')
'蒋爸爸'
>>> c
{1: '大波', 2: '小琪', 5: '蒋爸爸'}
>>> d={6:'琪宝宝'}
>>> c.update(d)
>>> c
{1: '大波', 2: '小琪', 5: '蒋爸爸', 6: '琪宝宝'}
>>> c.clear
<built-in method clear of dict object at 0x02996570>
>>> c
{1: '大波', 2: '小琪', 5: '蒋爸爸', 6: '琪宝宝'}
>>> c.clear()
>>> c
{}
>>> 
