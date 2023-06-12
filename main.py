a = ['a1', 'b2', 'c3']

for i in range(len(a)):
    print(i, a[i])

i = 0
for v in a:
    print(i, v)
    i += 1

for i, v in enumerate(a):
    print(i, v)