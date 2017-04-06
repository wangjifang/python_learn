#!/usr/bin/python
#coding=utf-8 
# 文件名：test.py
# 第一个注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
count = 1000 
miles = 1000.0
name = "jons"

print count
print miles
print name

a = b = c =  1
print a
print b
print c

count, miles, name = 1000, 1000.0, "jons"
print count
print miles
print name

s = "iloveyou"
print s[1:5]

str = 'Hello World!'
print str
print str[0]
print str[-6:-1]
print str[2:]
print str * 2
print str + "TEST"

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个的元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales', 2 : 'test'}
m = {'name':'wangjifang', 'age':'30'}
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
print tinydict[2]

abc = 111
res = isinstance(abc, long)
print res

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c 

c = a * b
print "3 - c 的值为：", c 

c = a / b
print "4 - c 的值为：", c 

c = a % b
print "5 - c 的值为：", c

a = 0

b = 20

print "a and b : ",  a and b

print "a or b : ", a or b

print "not a : ", not a


a = 10
b = 20
c = (1, 2, 3, 10)

if( a in c):
  print "a in c"
else:
  print "a not in c"

if(b not in c):
  print "b not in c"
else:
  print "b in c"

num = 9
if num >= 0 and num <= 10: 
    print 'hello'

num = 10
if num < 0 or num > 10:
    print 'hello'
else:
    print 'undefine'

num = 3
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = raw_input("Enter a number  :")
#    print "You entered: ", num

# print "Good bye!"
# 
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
 
print "Good bye!"

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print i,j