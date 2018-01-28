print("-------------大波哥-------------------")
temp = input("猜猜大波哥现在在想什么(答案1~9）:")
guess = int(temp)
if guess == 5:
    print('genius！！！')
while guess != 5:
    if guess>5:
        print("Opps!a little bigger")
    else:
        print('Opps!a little smaller')
    temp = input("one more time:")
    guess = int(temp)
    if guess == 5:
        print('genius！！！')
input("Press <enter>")
