def year_old(x):
    while x>2017:
        print('骚年，你怕是要穿越哟！')
        return 0  
    if x == '2017':
        return 1 
    else:
        if 2017<x<1917:
            return 2017-x+1
        else:
            print('您这是活了一个世纪啊，快点将长生不老药秘方给我') 
            return 2017-x+1

q=int(input('请输入你的出生年数（例如1995））：'))
print('你的虚岁：%d' %year_old(q))
input('press[enter]')



返回数字的就 return
自己diy的句子就 print
