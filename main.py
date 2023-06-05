# 명시적 타입 변환
q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r, type(r))

r = str(q) + u
print(r, type(r))