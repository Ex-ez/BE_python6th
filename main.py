a = {10, 20, 30}
a = {10, 20, 30, "멋쟁이사자", "Kang", 40}
a = {10, 20, 30, "멋쟁이사자", "Kang", 40, 10, 20}

new_set = a.copy()

b = set()
print(type(b))
a.add(50)
a.update([10, 20, 60, 70])
print(a)
a.remove('멋쟁이사자')
a.discard('멋쟁이사자')
a.discard(70)
print(a)

# new_set.clear()
# print(new_set)

intersection_a_new = a.intersection(new_set, a, b)
print(intersection_a_new)

union_a = a.union(new_set)
print('union_a:', union_a)

difference_a = a.difference(new_set)
print('difference_a:', difference_a)

print(b.issubset(a))
print(a.issuperset(b))

sym_a = a.symmetric_difference(new_set)
print('symmetric_difference:', sym_a)