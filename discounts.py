def discounts(price,rate):
    final_price = price * rate
    return final_price
oldprice = float(input('原价:'))
rate = float(input('折扣:'))
print('折后价:',discounts(oldprice, rate))
input('press[enter]')
