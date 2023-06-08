b = (10)
c = (10,)

print(b)
print(c)

d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, '멋쟁이사자')
f = 10, 20, -50, 21.3, '멋쟁이사자'

print(d, e, f,sep="\n")

print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[:3])
print(f[1:4])
print(f[3:])
g = c + f
print(g)
print(f * 5)
print(-10 in f)
print("===========")
h = (10, 20, -50, 20)
print(min(h), max(h))
print(h.count(20))
print(h.index(20))
sorted_a = sorted(h)
print(sorted_a)
a = (10, 20, -50)
x, y, z = a
print(x, y, z)

a = 1
b = 2
print(a, b)

a, b = b, a
print(a, b)