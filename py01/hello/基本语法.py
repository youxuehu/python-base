# 打印
print(1)
# 定义列表
list = ['apple', 'origin', 'balnana']
print(list)
# 遍历列表
for index, name in enumerate(list):
    print('name[{}]={}'.format(index, name))
    print(index)
    print(name)
# 字典
dictionary = {'name': "zhangsan", 'age': '30'}
# 遍历打印
print(dictionary)
# 逐个打印key
for key in dictionary.keys():
    print('key={}'.format(key))
# 逐个打印value
for value in dictionary.values():
    print('value={}'.format(value))
# 逐个打印key和value
for key, value in dictionary.items():
    print('{key}:{value}'.format(key=key, value=value))
# 变量输出
name = '张三'
print('my name is %s' % name)
age = 20
print('my name is %s, age is %d' % (name, age))
money = 100.5
print('共%f' % money)
print('共%2.2f' % money)
print('共%83.2f' % money)
# 输出集合
s = set('123456789')
# s = {'a', 'b', 'c'}
s.add('d')
print(s)
s.update('efg')
print(s)
s.remove('1')
print(s)
s.discard('sdsadsa')
print(s)
s.pop()
print(s)
# del s
# print(s)
s -= set('123456789')
print(s)
s1 = set('ef33vfvfv3423432')
# 取交集
s2 = s.intersection(s1)
print(s2)
s3 = s & s1
print(s3)
# 取并集
s4 = s.union(s1)
print(s4)
s5 = s | s1
print(s5)
# 取差集
s6 = s.difference(s1)
s6 = s - s1
print(s6)
# 取对称集
s7 = s.symmetric_difference(s1)
s7 = s ^ s1
print(s7)
print('遍历列表一')
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)
    # print('序号%s,值%s' % (list1.index(i) + 1, i))
# 打印集合下标
print('打印列表下标')
for i in range(len(list1)):
    # print('下标：$d,值：%d' % (i, list1[i]))
    print(i)
print('打印列表值')
for i in range(len(list1)):
    # print('下标：$s,值：%s' % (i, list1[i]))
    print(list1[i])
print('遍历列表三')
for i, val in enumerate(list1):
    print('下标：%s,值：%s' % (i, val))
# 元组
print('元组')
arr = 111, 'aaa'
print(arr[0])

