alien_0 = {'color':'green','points':5}

#打印字典元素的方法
print(alien_0['color'])
print(alien_0['points'])

print('####################################')
#字典添加元素的方法 
alien_0['x_poisition'] = 25
alien_0['y_poisition'] = 35

print(alien_0)
print('####################################')

#遍历字典的方法：dic.items()
user_0 = {'username':'efermi','first':'enrico','last':'fermi'}

for k,v in user_0.items():
	print('\n key\t'+ str(k))
	print('value\t' + str(v))


print('####################################')

#遍历的第二个例子

favorite_language = {'jen':'python','sarah':'c','edwar':'ruby','phil':'python'}

for name,lang in favorite_language.items():
	print(name.title()+"'favorite language is " + lang.title() +'.')



print('####################################')
#遍历字典中所有的键值
for key in favorite_language.keys():
	print(key.title())

for val in favorite_language.values():
	print(val.title())


print('####################################\n')
print('按顺序遍历字典中所有的键')
for key in sorted(favorite_language.keys()):
	print(key.title())


print('过滤掉值列表中的重复元素，遍历值列表')

for val in set(favorite_language.values()):
	print(val.title())


print('字典列表示例')


alien_0 = {'color':'green','points':5}
alien_1 = {'color':'red','points':10}
alien_2 = {'color':'yellow','points':2}

alien_list = []

# 定义个空列表

alien_list.append(alien_0)
alien_list.append(alien_1)
alien_list.append(alien_2)

print(alien_list)


print('通过for循环，把字典添加到列表中 ')
aliens = []

for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
print (aliens[:5])

print('在字典中，存储列表')

favorite_language = {'john':['c','python'],'Dominic':['java','php','mysql'],'marry':['c','python','java']}

for name,lang in favorite_language.items():
	print('\n'+name.title()+"'favorite language is \t")
	for l in lang:
		print(l.title())



print('####################################\n')
print('在字典中存储字典')
school = {
		'BISU':{
				'name':'Beijing International study university',
				'addr':'chaoyang district',
				'feature':'language and turiasim'
			},
		'NCUT':{
				'name':'north technog universing',
				'addr':'shijingshan district',
				'feature':'computer sinecine'
			},
		'TJU':{
			'name':'Tianjing university',
			'addr': 'Tianjin',
			'feature':'all'
			}
	
	}

for name ,school_data in school.items():
	print("The school 's abbreviation is " + name)
	print('the full name is '+school_data['name'])
	print('the address is'+ school_data['addr'])
	print('the feature is '+ school_data['feature']+'\n')
