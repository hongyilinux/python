
f_passwd = open('../../passwd','r')

f_text = open('../../test.txt','w')

'''
for line in f_passwd.readlines():
	f_text.write(line)

'''

f_text.writelines(f_passwd.readlines())


f_passwd.close()
f_text.close()


