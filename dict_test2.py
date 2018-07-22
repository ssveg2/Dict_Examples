spam = {'color': 'red', 'age': 42}         #定义字典;
if 'name' not in spam:                     #判断name是否为spam中的键，可写为：if 'name' not in spam.keys():
    spam['name'] = 'PATAC'                 #添加键-值对;
print(spam)                                #输出字典;
spam.setdefault('Sex', 'male')             #Sex为要检查的键名称，male为如果键不存在时要设置的值;
print(spam['Sex'])                         #Sex-male键值对被添加到字典
spam.setdefault('age', 18)                 #age键在字典中，值18无效，仍输出字典中的42;
print(spam['age'])