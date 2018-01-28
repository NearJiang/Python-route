grades = input('分数：')
num = int(grades)
if 90<num<=100:
    print('A')
else:
    if 80<=num<=90:
        print('B')
    else:
        if 60<=num<80:
            print('C')
        else:
            if 0<=num<60:
                print('D')
            else:
                while num>100 or num <0:
                    grades = input('输入错误，请输入0~100的数字,请重新输入：')
                    num = int(grades)
                    if 90<num<=100:
                        print('A')
                    else:
                        if 80<=num<=90:
                            print('B')
                        else:
                            if 60<=num<80:
                                print('C')
                            else:
                                if 0<=num<60:
                                    print('D')
input('press[enter]')
