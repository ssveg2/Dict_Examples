spam = {'color': 'red', 'age': 42}
print('Output Value in spam...')
for value in spam.values():
    print(value)
print('Output Key in spam...')
for key in spam.keys():
    print(key)
print('Output Key-Value in spam...')
for item in spam.items():
    print(item)
print('Output list of Keys')
print(list(spam.keys()))