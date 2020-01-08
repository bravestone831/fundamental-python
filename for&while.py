# for x in循环就是把每个元素带入变量x,然后执行缩进语句

#依次输出
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#计算总值
sum = 0 
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


#输出0-10的每一个值
for x in range(11): 
    print(int(x))

sum = 0 #求1-100的和
for x in range(101):
    sum = sum+x
print(sum)



s=0
n=1
while n<100:#条件不满足时退出循环
    s=s+n
    n=n+2
print(s)

#尽量不用break和continue,避免死循环

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环,后续语句不再执行
    print(n)
    n = n + 1
print('END')


#continue直接进行下一轮循环,后续语句不执行
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
