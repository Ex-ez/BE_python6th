from datetime import timedelta
from datetime import date
from datetime import datetime

td = timedelta(days=10)
print(td)

d1 = date(year=2023, month= 5, day= 5)
d2 = date(year=2023, month= 6, day= 9)

# 날짜의 연산자 오버로딩으로 비요할 수 있습니다.
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)

dt = datetime.today()

formatted_datetime = dt.strftime('%B, %d, %y')
print(formatted_datetime)