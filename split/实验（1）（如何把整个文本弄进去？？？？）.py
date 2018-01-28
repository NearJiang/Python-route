q = open('C:\\Users\\Near\\Desktop\\split\\chatting.txt.txt')

boy = []
girl =[]

f=open('C:\\Users\\Near\\Desktop\\split\\boy.txt','w')
g=open('C:\\Users\\Near\\Desktop\\split\\girl.txt','w')

for sentence in q:
    if sentence[:6] != '======':
        (role,line)=sentence.split(':',1)
        if role == '波':
            boy.append(line)
        if role == '琪':
            girl.append(line)
            
            f.wirtelines(boy)
            g.writelines(girl)
            
            f.close()
            g.close()

q.close()
