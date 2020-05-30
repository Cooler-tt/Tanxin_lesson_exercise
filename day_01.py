from func1 import func
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)
print(a is not b)
# list 数据类型
list1 = [1, 2, 3, 4]
# print(list1)
# print(type(list1))
# #添加append
# list1.append('a')
# print(list1)
# print(list1 + ['b'])
list2 = [1, 2, 3, 4, 'a', 'b', [1, 2, 3]]
print(list2[6][0])
a = [13, 24, 1, 56, 3, 64, 35, 54, 45, 7, 98, 102]
# a.sort(reverse=True)
# print(a)
# a.sort()
# print(a)
# 冒泡排序
# print(a)
# print(len(a))
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        # print(a)
print(a)
# 集合、字典
'''
set无序不重复的数据序列
'''
# set1 = {'1','2','3'}
# print(set1)
# set2 = set()
# print(set2)
# print('1' in set1)
# set3 = set('abcd')
# set33 = set(('a','b','c','d'))
# print(set33)
# set4 = set('aqwe')
# print(set3 | set4)
# print(set3 & set4)
# set4.clear()
# print(set3)
# set3.remove('a')
# print(set3,set4,sep='\n')
# 字典是一种可变容器类型，可以存储任意类型的对象
d1 = {1: 'Li Lei', 2: 'Lily'}
# print(d1)
# print(d1.keys())
# print(d1.values())
# keys = d1.get(2)
# print(keys)
# d1.setdefault(3,'Lucy')
# print(d1)
# d1[3] = 'Han Meimei'
# print(d1)
# d1[4] = 'Jack'
# del d1[1]
# print(d1)
# 元祖类型
t1 = (1, 2)
t3 = (3)
t33 = (3,)
t2 = 1, 2
t4 = ()
# print(t1,type(t1))
# print(t2,type(t2))
# print(t3,type(t3),t33,type(t33),sep='\n')
# print(type(t4))
mylist = ['a', 'b', 'c']
t5 = (1, 2, 3, 4, 5, mylist)
print(t5)
mylist[1] = 'd'
print(t5)
# 函数
func()
print(__name__)
