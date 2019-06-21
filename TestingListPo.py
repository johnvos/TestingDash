maxLength = 5

list = []

count = 0

for i in range(0,20):
    count+=1
    if count > maxLength:
        list.pop(0)
    list.append(i)

print(list)
