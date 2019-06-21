a = [
    {'hello':'bye'},
    {'hello':'bleh'}
]

b = [
    {'kill':'me'},
    {'kill':'you'}
]


for i in range(0,len(a)):
    print(i)
    print(a[i])
    print(b[i])
    a[i]['kill'] = b[i]['kill']

print(a)
print(b)