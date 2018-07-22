allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}         #定义字典，包含嵌套字典;
numBrought = 0                                              #初始化参数
for k, v in allGuests.items():                              #获取字典的键和值，分别赋值给k,v;
    numBrought = numBrought + v.get('apples', 0)            # v为一个字典，利用get()方法获取指定键名的值，若键不存在则用默认值
print(numBrought)