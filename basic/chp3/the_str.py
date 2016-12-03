#使用转义字符

print(' "Isn\'t " she said.')

s = 'Fisrt line \n Second line'

print(s)

print(r'C:\some\name')#注意有转义字符 raw string 取消转义字符的功能


#can span mutilple lines 

print("""\
Usage:thingy[OPTIONS]
	-h 				Display this usage message
	-H	hostname	Hostname to connect to 
""")


print('py'*3 +'thon')
print(3*'py' + 'thon')

#take care the store of the string

word = "python"

print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])
#print(word[-7])  #会产生索引越界



#注意中间是冒号，不是逗号
print(word[0:2]) #0到2 ，包含0，不包含2

print(word[:2])  #0到2 ，包含0，不包含2

print(word[3:5]) #3到5，包含3，不包含5 

print(word[3:])	 #3到最后一个

print(word[3:1024]) #3到最后一个

print(word[-2:]) #倒数第二个到最后一个

print(word[-5:-4]) #倒数第五个（包含），到倒数第四个（不包含 ）


