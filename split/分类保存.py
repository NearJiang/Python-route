q = open('C:\\Users\\Near\\Desktop\\python\\split\\chatting.txt.txt')

boy = []
girl = []
count = 1

for sentence in q:
    if sentence[:6] != '======':
        (role,line) = sentence.split(':',1)
        if role == '波':
            boy.append(line)
        if role == '琪':
            girl.append(line)
    else:
        z = 'boy' + str(count) + '.txt'
        x = 'girl' + str(count) + '.txt'
         
        j = open(z, 'w')
        s = open(x, 'w')
        
        j.writelines(boy)
        s.writelines(girl)

        j.close()
        s.close()
        

        boy = []
        girl = []
        count += 1

z = 'boy' + str(count) + '.txt'
x = 'girl' + str(count) + '.txt'
         
j = open(z, 'w')
s = open(x, 'w')
        
j.writelines(boy)
s.writelines(girl)

j.close()
s.close()

q.close()


    
