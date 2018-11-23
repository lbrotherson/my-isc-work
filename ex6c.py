something = 'Completely Different'
#print(dir(something))
count=0
for word in something:
    if 't' in word:
        count += 1
print(count)
