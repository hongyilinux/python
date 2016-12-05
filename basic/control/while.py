

print("第一个例子")
num  = 10

while num > 1:
	print(num)
	num = num -1
else:
	print("while is done")

print("第二个例子")

url = 'www.bisu.edu.cn'

while url:
	print(url)
	url = url[1:]


print("第三个例子")

x = 1 ;y = 10

while x < y:
	print(x,end=" ")
	x = x + 2

print("")

print("第四个例子")

url = "www.bisu.edu.cn"
while url:
	print (url)
	url = url[:-1]
else:
	print("game over")


print("第五个例子,用while循环显示列表中的元素")

li = [1,2,3,4,5,6,7,8,9,10]
count = 0

while count < len(li):
	print(li[count], end = " ")
	count += 1

print();

while li:
	print(li.pop(0),end = " ")

print()


li = [1,2,3,4,5,6,7,8,9,10]
while li:
	print(li[0],end = " ")
	li = li[1:]

print()

print("求100 以内所有偶数之和")

sum_odd = 0
num = 2 
while(num <= 100):
	sum_odd += num
	num += 2

print("the sum is %d"%sum_odd)

print("显示字典内所有的键值，并在显示结束后说明键的总个数")

dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'e':6,'1':1}
count = 0
li = list(dic)

while li:
	print(li.pop(0),end = " ")
	count += 1
else:
	print("\nthe count of keys is %d"%count)



print('列表：li1 = [0,1,2,3,4,5,6]  l2 = ["Sun","Mon","Tue","Wed","Fri","Sat"],构造字典，l1中的元素为键，\
		l2中的元素为值')

l1 = [0,1,2,3,4,5,6]  
l2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
count = 0
dic = {}
while count < len(l1):
	dic[l1[count]] = l2[count]
	count += 1

print(dic)

dic = {}

dic = dict(zip(l1,l2))
print(dic)
	
