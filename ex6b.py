s = 'I love to write Python.'
split_s=s.split()
print(split_s)
for word in split_s:
    if 'i' in word:
        print('I found \'i\'.')
for word in split_s:
    if word.find('i') !=  -1:
        print('I found \'i\'.')
    else: 
        print('Fail')
