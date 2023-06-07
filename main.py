# 예제 1: range(j) 사용하기
for i in range(5):
    print(i)

# 예제 2: range(i, j) 사용하기
for i in range(2, 7):
    print(i)

# 예제 3: range(i, j, k) 사용하기
for i in range(1, 10, 2):
    print(i)

#예제 4: 음수 값 사용하기
for i in range(-1, -10, -2):
    print(i)

a = range(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print("Reverse Rage with start, stop, step")
r = range(5, 0, -1)
print((r[0]))
print((r[1]))
print((r[2]))
print((r[3]))
print((r[4]))