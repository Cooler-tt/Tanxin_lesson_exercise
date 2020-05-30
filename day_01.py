a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is not b)
#list 数据类型
list1 = [1,2,3,4]
# print(list1)
# print(type(list1))
# #添加append
# list1.append('a')
# print(list1)
# print(list1 + ['b'])
list2 = [1,2,3,4,'a','b',[1,2,3]]
print(list2[6][0])
a = [13,24, 1, 56, 3, 64, 35, 54,45, 7, 98,102]
# a.sort(reverse=True)
# print(a)
# a.sort()
# print(a)
#冒泡排序
print(a)
print(len(a))
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        # print(a)
print(a)






