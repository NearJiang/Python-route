question = input('how many days to test？：')
num = int(question)
if num == 4:
    print('yeah,thx')
while num != 4:
    if num>4:
        print('a little more')
    else:
        print('it\'s less')
    que = input('how many:')
    num = int(que)
    if num == 4:
        print('awesome!')
input('press[enter]')
