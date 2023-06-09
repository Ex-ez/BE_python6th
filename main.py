class Mobile:
    fp = 'yes'


realme = Mobile()
redmi = Mobile()
geek = Mobile()

print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(geek.fp)

Mobile.fp = 'no'
print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(geek.fp)
print('--------------')

realme.fp = 'Not Working'
print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(geek.fp)
