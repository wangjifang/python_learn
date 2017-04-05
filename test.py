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
