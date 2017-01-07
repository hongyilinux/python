str = "hello python"

l1 = list(str)

print('将字符串转换成列表')
print(l1)

tu1 = tuple(str)
print('将字符串转换成元组')
print(tu1)

set1 = set(str)
print('将字符串转换成集合：集合是没有次序的，会删除重复元素')
print(set1)

list2 = [('a',1),('b',2),('c',3),('d',4)]
dic1 = dict(list2)

print('把带有键值对的元组列表转换成字典')
print(dic1)



