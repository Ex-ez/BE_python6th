show = lambda x: print(x)

show(5)

add = lambda x, y: (x + y)

print(add(5, 2))

add_sub = lambda x, y: (x + y, x - y)
a, s = add_sub(5, 2)

print(a)
print(s)

add = lambda x, y=3: (x + y)

print(add(5))