# coding=utf-8
# !/usr/bin/python

'''
	Dictionary（字典）
	无序的键：值对集合
	键必须互不相同
'''

key1 = '000028'
key2 = '000029'
key3 = '000030'
key4 = '111111'

value1 = [42.96296296296296, 116.57754010695187, 12.764670296430731]
value2 = [80.31496062992126, 308.36012861736333, 22.87264217841441]
value3 = [39.26553672316384, 136.0, -9.832775919732441]
value4 = [11, 11, 11]


'''初始化字典'''
profit = {}

'''增加或修改键'''
profit[key1] = value1
profit[key2] = value2
profit[key3] = value3
profit[key4] = value4

'''获取键的对应值'''
print profit.get(key1)

'''获取键值列表'''
print profit.keys()

'''获取值列表'''
print profit.values()

'''判断键值是否存在'''
print profit.has_key(key1)


'''
3、如何更新字典？
a、添加一个数据项（新元素）或键值对
adict[new_key] = value 形式添加一个项
b、更新一个数据项（元素）或键值对
adict[old_key] = new_value
c、删除一个数据项（元素）或键值对
del adict[key] 删除键key的项 / del adict 删除整个字典
adict.pop(key) 删除键key的项并返回key对应的 value值

1、adict.keys() 返回一个包含字典所有KEY的列表；
2、adict.values() 返回一个包含字典所有value的列表；
3、adict.items() 返回一个包含所有（键，值）元祖的列表；
4、adict.clear() 删除字典中的所有项或元素；
5、adict.copy() 返回一个字典浅拷贝的副本；
6、adict.fromkeys(seq, val=None) 创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值（默认为None）；
7、adict.get(key, default = None) 返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）；
8、adict.has_key(key) 如果key在字典中，返回True，否则返回False。 现在用 in 、 not in；
9、adict.iteritems()、adict.iterkeys()、adict.itervalues() 与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表；
10、adict.pop(key[,default]) 和get方法相似。如果字典中存在key，删除并返回key对应的vuale；如果key不存在，且没有给出default的值，则引发keyerror异常；
11、adict.setdefault(key, default=None) 和set()方法相似，但如果字典中不存在Key键，由 adict[key] = default 为它赋值；
12、adict.update(bdict) 将字典bdict的键值对添加到字典adict中。
'''
