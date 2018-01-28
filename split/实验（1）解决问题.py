q = open('C:\\Users\\Near\\Desktop\\python\\split\\chatting.txt.txt')

boy = []
girl = []

for sentence in q:
    if sentence[:6] != '======':
        (role,line) = sentence.split(':',1)
        if role == '波':
            boy.append(line)
        if role == '琪':
            girl.append(line)
    else:
        z = 'boy.txt'
        x = 'girl.txt'
         
        j = open(z, 'w')
        s = open(x, 'w')
        
        j.writelines(boy)
        s.writelines(girl)

        j.close()
        s.close()
        

z = 'boy.txt'
x = 'girl.txt'

j = open(z, 'w')
s = open(x, 'w')
            
j.writelines(boy)
s.writelines(girl)
j.close()
s.close()

q.close()
       

