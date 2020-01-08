#if语句是自上而下判断，也就是说，if遇到第一个满足条件（判断为true）的语句，
#就停止下面所有的判断(跳出if)

s = int(input('Please enter your age:'))
if s >6:
    print('teen')
elif s >18:
    print('you\'re old')
else:
    print('kid')

birth = int(input('birth: '))#input返回是str,不能和2000这个整型比较，所以加int
if birth < 2000:
    print('00前')
else:
    print('00后')

#BMI
a=float(input('Please enter your height:'))
b=float(input('Please enter your weight:'))
c= b/(a*a)

if c<18.5:
    print('too thin')
elif c>18.5 and c<25:
    print('normal')
elif c>=25 and c<28:
    print('overweight')
else:
    print('obesity')
