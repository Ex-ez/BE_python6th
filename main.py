a = {10, 20, 30}
a = {10, 20, 30, "멋쟁이사자", "Kang", 40}
a = {10, 20, 30, "멋쟁이사자", "Kang", 40, 10, 20}

b = set()
print(type(b))
a.add(50)
a.update([10, 20, 60, 70])
print(a)
a.remove('멋쟁이사자')
a.discard('멋쟁이사자')
a.discard(70)
print(a)

new_set = a.copy()
new_set.clear()
print(new_set)