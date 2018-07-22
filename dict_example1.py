message = 'It was a bright cold day in April, and the clocks were striking thirteen'   #定义字符串，即单个字符的列表
count = {}                                                                             #定义空字典
for character in message:                                                              #遍历字符串
    count.setdefault(character, 0)                                                     #初始化character键值
    count[character] = count[character] + 1                                            #更新character键值
print(count)