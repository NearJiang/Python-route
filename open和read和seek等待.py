Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> q=open('C:\\Users\\Near\\Desktop\\New Text Document.txt')
>>> q.read(10)
'“小说”一词最早出现'
>>> q.tell()
20
>>> q.seek(45,0)
45
>>> q.readline()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    q.readline()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 12: illegal multibyte sequence
>>> q.readline()
''
>>> q.close()
>>> q=open('C:\\Users\\Near\\Desktop\\New Text Document.txt')
>>> q.seek(50,0)
50
>>> q.readline()
'干县令，其于大达亦远矣。」\n'
>>> list(q)
['庄子所谓的「小说」，是指琐碎的言论，\n', '与今日小说观念相差甚远。\n', '直至东汉桓谭《新论》：\n', '「小说家合残丛小语，近取譬喻，以作短书，治身理家，有可观之辞。」\n', '班固《汉书．艺文志》将「小说家」列为十家之后，\n', '其下的定义为：\n', '「小说家者流，盖出于稗官，街谈巷语，道听途说[4]之所造也。」\n', '才稍与今日小说的意义相近。\n', '而中国小说最大的特色，\n', '便自宋代开始具有文言小说与白话小说两种不同的小说系统。\n', '文言小说起源于先秦的街谈巷语，\n', '是一种小知小道的纪录。\n', '在历经魏晋南北朝及隋唐长期的发展，\n', '无论是题材或人物的描写，\n', '文言小说都有明显的进步，\n', '形成笔记与传奇两种小说类型。\n', '而白话小说则起源于唐宋时期说话人的话本，\n', '故事的取材来自民间，\n', '主要表现了百姓的生活及思想意识。\n', '但不管文言小说或白话小说都源远流长，\n', '呈现各自不同的艺术特色。']
>>> q.seek(0,0)
0
>>> for line in list(g)
SyntaxError: invalid syntax
>>> for line in list(g):
	print(line)

	
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    for line in list(g):
NameError: name 'g' is not defined
>>> for line in list(q):
	print(line)

	
“小说”一词最早出现于《庄子·外物》：

「饰小说以干县令，其于大达亦远矣。」

庄子所谓的「小说」，是指琐碎的言论，

与今日小说观念相差甚远。

直至东汉桓谭《新论》：

「小说家合残丛小语，近取譬喻，以作短书，治身理家，有可观之辞。」

班固《汉书．艺文志》将「小说家」列为十家之后，

其下的定义为：

「小说家者流，盖出于稗官，街谈巷语，道听途说[4]之所造也。」

才稍与今日小说的意义相近。

而中国小说最大的特色，

便自宋代开始具有文言小说与白话小说两种不同的小说系统。

文言小说起源于先秦的街谈巷语，

是一种小知小道的纪录。

在历经魏晋南北朝及隋唐长期的发展，

无论是题材或人物的描写，

文言小说都有明显的进步，

形成笔记与传奇两种小说类型。

而白话小说则起源于唐宋时期说话人的话本，

故事的取材来自民间，

主要表现了百姓的生活及思想意识。

但不管文言小说或白话小说都源远流长，

呈现各自不同的艺术特色。
>>> q
<_io.TextIOWrapper name='C:\\Users\\Near\\Desktop\\New Text Document.txt' mode='r' encoding='cp936'>
>>> for line in q:
	print(line)

	
>>> 
>>> g.seek(0,0)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    g.seek(0,0)
NameError: name 'g' is not defined
>>> q.seek(0,0)
0
>>> for line in q:
	print(line)

	
“小说”一词最早出现于《庄子·外物》：

「饰小说以干县令，其于大达亦远矣。」

庄子所谓的「小说」，是指琐碎的言论，

与今日小说观念相差甚远。

直至东汉桓谭《新论》：

「小说家合残丛小语，近取譬喻，以作短书，治身理家，有可观之辞。」

班固《汉书．艺文志》将「小说家」列为十家之后，

其下的定义为：

「小说家者流，盖出于稗官，街谈巷语，道听途说[4]之所造也。」

才稍与今日小说的意义相近。

而中国小说最大的特色，

便自宋代开始具有文言小说与白话小说两种不同的小说系统。

文言小说起源于先秦的街谈巷语，

是一种小知小道的纪录。

在历经魏晋南北朝及隋唐长期的发展，

无论是题材或人物的描写，

文言小说都有明显的进步，

形成笔记与传奇两种小说类型。

而白话小说则起源于唐宋时期说话人的话本，

故事的取材来自民间，

主要表现了百姓的生活及思想意识。

但不管文言小说或白话小说都源远流长，

呈现各自不同的艺术特色。
>>> 
