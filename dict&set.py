d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

s = set ([1,1,2,2,2,3])
print(s) #重复元素在set中自动被过滤

# set可以看成数学意义上的无序和无重复元素的集合
# 两个set可以做数学意义上的交集、并集等操作

s1= set([1,3,5,6])
s2= set([1,5,7,8])
print(s1 & s2) #交集
print(s1 | s2) #并集

#list是可变对象,str是不可变对象,只能对可变对象进行操作
a=['b','c','a']
a.sort()
print(a)# a是list，对其进行操作可以使a内部发生变化
print("\n")

a='abc'
a.replace('a','A')
print(a) #结果不是Abc
print("\n")

a='abc'
b=a.replace('a','A')
print(b)
print(a)#b就可以输出Abc
#说明函数的作用是创建新字符串Abc，再让b指向新字符串
