words = ['cat','window','defenstrate']

for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)

for w in words:
	print(w,len(w))

for w in words[:]:
	print(w,len(w))


for n in range(2,10):
	for x in range(2,n):
		if n%x == 0:
			print(n,'equals',x,'*',n//x)
			break
		else:
			print(n,'is a primer number')
			


def fib2(n):
	result = []    #define a empty list 
	a,b = 0,1
	while a < n:
		result.append(a)
		a,b = b,a+b
	return result

f100 = fib2(100)
print(f100)


print('######################################');

def f(a,l = []):
	l.append(a)
	return l

print(f(2))
print(f(3))

print('######################################');

def f(a,l = None):
	if(l is None):
		l = []
	l.append(a)
	return l

print(f(2))
print(f(3))

print('######################################');

def function(a):
	pass

