from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

print("배열 삽입 실습")
stu_roll.insert(1, 106)
stu_roll.insert(3, 107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("배열 요소 삭제")

stu_roll.remove(107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("배열 pop() 함수 실습")

element = stu_roll.pop(2)
print('element:', element)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("array index 메소드")
print(stu_roll.index(101))

print("extend() 메소드")
arr = array('i', [201, 208, 209])
stu_roll.extend(arr)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("reverse() 메소드")
stu_roll.reverse()
n = len(stu_roll)
i = 0
while i < n:
        print(stu_roll[i])
        i += 1