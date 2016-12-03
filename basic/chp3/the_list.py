squares = [1,4,9,16,25]

print(squares)

#list can be change
squares += [36,64,81,100]

print(squares)

cubs = [1,8,27,64]


#list 的两个操作，append，和pop

cubs.append(125)

cubs.append(6**3)

print(cubs)

res = cubs.pop()
print(res)
print(cubs)
print(cubs[1:3])


#list 的批处理

letters = ['a','b','c','d','f','g']

print(letters)

letters[2:5] = ['C','D',"E"]
print(letters)

print(len(letters))
