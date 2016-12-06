import os

file_test_txt = open('../../test.txt','w+')

if not file_test_txt.writable():
	print("open error")

list_dir = os.listdir('/etc')

for list_item in list_dir:
	file_test_txt.write(list_item+"\n")




file_test_txt.close()


