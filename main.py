stu = {101: 'Kim', 102: 'Bae', 103: 'Hong'}
fees = {'kim': 2000, 'bae': 3000, 'hong': 8000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['kim'])
print(fees['bae'])
print(fees['hong'])

stu[102] = 'Python'

print(stu)

stu[104] = '멋쟁이사자'

print(stu)

del stu[102]

print(stu)

print(102 not in stu)

# stu.clear()

print(stu)

new_stu = stu.copy()

key = (101, 102, 103)
value = '멋쟁이사자'
new_stu = dict.fromkeys(key, value)

print(new_stu)
print(stu[101])
print(stu.get(101))
print(stu.items())
print(stu.keys())
print(stu.values())
stu[104] = '멋쟁이사자'
print(stu)
stu.update({104: '멋쟁이사자2'})
print(stu)
stu.pop(104)
print(stu)
stu.pop(104, 'No Value')
stu.setdefault(104, 'Park')
print(stu)

print(stu.popitem())
print(stu.popitem())
print(stu.popitem())
