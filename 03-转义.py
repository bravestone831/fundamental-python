#文本和字符串是有区别的
print(5+8)
print('5'+'8')

#对'转义
print('I don\'t have job interviews and I\'m very disappointed.')

str = 'C:\now'
print(str)
str= 'C:\\now'#用\对自身进行转义
print(str)

#对于很多\ 使用原始字符串r而不是使用转义
str = r'C:\now\document\politics\study'
print(str)

#但是r后面语句的末尾不能有\
#如果非要加\就只能print的时候加一个\，通过转义\实现
str = r'C:\now\document\politics\study''\\'
print(str)

#计算几年有多少秒
days_per_year = 365
hours_per_day = 24
minute_per_hour = 60
second_per_minute = 60
n = int(input('How many years do you want to calculate:'))
result_is = days_per_year*hours_per_day*minute_per_hour*second_per_minute*n
print('the result you want is:',result_is)
